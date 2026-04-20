"""dragonfly-trace commands which will be added to the dragonfly cli"""
import click
from dragonfly.cli import main


@click.group(help='dragonfly trace commands.')
@click.version_option()
def trace():
    pass


# add sub-commands to trace

# add trace sub-commands
main.add_command(trace)
