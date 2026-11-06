# TODO: define your data classes here

from pydantic import BaseModel


class DataConfig(BaseModel):
    table: str
    data_path: str
    features_columns: list[str]


class ModelConfig(BaseModel):
    name: str
    type: str
    params: dict[str, int]


class Config(BaseModel):
    data: DataConfig
    model: ModelConfig
