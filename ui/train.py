import streamlit as st


def render():
    ...


def train_widget():
    input_widget, output_widget = st.columns([0.25, 0.75])
    with input_widget:
        with st.container(border=True):
            st.markdown("### Data")

            data_object = st.file_uploader("Data Path: ")

            # TODO: Target column names
            target_variable = st.selectbox("Target Variable: ", [])

            dag_path = st.file_uploader("DAG Path: ")

        with st.container(border=True):
            st.markdown("### Sampling")

            lower_cap = st.number_input("Target Lower Cap: ")
            upper_cap = st.number_input("Target Upper Cap: ", min_value=lower_cap)

        with st.container(border=True):
            st.markdown("### Methods")
            # TODO: Add methods
            estimation_method = st.selectbox("Estimation Method: ", [])
            refutation_method = st.selectbox("Refutation Method: ", [])

            save = st.toggle("Save Model", value=True)

        with st.button("Train"):
            ...
