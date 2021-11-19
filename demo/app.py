import os
from os.path import join

import streamlit as st
import markdowns

import pandas as pd
import numpy as np

ROOT_DIR = "images"

img_data = [
    join(ROOT_DIR, "select_images/bus.jpg"),
    join(ROOT_DIR, "select_images/couch.jpg"),
    join(ROOT_DIR, "select_images/fruits.jpg"),
    join(ROOT_DIR, "select_images/sheep.jpg"),
    join(ROOT_DIR, "select_images/tennis.jpg"),
    join(ROOT_DIR, "select_images/umbrella.jpg")
]

imgs = [open(i, 'rb').read() for i in img_data]

loaded_images = {
    "Bus": imgs[0],
    "Couch": imgs[1],
    "Fruits": imgs[2],
    "Sheep": imgs[3],
    "Tennis": imgs[4],
    "Umbrella": imgs[5],
}

show_rec = False

def main():
    st.set_page_config(page_title="2163 - Any Shot Learning",
                        page_icon="images/cv_lab.png",
                        layout="wide",
                        initial_sidebar_state='expanded')

    st.sidebar.header('2163 - Any Shot Learning')
    selected_demo = st.sidebar.selectbox('Select a Demo', np.array(["test1", "test2"]))
    st.title('In progress UniT demo')
    
    # background on image level vs instance level annotation
    # wouldn't it be nice to be able to transfer knowledge from base classes to novel!
    st.markdown(markdowns.motivation_title, unsafe_allow_html=True)
    with st.beta_expander("See more"):
        st.markdown(markdowns.motivation_string, unsafe_allow_html=True)
        bcol1, bcol2, bcol3 = st.beta_columns([1, 1, 1])
        bcol2.image("images/image_vs_instance.png", width=550)

    # intro to UBC computer vision lab


    # theory on UniT paper
    st.markdown(markdowns.unit_title, unsafe_allow_html=True)
    with st.beta_expander("See more"):
        st.markdown(markdowns.unit_string, unsafe_allow_html=True)
        bcol1, bcol2, bcol3 = st.beta_columns([1, 1, 1])
        bcol2.image("images/unit.png", width=550)

    # about the dataset(s)
    # what kind of annotations there are 
    st.markdown(markdowns.dataset_title, unsafe_allow_html=True)
    with st.beta_expander("See more"):
        st.markdown(markdowns.dataset, unsafe_allow_html=True)

    # dataset in context of paper - base vs novel? which classes?


    # select image of provided images
    st.markdown(markdowns.object_selection_header, unsafe_allow_html=True)
    radio_selection_col, image_selection_col, col3 = st.beta_columns([2, 1, 1])
    with radio_selection_col:
        st.write(markdowns.radio_selection_styles, unsafe_allow_html=True)
        selected_image = st.radio("", list(loaded_images.keys()))

    with image_selection_col:
        st.image(loaded_images[selected_image],
                 caption='Selected Object',
                 width=350)
    # OR
    # upload your own
    st.markdown(markdowns.upload_file_header, unsafe_allow_html=True)
    uploaded_files = st.file_uploader("Choose a file", accept_multiple_files=True)
    for uploaded_file in uploaded_files:
        bytes_data = uploaded_file.read()
        st.image(bytes_data,
                 caption=uploaded_file.name,
                 width=350)

    # select a model
    model_options = ("None", "Pre-trained A", "Pre-trained B")
    st.write(markdowns.selectbox_styles, unsafe_allow_html=True)
    selected_model = st.selectbox("Select a model", model_options)

    if len(selected_model) == 0 or selected_model == "None":
        return
        # background on model

    # RUN!
    col1, col2, col3 = st.beta_columns([1, 1, 1])
    st.markdown(markdowns.run_model_button, unsafe_allow_html=True)
    global show_rec
    if col2.button("Run Model"):
        show_rec = True

    # results
    if show_rec:
        st.write("reconstruction")

    threshold = st.slider("Threshold Value",
                          min_value=-0.3,
                          max_value=0.3,
                          value=0.0,
                          step=0.001)
    if threshold:
        st.write("show threshold diff")


if __name__ == "__main__":
    main()