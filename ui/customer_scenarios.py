import os
from glob import glob
import streamlit as st


def render():
    st.write("Done")


def customer_widget(data_path: str, backend: "CustomerScenarios"):
    input_widget, output_widget = st.columns([0.25, 0.75])
    with input_widget:
        data_file = st.file_uploader("Data (CSV): ", key="customer_data_file")
        target = st.selectbox(
            "Target Variable: ", ["GMV", "Retention"], key="customer_target"
        )

        models = [
            f.split(os.path.sep)[-1].strip(".pkl")
            for f in glob(os.path.join(data_path, "..", "model", "*.pkl"))
            if f.split(os.path.sep)[-1].lower().startswith(target.lower())
        ]
        model_version = st.selectbox("Model Version: ", models, key="customer_model")
        st.button(
            "Analyze",
            key="customer_analyze",
            on_click=lambda: st.session_state.update({"customer_analyze_active": True}),
        )
        if "customer_analyze_active" not in st.session_state:
            st.session_state["customer_analyze_active"] = False
        if st.session_state["customer_analyze_active"]:
            # TODO: Get columns
            for col in ...:
                with st.container(border=True):
                    distribution = st.selectbox(
                        "Distribution: ",
                        ["Normal", "Uniform", "Poisson", "Lognormal"],
                    )
                    min_value = st.number_input("Min Value: ")
                    max_value = st.number_input("Max Value: ", min_value=min_value)
                    mean = st.number_input("Mean: ")
                    if distribution in ["Normal", "Lognormal"]:
                        std_dev = st.number_input("Std Dev: ")
            if st.button("Run"):
                with output_widget:
                    render()
