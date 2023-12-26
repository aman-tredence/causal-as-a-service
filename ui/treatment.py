import os
from glob import glob
import streamlit as st


def render(output_widget):
    ...


def treatment_widget(data_path: str):
    input_widget, output_widget = st.columns([0.25, 0.75])
    with input_widget:
        data_file = st.file_uploader("Data: ")
        if data_file is not None:
            with open(os.path.join(data_path, "input", "input_data.csv"), "w") as f:
                f.write(data_file.read())

        target = st.selectbox(
            "Target Variable: ", ["GMV", "Retention"], key="treatment_target"
        )
        models = [
            f.split(os.path.sep)[-1].strip(".pkl")
            for f in glob(os.path.join(data_path, "..", "model", "*.pkl"))
            if f.split(os.path.sep)[-1].lower().startswith(target.lower())
        ]
        model_version = st.selectbox("Model Version: ", models)
        if st.button("Fetch Columns", key="treatment_fetch_columns"):
            with st.container(border=True):
                # TODO: Get columns
                st.selectbox("Select Columns: ", [])
                if st.button("Analyze", key="treatment_analyze"):
                    with st.container(border=True):
                        distribution = st.selectbox(
                            "Distribution: ",
                            ["Normal", "Poisson", "Lognormal"],
                        )
                        min_value = st.number_input("Min Value: ")
                        max_value = st.number_input("Max Value: ", min_value=min_value)
                        mean = st.number_input("Mean: ")
                        if distribution in ["Normal", "Lognormal"]:
                            std_dev = st.number_input("Std Dev: ")
                        if st.button("Predict", key="treatment_predict"):
                            render(output_widget)
