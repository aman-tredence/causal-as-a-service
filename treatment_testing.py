import os
from scripts import TreatmentScenarios
import pandas as pd
import json

data_dir = os.getcwd()
data_dir = data_dir.split("\\")
data_dir = "/".join(data_dir)

test_path = os.path.join(data_dir, "data/input/treatment_config.json")

with open(os.path.join(data_dir, "data/input/treatment_config.json"), 'r') as f:
    config = json.load(f)

trt_obj = TreatmentScenarios(data_dir)

results = trt_obj.scenario_creation([config], fetch_columns = True)

print(results)

print()

print("Predictions", end="\n")

results = trt_obj.scenario_creation([config], fetch_columns = False)

print(results)
