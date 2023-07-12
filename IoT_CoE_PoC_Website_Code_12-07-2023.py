import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import numpy as np
import cv2
from datetime import datetime

import time

st.set_page_config(page_title="IoT CoE Track 'N' Trace",page_icon=":tada:",layout="wide")

with st.container():
 #st.subheader("Track and Trace Application")
 st.title("IoT CoE Track 'N' Trace")

 with  st.sidebar:
  selected =option_menu(
         menu_title="Assembly Line",
         options=("Material Handling Station","Pinning and Press Station","Drilling Station"),
  )

if selected == "Material Handling Station":
     st.title(f"you have selected {selected}")
     vid = cv2.VideoCapture(0)

     detector = cv2.QRCodeDetector()

     while True:

         # Capture the video frame by frame
         Ret, frame = vid.read()

         data, bbox, straight_qrcode = detector.detectAndDecode(frame)
         if len(data) > 0:
             st.write(data)
             time.sleep(2)
             # Display the resulting frame
         cv2.imshow('frame', frame)

         # cv2.imshow('frame2',frame)

         # the 'q' button is set as the
         # quitting button you may use any
         # desired button of your choice
         if cv2.waitKey(1) & 0xFF == ord('q'):
             break

     # After the loop release the cap object
     vid.release()
     # Destroy all the windows
     cv2.destroyAllWindows()

if selected == "Pinning and Press Station":
  st.title(f"you have selected {selected}")


if selected == "Drilling Station":
 st.title(f"you have selected {selected}")
