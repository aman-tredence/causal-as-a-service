import os
import json
from glob import glob
import streamlit as st


def render():
    st.write("Done")


def treatment_widget(data_path: str, backend: "TreatmentScenarios"):
    input_widget, output_widget = st.columns([0.25, 0.75])
    with input_widget:
        with st.container(border=True):
            data_file = st.file_uploader("Data: ")
            if data_file is not None:
                with open(os.path.join(data_path, "input", "input_data.csv"), "w") as f:
                    f.write(data_file.read())

            target = st.selectbox(
                "Target Variable: ", ["GMV_cur", "retention"], key="treatment_target"
            )
            models = [
                f.split(os.path.sep)[-1].strip(".pkl")
                for f in glob(os.path.join(data_path, "..", "model", "*.pkl"))
                if f.split(os.path.sep)[-1].lower().startswith(target.lower())
            ]
            model_version = st.selectbox("Model Version: ", models)
            st.button(
                "Fetch Columns",
                key="treatment_fetch_columns",
                on_click=lambda: st.session_state.update(
                    {"treatment_fetch_columns_active": True}
                ),
            )

        if "treatment_fetch_columns_active" not in st.session_state:
            st.session_state["treatment_fetch_columns_active"] = False
        if st.session_state["treatment_fetch_columns_active"]:
            with open(os.path.join(data_path, "input/treatment_config.json"), "r") as f:
                config = json.load(f)
                config["model"]["version"] = int(model_version.split("v")[-1])
            results = backend.scenario_creation([config], fetch_columns=True)
            with st.container(border=True):
                col_name = st.selectbox("Select Columns: ", results)
                st.button(
                    "Analyze",
                    key="treatment_analyze",
                    on_click=lambda: st.session_state.update(
                        {"treatment_analyze_active": True}
                    ),
                )

                if "treatment_analyze_active" not in st.session_state:
                    st.session_state["treatment_analyze_active"] = False
                if st.session_state["treatment_analyze_active"]:
                    # TODO draw distribution
                    with st.container(border=True):
                        distribution = st.selectbox(
                            "Distribution: ",
                            ["Normal", "Poisson", "Lognormal"],
                        )
                        min_value = st.number_input("Min Value: ")
                        max_value = st.number_input("Max Value: ", min_value=min_value)
                        mean = st.number_input("Mean: ")
                        std_dev = (
                            st.number_input("Std Dev: ")
                            if distribution in ["Normal", "Lognormal"]
                            else 1
                        )
                        if st.button("Predict", key="treatment_predict"):
                            config["data_change"] = {
                                "tweak_col": col_name,
                                "distribution": distribution,
                                "min_value": min_value,
                                "max_value": max_value,
                                "mean": mean,
                                "std_dev": std_dev,
                            }
                            with output_widget:
                                render()
