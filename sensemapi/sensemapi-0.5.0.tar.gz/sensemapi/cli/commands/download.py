# system modules
import logging
import time
import sys

# internal modules
import sensemapi
from sensemapi.client import SenseMapClient
from sensemapi.errors import SenseMapiError
from sensemapi.cli.commands.main import cli

# external modules
import pandas as pd
import click
from rich.progress import Progress
from rich.syntax import Syntax
from rich.panel import Panel

logger = logging.getLogger(__name__)


def datetime_value(x):
    try:
        if dt := pd.to_datetime(x):
            return dt.to_pydatetime()
    except Exception as e:
        logger.error(f"Can't parse {x!r} as date, ignoring")


@cli.command(
    # Due to a bug in click (https://github.com/pallets/click/issues/1253)
    # if we want to use the automatic environment variable feature AND a
    # command name that consists of two words, we cannot use a dash to separate
    # them but must use an underscore.
    name="download",
    help="Download data from a senseBox sensor",
)
@click.option(
    "--sensebox",
    "sensebox_id",
    help="senseBox ID",
    required=True,
)
@click.option(
    "--sensor",
    "sensor_ids",
    help="sensor ID",
    multiple=True,
)
@click.option(
    "--from",
    "from_time",
    help="interval start time to retrieve data",
    type=datetime_value,
)
@click.option(
    "--to",
    "to_time",
    help="interval end time to retrieve data",
    type=datetime_value,
)
@click.option(
    "-o",
    "--output",
    help="output file",
    type=click.File("w"),
    default=sys.stdout,
)
@click.pass_context
def download(
    ctx,
    sensebox_id,
    sensor_ids,
    from_time,
    to_time,
    output,
):
    client = SenseMapClient()
    box = client.get_box(id=sensebox_id)
    if logger.getEffectiveLevel() < logging.DEBUG:
        logger.debug(f"box =\n{box}")
    if not sensor_ids:
        logger.info(
            f"No --sensor specified, using all {len(box.sensors)} "
            f"sensors of senseBox {box.name!r} ({box.id})"
        )
        sensor_ids = list(box.sensors.by_id)
    logger.info(
        f"Downloading data from {len(sensor_ids)} sensors "
        f"{list(box.sensors.by_title)} "
        f"of senseBox {box.name!r} ({box.id}) sensors"
    )
    data = []
    with Progress(
        console=ctx.obj.get("console"),
        disable=logger.getEffectiveLevel() > logging.ERROR,
    ) as progress:
        task_sensors = progress.add_task("📥 Downloading sensor data")
        logger.debug(f"{from_time = }, {to_time = }")
        for sensor_id in progress.track(sensor_ids, task_id=task_sensors):
            if not (sensor := box.sensors.by_id.get(sensor_id)):
                logger.error(
                    msg := f"Box {box.name!r} ({box.id}) "
                    f"doesn't have a sensor with id {sensor_id}. Skipping."
                )
                continue
            if logger.getEffectiveLevel() < logging.DEBUG:
                logger.debug(f"sensor =\n{sensor}")
            fmt = "%Y-%m-%dT%H:%M:%S%z"
            txt = ""
            if not (from_time or to_time):
                pass
            elif from_time and to_time:
                txt = (
                    f"between {from_time.strftime(fmt)!r} "
                    f"and {to_time.strftime(fmt)!r}"
                )
            elif from_time:
                txt = f"starting {from_time.strftime(fmt)!r}"
            elif to_time:
                txt = f"starting {to_time.strftime(fmt)!r}"

            logger.info(
                f"Downloading measurements "
                f"of sensor {sensor.title!r} ({sensor.id}) {txt}"
            )
            measurements = sensor.get_measurements(
                from_date=from_time,
                to_date=to_time,
            )
            if logger.getEffectiveLevel() < logging.DEBUG:
                logger.debug(f"measurements:\n{measurements}")
            logger.debug(
                f"Converting {max(map(len,measurements.data.values()))} "
                f"measurements of sensor {sensor.title!r} ({sensor.id}) "
                f"to pandas series..."
            )
            series = measurements.series
            data.append(series)
    if not data:
        logger.error(
            f"🤷 No data to save to {outout.name!r}, see previous errors."
        )
        ctx.exit(1)
    elif len(data) == 1:
        df = data[0].to_frame()
    else:
        logger.info(f"🔄 Merging {len(data)} sensor measurement datasets")
        df = pd.concat([s.to_frame() for s in data], axis="columns")
    logger.info(f"↕️  Sorting index")
    df.sort_index(inplace=True)
    if len(df.index) <= 0:
        logger.warning(
            f"Apparently there is no data in your selected time range. "
            f"Saving header anyway..."
        )
    logger.info(f"📥 Saving {len(df.index)} CSV lines to {output.name!r}")
    df.to_csv(output)
    if (
        logger.getEffectiveLevel() <= logging.INFO
        and output is not sys.stdout
        and len(df.index) > 0
    ):
        ctx.obj["console"].print(
            Panel(
                Syntax(
                    df.head(10).to_csv().strip() + "\n..."
                    if len(df.index) > 10
                    else "",
                    "haskell",  # there's no 'csv' lexer...
                    line_numbers=True,
                    word_wrap=True,
                    padding=1,
                ),
                title=f"📎 CSV data excerpt written to {output.name!r}",
            )
        )
        ctx.obj["console"].print(
            Panel(
                Syntax(
                    f"""
# You can read this data e.g. with:
import pandas as pd
# first column is the time
pd.read_csv({output.name!r},index_col=0,parse_dates=[0])
                    """.strip(),
                    "python",
                    line_numbers=True,
                    dedent=True,
                    padding=1,
                ),
                title=f"📤 Reading {output.name!r} with 🐍 Python and 🐼 pandas",
            )
        )


if __name__ == "__main__":
    download()
