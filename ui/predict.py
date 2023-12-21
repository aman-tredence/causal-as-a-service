import streamlit as st


def render(column):
    ...


def predict_widget():
    input_widget, output_widget = st.columns([0.25, 0.75])
    with input_widget:
        with st.container(border=True):
            st.markdown("Data")

            # TODO: Target column names
            target_variable = st.selectbox(
                "Target Variable: ", [], key="predict_target"
            )

            dag_path = st.file_uploader("DAG Path: ")

            if st.button("Fetch Models"):
                # TODO: Fetch Models
                with st.container(border=True):
                    st.markdown("### Model")
                    st.selectbox("Model Variables: ", [])

                    if st.button("Predict", key="Predict_button"):
                        render(output_widget)
