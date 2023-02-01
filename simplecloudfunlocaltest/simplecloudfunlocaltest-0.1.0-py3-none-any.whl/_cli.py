import click
from simplecloudfunlocaltest import simplefunctions

@click.command()
@click.option("--target", envvar="FUNCTION_TARGET", type=click.STRING, required=True)
@click.option("--host", envvar="HOST", type=click.STRING, default="0.0.0.0")
@click.option("--port", envvar="PORT", type=click.INT, default=8080)
@click.option("--debug", envvar="DEBUG", is_flag=True)
def _cli(target, host, port, debug):
    simplefunctions.create_app(target,host,port,debug)

