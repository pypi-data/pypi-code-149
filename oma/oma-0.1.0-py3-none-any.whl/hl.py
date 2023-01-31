import os

import requests
import typer
from rich import box, print
from rich.panel import Panel
from rich.table import Table

from oma import utils

app = typer.Typer()


@app.command()
def configure():
    """Configures the cli to work with your Home Lab"""
    dash_dot_url = typer.prompt("What is your Home Lab Dash Dot url?")
    with open(os.path.join(os.getenv("HOME"), ".oma_conf"), "w+") as conf:
        conf.write(
            f'dash_dot_url={dash_dot_url[:len(dash_dot_url)-1] if dash_dot_url[-1] == "/" else dash_dot_url}'
        )


@app.command()
def info():
    """Displays information about your Home Lab"""
    conf_exists = os.path.isfile(os.path.join(os.getenv("HOME"), ".oma_conf"))
    if not conf_exists:
        print("Please run configure, before you run this command")
        typer.Exit(1)
    else:
        with open(os.path.join(os.getenv("HOME"), ".oma_conf"), "r") as conf:
            for line in conf.readlines():
                key, value = line.split("=")
                dash_dot_url = value if key == "dash_dot_url" else None

        result_info = requests.get(f"{dash_dot_url}/info").json()
        result_cpu = requests.get(f"{dash_dot_url}/load/cpu").json()
        result_ram = requests.get(f"{dash_dot_url}/load/ram").json()
        result_storage = requests.get(f"{dash_dot_url}/load/storage").json()
        result_network = requests.get(f"{dash_dot_url}/load/network").json()

        table = Table(box=box.MINIMAL)

        table.add_column("Name", justify="left", style="medium_purple3")
        table.add_column("Usage", justify="left", style="khaki3")
        table.add_column("Info", justify="left", style="magenta")

        table.add_row(
            "Uptime",
            f'{utils.get_readable_uptime(result_info["os"]["uptime"])}',
            f'{result_info["os"]["distro"]} {result_info["os"]["arch"]} {result_info["os"]["kernel"]}',
        )
        table.add_row(
            "CPU",
            f"{utils.get_cpu_load(result_cpu)} @{utils.get_cpu_temp(result_cpu)}",
            f'{result_info["cpu"]["brand"]} {result_info["cpu"]["model"]}, {result_info["cpu"]["cores"]} cores, {result_info["cpu"]["threads"]} threads @{result_info["cpu"]["frequency"]}Ghz',
        )
        table.add_row(
            "RAM",
            f'{utils.get_formatted_size(result_ram["load"])}',
            f'{utils.get_formatted_size(result_info["ram"]["size"])} {result_info["ram"]["layout"][0]["brand"]} {result_info["ram"]["layout"][0]["type"]} @{(result_info["ram"]["layout"][0]["frequency"])}Mhz',
        )
        table.add_row(
            "Storage",
            f'{utils.get_formatted_size(result_storage["layout"][0]["load"])}',
            f'HD: {utils.get_total_storage_size(result_info["storage"]["layout"], "HD")} {utils.get_storage_brand(result_info["storage"]["layout"], "HD")}, SSD: {utils.get_total_storage_size(result_info["storage"]["layout"], "SSD")} {utils.get_storage_brand(result_info["storage"]["layout"], "SSD")}',
        )
        table.add_row(
            "Network",
            f'⬇ {utils.get_formatted_size(result_network["down"])} ⬆ {utils.get_formatted_size(result_network["up"])}',
            f'⬇ {utils.get_formatted_size(result_info["network"]["speedDown"])} ⬆ {utils.get_formatted_size(result_info["network"]["speedUp"])}',
        )

        print(
            Panel(
                table,
                title="Home Lab Info",
                border_style="green",
                box=box.DOUBLE,
                expand=False,
            )
        )

@app.command()
def show():
    """Opens your Home Lab's dash dot application"""
    conf_exists = os.path.isfile(os.path.join(os.getenv("HOME"), ".oma_conf"))
    if not conf_exists:
        print("Please run configure, before you run this command")
        typer.Exit(1)
    else:
        with open(os.path.join(os.getenv("HOME"), ".oma_conf"), "r") as conf:
            for line in conf.readlines():
                key, value = line.split("=")
                dash_dot_url = value if key == "dash_dot_url" else None

        if dash_dot_url:
            print(f"Opening {dash_dot_url}")
            cmd_status = typer.launch(dash_dot_url)