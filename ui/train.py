import os
import streamlit as st


def render():
    ...


def update_json(
    file: str,
    lower: float,
    upper: float,
    est_method: str,
    ref_method: str,
    save_model: bool,
    target_var: str,
):
    ...


def train_widget(data_path: str):
    input_widget, output_widget = st.columns([0.25, 0.75])
    with input_widget:
        with st.container(border=True):
            st.markdown("### Data")

            data_object = st.file_uploader("Data File (CSV): ")
            if data_object is not None:
                with open(os.path.join(data_path, "input", "input_data.csv"), "w") as f:
                    f.write(data_object.read())

            target_variable = st.selectbox("Target Variable: ", ["GMV", "Retention"])

            dag_file = st.file_uploader("DAG File: ")
            if dag_file is not None:
                with open(os.path.join(data_path, "input", "dag.txt"), "w") as f:
                    f.write(dag_file.read())

        with st.container(border=True):
            st.markdown("### Sampling")

            lower_cap = st.number_input("Target Lower Cap: ")
            upper_cap = st.number_input("Target Upper Cap: ", min_value=lower_cap)

        with st.container(border=True):
            st.markdown("### Methods")
            estimation_method = st.selectbox(
                "Estimation Method: ",
                ["backdoor.linear_regression", "backdoor.generalized_linear_model"],
            )
            refutation_method = st.selectbox(
                "Refutation Method: ",
                ["data_subset_refuter", "random_common_cause", "None"],
                value="None",
            )

            save = st.toggle("Save Model", value=True)

        if st.button("Train"):
            print("Train")
