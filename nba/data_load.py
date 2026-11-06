
from pathlib import Path

import pandas as pd

from nba.config import load_config


def load_csv(data_path: Path) -> pd.DataFrame:
    return pd.read_csv(data_path)


if __name__ == "__main__":
    project_root = Path(__file__).resolve().parent.parent

    config_path = project_root / "config.yaml"
    config = load_config(config_path)

    data_path = project_root / config.data.data_path

    df = load_csv(data_path)
    print(data_path)
