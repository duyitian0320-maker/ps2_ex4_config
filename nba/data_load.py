import pandas as pd
from pathlib import Path


def load_csv(data_path: Path) -> pd.DataFrame:
    return pd.read_csv(data_path)


if __name__ == "__main__":
    # TODO: avoid hardcoding this data path using the pathlib library
    project_root = Path(__file__).resolve().parent.parent
    data_path = project_root / "data" / "game.csv"

    df = load_csv(data_path)
    print(data_path)
