import typer
from .commands import install, enable, disable, scaffold

cli = typer.Typer()

cli.command()(install.install)
cli.command()(enable.enable)
cli.command()(disable.disable)
cli.command()(scaffold.scaffold)

if __name__ == "__main__":
    cli()
