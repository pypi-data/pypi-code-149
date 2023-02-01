import logging

from nornir.core.inventory import Host
from nornir.core.task import MultiResult, Result, Task
from nornir_netmiko import netmiko_send_command
from nornir_utils.plugins.tasks.files import write_file
from ntc_templates.parse import parse_output

from nornir_network_backup.nornir.utils import (
    fact_to_yml,
    generate_comment,
    generate_filename,
    remove_file,
    rename_file,
    touch_file,
)

logger = logging.getLogger(__name__)

CONNECTION_NAME = "netmiko"


def get_fact_commands(host: Host) -> list:
    """return a list of all the facts commands found hierarchically in host and all groups
    The default recursive behavior in Nornir will stop at the first match
    """
    fact_commands = [cmd for cmd in host.extended_data().get("cmd_facts", [])]

    for grp in host.groups:
        fact_commands += [cmd for cmd in grp.extended_data().get("cmd_facts", [])]

    return list(set(fact_commands))


def task_get_facts(task: Task, user_config: dict, **kwargs) -> Result:
    commands = get_fact_commands(task.host)

    facts = {
        "all_commands": [],
        "failed_commands": [],
        "success_commands": [],
        "failed": False,
    }

    for cmd in commands:
        cmd_nice = cmd.replace(" ", "_").replace("|", "_")
        facts["all_commands"].append(cmd)

        output = task.run(
            name=f"fact_netmiko_send_command_{cmd_nice}",
            task=netmiko_send_command,
            command_string=cmd,
            # use_textfsm=user_config["textfsm"]["enabled"],
            # severity_level=logging.DEBUG,
        )

        if output.failed:
            facts["failed_commands"].append(cmd)

        else:
            facts["success_commands"].append(cmd)

            use_textfsm = user_config["textfsm"]["enabled"]

            _content = output.result
            if use_textfsm:
                try:
                    __content = parse_output(
                        platform=task.host.platform, command=cmd, data=_content
                    )
                    _content = __content
                except Exception:
                    logger.error(
                        f"unable to parse textfsm for host:{task.host.name} platform:{task.host.platform} command:{cmd}"
                    )
                    pass

            # >>> vlan_parsed = parse_output(platform="cisco_ios", command="show vlan", data=vlan_output)

            content, extension = fact_to_yml(_content)

            fact_file = generate_filename(
                filetype="fact",
                hostname=task.host,
                user_config=user_config,
                command=cmd,
                extension=extension,
                remove_txt=True,
            )

            if not output.result:
                remove_file(fact_file)
                continue

            task.run(
                task=write_file,
                filename=fact_file,
                content=f"{content}",
            )

    # save the result to the inventory Host object
    # facts = {"all_commands": [], "failed_commands": [], "success_commands": []}
    facts["total_commands"] = len(facts["all_commands"])
    facts["total_failed_commands"] = len(facts["failed_commands"])
    facts["total_success_commands"] = len(facts["success_commands"])
    facts["failed"] = True if facts["failed_commands"] else False

    task.host.data.setdefault("_backup_results", {}).setdefault("facts", facts)

    return Result(host=task.host, result=facts)
    # return Result(host=task.host, result=facts, failed=failed)
