import os

import typer

app = typer.Typer()


@app.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    """
    Files (not directories) are listed when no command is entered.
    """
    if ctx.invoked_subcommand is None:
        files = [f for f in os.listdir('.') if os.path.isfile(f)]
        files.sort()
        for f in files:
            typer.echo(f)


@app.command('cd')
def change_directory(fd: str = typer.Option("", help='show files and directories'),
                     fx: str = typer.Option("", help='show files with details.'),
                     do: str = typer.Option("", help='show only directories.')):
    """
    Change directory and show files (see cd --help for options).
    """
    # see https://www.geeksforgeeks.org/tree-command-unixlinux/
    # https://www.geeksforgeeks.org/egrep-command-in-linux-with-examples/ and
    # https://www.gnu.org/software/coreutils/manual/html_node/Directory-listing.html#Directory-listing for reference.

    os.chdir(typer.prompt('enter path to target directory: '))
    if fd:
        typer.echo(os.system('ls --color=auto --group-directories-first'))
    elif fx:
        typer.echo(os.system('ls -p -lh --color=auto | egrep -v /$'))
    elif do:
        typer.echo(os.system('tree -diC -L 1'))
    else:
        typer.echo(os.system('ls -p --format=vertical --color=auto --| egrep -v /$'))

