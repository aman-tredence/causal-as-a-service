import os
import streamlit as st

from ui import train_widget, predict_widget


st.set_page_config(layout="wide")

# DATA_PATH = os.path.join(os.path.pardir(__file__), "data")


def main():
    train, predict, treatment, customer = st.tabs(
        ["Train", "Predict", "Treatment Scenarios", "Customer Scenarios"]
    )

    with train:
        train_widget()

    with predict:
        predict_widget()

    # with treatment:
    #     treatment_widget()

    # with customer:
    #     customer_widget()


main()
