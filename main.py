import pathlib
import streamlit as st

from ui import train_widget, predict_widget, treatment_widget, customer_widget

# from scripts import Training, Testing


st.set_page_config(layout="wide")

DATA_PATH = pathlib.Path(__file__).parent.joinpath("data")
print(DATA_PATH)

DATA_PATH.joinpath("input").mkdir(exist_ok=True)
DATA_PATH.joinpath("output").mkdir(exist_ok=True)


def main():
    train, predict, treatment, customer = st.tabs(
        ["Train", "Predict", "Treatment Scenarios", "Customer Scenarios"]
    )

    # backend = {
    #     "train": Training(DATA_PATH),
    #     "predict": Testing(DATA_PATH),
    # }

    with train:
        train_widget(DATA_PATH)

    with predict:
        predict_widget(DATA_PATH)

    with treatment:
        treatment_widget(DATA_PATH)

    with customer:
        customer_widget(DATA_PATH)


main()
