import os
from scripts import CustomerScenarios
import pandas as pd
import json

data_dir = os.getcwd()
data_dir = data_dir.split("\\")
data_dir = "/".join(data_dir)

with open(os.path.join(data_dir, "data/input/customer_config.json"), 'r') as f:
    config = json.load(f)


cust_obj = CustomerScenarios(data_dir)

results = cust_obj.scenario_creation([config], analyze=True)

# print(results)

first_customer = pd.DataFrame(results['predictions'])
coeffs = pd.DataFrame(results['coeffs'])
stats = pd.DataFrame(results['stats'])

with open(os.path.join(data_dir, "data/input/cust_new_data.json")) as f:
    new_data = json.load(f)
    
config["new_data"] = new_data

print("Predictions on new data")
results = cust_obj.scenario_creation([config],
                                     analyze = False)

