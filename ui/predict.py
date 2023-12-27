import os
import streamlit as st
from glob import glob


def render(column):
    st.markdown("<center><h1>Prediction Complete</h1></center>", unsafe_allow_html=True)


def predict_widget(data_path: str, backend: "Testing"):
    input_widget, output_widget = st.columns([0.25, 0.75])
    with input_widget:
        with st.container(border=True):
            st.markdown("### Data")
            data_object = st.file_uploader("Data File (CSV): ", key="predict_data")
            if data_object is not None:
                with open(os.path.join(data_path, "input", "input_data.csv"), "w") as f:
                    f.write(data_object.read())

            target_variable = st.selectbox(
                "Target Variable: ", ["GMV", "Retention"], key="predict_target"
            )

            with st.container(border=True):
                st.markdown("### Model")
                models = [
                    f.split(os.path.sep)[-1].strip(".pkl")
                    for f in glob(os.path.join(data_path, "..", "model", "*.pkl"))
                    if f.split(os.path.sep)[-1]
                    .lower()
                    .startswith(target_variable.lower())
                ]
                st.selectbox("Model Variables: ", options=models, key="predict_model")

                if st.button("Predict", key="Predict_button"):
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
                    backend.predict([config])
                    render(output_widget)
