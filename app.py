import streamlit as st
from PIL import Image
import pickle
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import tensorflow as tf
from keras.preprocessing import image
import os
from werkzeug.utils import secure_filename
st.set_option('deprecation.showfileUploaderEncoding', False)
from keras.models import load_model

html_temp = """
   <div class="" style="background-color:blue;" >
   <div class="clearfix">
   <div class="col-md-12">
   <center><p style="font-size:40px;color:white;margin-top:10px;">Poornima Institute of Engineering & Technology</p></center>
   <center><p style="font-size:30px;color:white;margin-top:10px;">Digital Image Processing lab by Rahul Kumar Agrawal</p></center>
   </div>
   </div>
   </div>
   """
st.markdown(html_temp,unsafe_allow_html=True)

st.title("""
        Various shades of RED color
         """
         )
file= st.file_uploader("Please upload image", type=("jpg", "png"))
R = st.slider('R', min_value=0, max_value=255, step=1)
# G = st.slider('G', min_value=0, max_value=255, step=1)
# B = st.slider('B', min_value=0, max_value=255, step=1)

import cv2
from  PIL import Image, ImageOps
def import_and_predict(image_data):
  #img = image.load_img(image_data, target_size=(224, 224))
  #image = image.img_to_array(img)
  #img_reshap= np.expand_dims(image, axis=0)
  #img_reshap = preprocess_input(img_reshap)

  image_data[:] = [R,0,0]
  st.image(image_data, use_column_width=True)
  return 0
if file is None:
  st.text("Please upload an Image file")
else:
  file_bytes = np.asarray(bytearray(file.read()), dtype=np.uint8)
  image = cv2.imdecode(file_bytes, 1)
  st.image(file,caption='Uploaded Image.', use_column_width=True)

if st.button("Change Color"):
  result=import_and_predict(image)

if st.button("About"):
  st.header("Developed by Sagar Gyanchandani-PIET18CS127")
  st.subheader("(RTU Final practical), Student, Department of Computer Engineering")
html_temp = """
   <div class="" style="background-color:black;" >
   <div class="clearfix">
   <div class="col-md-12">
   <center><p style="font-size:20px;color:white;margin-top:10px;">Digital Image processing RTU Final Practical</p></center>
   </div>
   </div>
   </div>
   """
st.markdown(html_temp,unsafe_allow_html=True)
