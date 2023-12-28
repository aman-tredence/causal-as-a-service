import pathlib
from scripts import Testing


data_path = pathlib.Path(__file__).parent.joinpath("data")

target_variable = "GMV_cur"

# Run Backend
config = {
    "data": {
        "target": target_variable,
        "data_path": data_path.joinpath("input"),
        "data_output_path": data_path.joinpath("output"),
        "model_output_path": data_path.joinpath("..", "model"),
    },
    "model": {"version": 1},
    "analyse": True,
    }

test = Testing(data_path)

test.predict([config])