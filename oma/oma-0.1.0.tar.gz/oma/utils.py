def get_formatted_size(num, suffix="B"):
    for unit in ["", "Ki", "Mi", "Gi", "Ti", "Pi", "Ei", "Zi"]:
        if abs(num) < 1024.0:
            return f"{num:3.1f}{unit}{suffix}"
        num /= 1024.0
    return f"{num:.1f}Yi{suffix}"


def get_total_storage_size(devices: list, storage_type: str):
    return get_formatted_size(
        sum([device["size"] for device in devices if device["type"] == storage_type])
    )


def get_storage_brand(devices: list, storage_type: str):
    return list(
        set([device["brand"] for device in devices if device["type"] == storage_type])
    )[0]


def get_readable_uptime(timestamp: str):
    days = timestamp // 86400
    hours = timestamp // 3600 % 24
    minutes = timestamp // 60 % 60
    seconds = timestamp % 60

    return f"{int(round(days, 0))} days, {int(round(hours, 0))} hours, {int(round(minutes, 0))} minutes and {int(round(seconds, 0))} seconds"


def get_cpu_load(items: list):
    return f'{int(round(sum([item["load"] for item in items])/len(items), 0))}%'


def get_cpu_temp(items: list):
    return f'{int(round(sum([item["temp"] for item in items])/len(items), 0))}℃'


def get_config():
    conf_exists = os.path.isfile(os.path.join(os.getenv("HOME"), ".oma_conf"))
    if not conf_exists:
        print("Please run configure, before you run this command")
        typer.Exit(1)
    else:
        with open(os.path.join(os.getenv("HOME"), ".oma_conf"), "r") as conf:
            for line in conf.readlines():
                key, value = line.split("=")
                dash_dot_url = value if key == "dash_dot_url" else None