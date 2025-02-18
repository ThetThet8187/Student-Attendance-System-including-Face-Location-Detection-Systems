import streamlit as st
import cv2
import numpy as np
import face_recognition
import geopy
from geopy.geocoders import Nominatim

# Initialize geolocation
geolocator = Nominatim(user_agent="geoapiExercises")

st.title("Student Attendance System")

# Function to get location
def get_location():
    location = geolocator.geocode("Your City")  # Replace with dynamic IP-based geolocation if needed
    return location.address if location else "Location not found"

# Face Recognition Function
def recognize_face():
    st.write("Starting Face Recognition...")
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(rgb_frame)

        for face in face_locations:
            top, right, bottom, left = face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

        cv2.imshow("Face Recognition", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

# UI Buttons
if st.button("Start Face Recognition"):
    recognize_face()

if st.button("Get Location"):
    st.write("Current Location:", get_location())
