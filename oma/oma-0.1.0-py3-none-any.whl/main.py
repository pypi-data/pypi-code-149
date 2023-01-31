import typer

from oma import hl

app = typer.Typer(add_completion=False)
app.add_typer(hl.app, name="hl", help="Home Lab commands")
