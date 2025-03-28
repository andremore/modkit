import typer
from .commands import install, enable, disable, scaffold, validate, dev, list_modules, uninstall

cli = typer.Typer()

cli.command()(install.install)
cli.command()(enable.enable)
cli.command()(disable.disable)
cli.command()(scaffold.scaffold)
cli.command()(validate.validate)
cli.command()(dev.dev)
cli.command(name="list")(list_modules.list_modules)
cli.command()(uninstall.uninstall)

if __name__ == "__main__":
    cli()
