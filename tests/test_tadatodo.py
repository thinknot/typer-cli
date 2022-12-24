from typer.testing import CliRunner


from tadatodo import __app_name__, __version__, cli

# Typer’s CliRunner is a subclass of Click’s CliRunner.
runner = CliRunner()


def test_version():
    # calls .invoke() on runner to run the application with the --version option. 
    result = runner.invoke(cli.app, ["--version"])

    # a Result object, which holds the result of running the CLI application with
    # the target arguments and options. Result objects provide several useful
    # attributes and properties, including the application’s exit code and standard output. 
    assert result.exit_code == 0

    assert f"{__app_name__} v{__version__}\n" in result.stdout
