# TODO: read in your yaml file and parse it using the data classes defined in dataclasses.py

from pathlib import Path

import yaml

from nba.dataclasses import Config


def load_config(config_path: Path) -> Config:
    with config_path.open("r") as file:
        config_dict = yaml.safe_load(file)

    return Config.model_validate(config_dict)


if __name__ == "__main__":
    project_root = Path(__file__).resolve().parent.parent
    config_path = project_root / "config.yaml"

    config = load_config(config_path)
    print(config)
