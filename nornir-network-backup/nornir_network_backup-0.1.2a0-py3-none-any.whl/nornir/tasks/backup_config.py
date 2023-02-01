import datetime
import logging
from pathlib import Path

from nornir.core.inventory import Host
from nornir.core.task import MultiResult, Result, Task
from nornir_netmiko import netmiko_send_command
from nornir_utils.plugins.tasks.files import write_file

from nornir_network_backup.nornir.tasks.get_facts import task_get_facts
from nornir_network_backup.nornir.utils import (
    generate_comment,
    generate_filename,
    remove_file,
)

logger = logging.getLogger(__name__)

CONNECTION_NAME = "netmiko"


def task_backup_config(
    task: Task,
    user_config: dict,
    **kwargs,
    # config_backup_folder,
) -> Result:

    # print(f"host parameters: {task.host.dict()}")

    task_starttime = datetime.datetime.now()

    config_file = None
    config_diff_file = None

    # import sys
    # sys.exit()

    result = {
        "get_running_config": False,
        "save_running_config": False,
        "failed": False,
    }

    # print(summary_facts)

    cmd_running_config = task.host.extended_data().get("cmd_running_config")
    # print(f"show running config command = {cmd_running_config}")

    r = None
    summary_facts = dict()

    try:
        r = task.run(task=netmiko_send_command, command_string=cmd_running_config)
    except Exception:
        pass

    if r:

        if r.failed:
            result["failed"] = True

        if not r.failed:
            result["get_running_config"] = True

            # get all the facts
            if user_config["facts"]["enabled"]:
                fact_tasks_output = task.run(
                    task=task_get_facts,
                    user_config=user_config,
                )
                if not fact_tasks_output.failed:
                    summary_facts = get_summary_facts(
                        fact_tasks_output,
                        host=task.host,
                        wanted_summary_facts=user_config["facts"]["summary"],
                    )
                # print(fact_tasks_output.result)
            # else:
            #     summary_facts = dict()

        backup_config_file = generate_filename(
            filetype="backup",
            hostname=task.host,
            user_config=user_config,
        )

        r = task.run(
            task=write_file,
            filename=backup_config_file,
            content=generate_comment(summary_facts)
            + "\n"
            + r.result
            + "\n"
            + generate_comment("### END OF CONFIG ###", header=[""]),
        )

        if not r.failed:
            result["save_running_config"] = True
            config_file = backup_config_file

            # remove the .failed file if it should exist
            if Path(f"{config_file}.failed"):
                remove_file(f"{config_file}.failed")

            if user_config["backup_config"]["save_config_diff"]:
                diff_file = generate_filename(
                    filetype="diff",
                    hostname=task.host,
                    user_config=user_config,
                )
                if r.diff and diff_file:
                    config_diff_file = diff_file
                    task.run(
                        task=write_file,
                        filename=diff_file,
                        content=r.diff,
                    )

        if r.failed:
            result["failed"] = True

    task_endtime = datetime.datetime.now()
    task_duration = task_endtime - task_starttime

    # save the result to the inventory Host object
    task.host.data.setdefault("_backup_results", {}).setdefault("config", {})
    task.host.data["_backup_results"]["config"] = result
    task.host.data["_backup_results"]["starttime"] = task_starttime
    task.host.data["_backup_results"]["endtime"] = task_endtime
    task.host.data["_backup_results"]["duration"] = task_duration.total_seconds()
    task.host.data["_backup_results"]["config"]["backup_file"] = (
        Path(config_file).name if config_file else ""
    )
    task.host.data["_backup_results"]["config"]["diff_file"] = (
        config_diff_file if config_diff_file else ""
    )

    print(
        f"{task.host}: {'FAILED' if result['failed'] else 'SUCCESS'} in {task_duration.total_seconds()} seconds"
    )
    logger.info(
        f"{task.host}: {'FAILED' if result['failed'] else 'SUCCESS'} in {task_duration.total_seconds()} seconds"
    )

    return Result(host=task.host, result=result)


def get_summary_facts(
    results: MultiResult, host: Host, wanted_summary_facts: dict
) -> dict:
    """Get summary facts from all the previous 'show' results of all the tasks
    with name "fact_netmiko_send_command"

    We'll check the fact output results first, afterwards we'll check the host
    data fields (fact info has priority)

    "summary" facts are pre-defined keywords in the nornir configuration file and
    these will be added on top of the backup configuration file as comments. Only
    the facts that are found in the output fatcs commands will be displayed

    Example config backup file

        !
        ! ### START OF CONFIG ###
        !
        ! BOOT_VERSION: BOOT16-SEC-V3.4R3E40C
        ! DEVICE: LBB_140
        ! HOSTNAME: dops-lab-02
        ! MAC: 70:FC:8C:07:22:CC
        ! RELOAD_REASON: Power Fail detection
        ! SERIAL: T1703006230033175
        ! SOFTWARE: ONEOS16-MONO_FT-V5.2R2E7_HA8
        !
        Building configuration...

        Current configuration:

        !
        bind ssh Dialer 1
        bind ssh Loopback 1
        !

    """
    have_summary_facts = {}

    for r in results:
        if not r.name.startswith("fact_netmiko_send_command") or r.failed:
            continue

        for res in _extract_fact_from_result(r.result, wanted_summary_facts):
            # print(res)
            # print(type(res))
            if res:
                have_summary_facts[res[0]] = res[1]

        # print(r.result)
        # print(r.name)
        # print(type(r.result))
        # print(r.result)
        # print(f"failed: {r.failed}")

    # find missing wanted facts in the hosts.yaml file
    missing_wanted_facts = [
        key.lower()
        for key in wanted_summary_facts.keys()
        if key.upper() not in have_summary_facts.keys()
    ]
    # print(f"MISSING WANTED KEYS:{missing_wanted_facts}")

    for key in missing_wanted_facts:
        # print(f"KEY:{key}")
        if key in host.data:
            value = host.data[key]
            if not value:
                continue
            if type(value) is list:
                value = "|".join(value)
            have_summary_facts[key.upper()] = value

    # for key in host.data.keys():
    #     print(f"KEY:{key}")
    #     if key.upper() in missing_wanted_facts:
    #         have_summary_facts[key.upper()] = host.data[key]

    return have_summary_facts


def _extract_fact_from_result(result, wanted_summary_facts):
    """checks all the results to see if we should extract something for the summary facts"""
    if type(result) is list:
        for entry in result:
            for rc in _extract_fact_from_result(entry, wanted_summary_facts):
                yield rc

    if type(result) is dict:
        for key in wanted_summary_facts.keys():
            if key in result:
                value = result[key]
                if not value:
                    continue
                if type(value) is list:
                    value = "|".join(value)
                yield [key.upper(), value]
