# https://docs.python.org/3/library/configparser.html#configparser.ConfigParser
import configparser
# https://docs.python.org/3/library/pathlib.html#pathlib.Path
from pathlib import Path


import typer


from . import (

    DB_WRITE_ERROR, DIR_ERROR, FILE_ERROR, SUCCESS, __app_name__

)

# cross-platform way to handle system paths.
CONFIG_DIR_PATH = Path(typer.get_app_dir(__app_name__))
# path to a directory where you can store configurations.
CONFIG_FILE_PATH = CONFIG_DIR_PATH / "config.ini"

#  initializes the application’s configuration file and database.
def init_app(db_path: str) -> int:

    """Initialize the application."""

    config_code = _init_config_file()

    if config_code != SUCCESS:

        return config_code

    database_code = _create_database(db_path)

    if database_code != SUCCESS:

        return database_code

    return SUCCESS


def _init_config_file() -> int:

    try:

        CONFIG_DIR_PATH.mkdir(exist_ok=True)

    except OSError:

        return DIR_ERROR

    try:

        CONFIG_FILE_PATH.touch(exist_ok=True)

    except OSError:

        return FILE_ERROR

    return SUCCESS


def _create_database(db_path: str) -> int:
    #  handle config files with a structure similar to INI files.
    config_parser = configparser.ConfigParser()

    config_parser["General"] = {"database": db_path}

    try:

        with CONFIG_FILE_PATH.open("w") as file:

            config_parser.write(file)

    except OSError:

        return DB_WRITE_ERROR

    return SUCCESS