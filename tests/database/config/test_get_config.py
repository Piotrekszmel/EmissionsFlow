import os
import pytest
from database.config.get_config import get_config

@pytest.fixture
def valid_config_file_path():
    return os.path.join(os.path.dirname(__file__), "valid_db_config.yaml")

@pytest.fixture
def invalid_config_file_path():
    return os.path.join(os.path.dirname(__file__), "invalid_db_config.yaml")

def test_get_config_valid(valid_config_file_path):
    config = get_config(valid_config_file_path)
    assert config["host"] == "0.0.0.0"
    assert config["port"] == "5432"
    assert config["dbname"] == "postgres"
    assert config["user"] == "postgres"
    assert config["password"] == "postgres"

def test_get_config_file_not_found():
    with pytest.raises(RuntimeError) as excinfo:
        get_config("non_existent_config.yaml")
    assert "Error loading configuration" in str(excinfo.value)

def test_get_config_invalid_yaml(invalid_config_file_path):
    with pytest.raises(ValueError) as e:
            get_config(invalid_config_file_path)
    assert "The YAML content should represent a dictionary." in str(e.value)
