
from . import cli, __app_name__

def main():
    # ensures the correct app name when running the --help option
    cli.app(prog_name=__app_name__)

if __name__ == "__main__":
    main()
