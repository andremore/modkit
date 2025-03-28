import typer
from .commands import install, enable, disable, scaffold, validate, dev

cli = typer.Typer()

cli.command()(install.install)
cli.command()(enable.enable)
cli.command()(disable.disable)
cli.command()(scaffold.scaffold)
cli.command()(validate.validate)
cli.command()(dev.dev)

if __name__ == "__main__":
    cli()
