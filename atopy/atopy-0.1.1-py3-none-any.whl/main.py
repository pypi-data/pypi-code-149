import typer
from loguru import logger

from atopy.datetime import nstime as _nstime
from atopy.datetime import timezone, utc_astimezone, utc_now

app = typer.Typer()


@app.command()
def now(tz: str = "UTC") -> None:
    dt = utc_astimezone(utc_now(), timezone(tz))
    logger.info(f"now: {dt}")


@app.command()
def nstime() -> None:
    n = _nstime()
    logger.info(f"nstime: {n}")


if __name__ == "__main__":
    app()
