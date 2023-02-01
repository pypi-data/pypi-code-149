import datetime
import logging
import sys

import click
import ruamel.yaml
from nornir import InitNornir
from nornir.core.filter import F
from nornir.core.inventory import Host
from nornir.core.plugins.inventory import (
    InventoryPluginRegister,
    TransformFunctionRegister,
)
from nornir_inspect import nornir_inspect

from nornir_network_backup.nornir.config import init_user_defined_config
from nornir_network_backup.nornir.plugins.inventory import (
    NMAPDiscoveryInventory,
)
from nornir_network_backup.nornir.plugins.inventory.transform_functions import (
    load_credentials,
)
from nornir_network_backup.nornir.report import print_results_csv
from nornir_network_backup.nornir.tasks.backup_config import task_backup_config
from nornir_network_backup.nornir.utils import rename_failed_hosts_backup_file

logger = logging.getLogger(__name__)

CONNECTION_NAME = "netmiko"


def add_host_to_inventory(
    hostname: str, ip: str, username: str, password: str, platform: str
):
    """adds a host to the inventory programatically"""
    if not platform:
        raise click.UsageError(
            "This host is not known in the database, you will have to provide the platform driver manually\n"
        )

    return Host(
        name=hostname,
        hostname=hostname,
        username=username,
        password=password,
        platform=platform,
    )


def _init_nornir(
    config_file: str,
    regenerate_hostsfile: bool,
    gather_facts: bool,
):
    """Initiates the nornir object without applying any filters

    backup_script = single | many
    """

    # register extra plugins
    InventoryPluginRegister.register(
        "NMAPDiscoveryInventory", NMAPDiscoveryInventory
    )
    TransformFunctionRegister.register("load_credentials", load_credentials)

    nornir_config = None

    with open(config_file, "r") as f:
        yml = ruamel.yaml.YAML(typ="safe")
        nornir_config = yml.load(f)

    if (
        regenerate_hostsfile is not None
        and nornir_config["inventory"]["plugin"] == "NMAPDiscoveryInventory"
    ):
        nornir_config["inventory"]["options"][
            "regenerate"
        ] = regenerate_hostsfile

    if gather_facts is not None:
        nornir_config["user_defined"]["facts"]["enabled"] = gather_facts

    nr = InitNornir(**nornir_config)

    return nr


def run_backup_process(nr, nr_unfiltered):

    backup_start_time = datetime.datetime.now()

    logger.info(
        f"--- START BACKUP PROCESS FOR {len(nr.inventory.hosts)} HOSTS ---"
    )
    print(
        "-" * 50
        + f"\n--- START BACKUP PROCESS FOR {len(nr.inventory.hosts)} HOSTS ---\n"
        + "-" * 50
    )

    result = nr.run(
        task=task_backup_config,
        user_config=nr.config.user_defined,
    )

    rename_failed_hosts_backup_file(
        result.failed_hosts, user_config=nr.config.user_defined
    )

    for failed_host in result.failed_hosts:
        print(f"{failed_host}: FAILED")
        logger.error(f"FAILED HOST: {failed_host}")

    # print(nornir_inspect(result))

    backup_end_time = datetime.datetime.now()

    backup_duration = backup_end_time - backup_start_time

    nbr_processed_hosts = len(result.items())
    nbr_failed_hosts = len(result.failed_hosts)
    nbr_success_hosts = nbr_processed_hosts - nbr_failed_hosts

    logger.info(
        f"--- {nbr_success_hosts} FINISHED IN {backup_duration.total_seconds()} SECONDS, {nbr_failed_hosts} FAILED ---"
    )
    print(
        "-" * 50
        + f"\n--- {nbr_success_hosts} FINISHED, {nbr_failed_hosts} FAILED IN {backup_duration.total_seconds()} SECONDS ---\n"
        + "-" * 50
    )

    # TODO: parameterize

    print_results_csv(
        nr.config.user_defined["backup_config"]["reports"]["summary"]["filename"],
        nr.config.user_defined["backup_config"]["reports"]["details"]["filename"],
        result,
        append_summary=nr.config.user_defined["backup_config"]["reports"]["summary"]["append"],
        append_details=nr.config.user_defined["backup_config"]["reports"]["details"]["append"],
        **dict(
            starttime=backup_start_time,
            stoptime=backup_end_time,
            total_host_cnt=len(nr.inventory.hosts),
            filtered_host_cnt=len(nr_unfiltered.inventory.hosts),
        ),
    )


def _apply_inventory_transformation(
    nr, username: str = None, password: str = None, platform: str = None
):

    transform_function = TransformFunctionRegister.get_plugin(
        "load_credentials"
    )
    for h in nr.inventory.hosts.values():
        transform_function(
            h,
            **(
                {
                    "username": username,
                    "password": password,
                    "platform": platform,
                }
                or {}
            ),
        )


def nr_backup(
    username: str,
    password: str,
    all_hosts: bool,
    host_list: list,
    group_list: list,
    regenerate_hostsfile: bool,
    gather_facts: bool,
    config_file: str = None,
    platform: str = None,
    verbose=None,
    dryrun=False,
):
    """Starts the backup process for many hosts based on nornir filtering:

    if all_hosts is True => use all hosts, regardless if host_list or group_list is defined
    """

    if dryrun:
        print(
            "dryrun mode is enabled - hosts.yaml file will not be re-generated"
        )
        regenerate_hostsfile = False

    nr = _init_nornir(
        config_file=config_file,
        regenerate_hostsfile=regenerate_hostsfile,
        gather_facts=gather_facts,
    )

    init_user_defined_config(nr)

    _filter = []

    for host in host_list:
        _filter.append(f"F(name__eq='{host}') | F(hostname__eq='{host}')")

    for group in group_list:
        _filter.append(f"F(groups__contains='{group}')")

    if _filter:
        nr_filtered = nr.filter(eval("|".join(_filter)))
    elif all_hosts:
        nr_filtered = nr.filter(~F(platform__eq=""))
    else:
        raise Exception("Please provide a nornir filter")

    # if there are any hosts that don't exist then we will add them
    # dynmically to the inventory but in that case the platform should
    # be added manually
    if host_list and not nr_filtered.inventory.hosts:
        for hostname in host_list:
            logger.info(
                f"-- host {hostname} was not found in the inventory, we will create an entry"
            )
            nr.inventory.hosts[hostname] = add_host_to_inventory(
                hostname, hostname, username, password, platform
            )
            nr.inventory.hosts[hostname].defaults = nr.inventory.defaults
            grp = nr.inventory.groups.get(platform)
            if grp:
                nr.inventory.hosts[hostname].groups.add(grp)

        nr_filtered = nr.filter(eval("|".join(_filter)))

    # add username + password + platform to each host
    _apply_inventory_transformation(
        nr_filtered, username=username, password=password, platform=platform
    )

    if not nr_filtered.inventory.hosts:
        raise click.UsageError("no hosts found to process - exit script\n")

    print(
        f"starting backup for {len(nr_filtered.inventory.hosts)} hosts: {[ str(h) for h in nr_filtered.inventory.hosts]}"
    )

    if dryrun:
        print("dryrun mode is enabled - backup will not be started")
        sys.exit()

    run_backup_process(nr_filtered, nr)
