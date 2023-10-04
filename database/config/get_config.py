from typing import Dict
import yaml


def get_config(config_file_path: str) -> Dict[str, str]:
    try:
        with open(config_file_path, 'r') as config_file:
            config = yaml.safe_load(config_file)

        database_config = config.get('database', {})
        db_host = database_config.get('host', '')
        db_port = str(database_config.get('port', ''))
        db_name = database_config.get('name', '')
        db_user = database_config.get('user', '')
        db_password = database_config.get('password', '')

        return {
            "host": db_host,
            "port": db_port,
            "dbname": db_name,
            "user": db_user,
            "password": db_password,
        }
    except (FileNotFoundError, yaml.YAMLError) as e:
        raise RuntimeError(f"Error loading configuration: {e}")