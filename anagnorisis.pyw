import cv2
import numpy as np
import glob
import os
import tkinter as tk
from tkinter import filedialog
import subprocess

def resize_image(image, width, height):
    h, w = image.shape[:2]
    aspect_ratio = w / h

    if aspect_ratio > width / height:
        new_w = width
        new_h = int(width / aspect_ratio)
    else:
        new_h = height
        new_w = int(height * aspect_ratio)

    resized = cv2.resize(image, (new_w, new_h))
    return resized

def detect_skin_and_label(image_path):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    image = cv2.imread(image_path)
    
    if image is None:
        print(f"Could not read the image at path: {image_path}")
        return
    
    resized = resize_image(image, 600, 600)
    
    hsv = cv2.cvtColor(resized, cv2.COLOR_BGR2HSV)
    
    sk_lower = np.array([0, 10, 60], dtype=np.uint8)  
    sk_upper = np.array([20, 150, 255], dtype=np.uint8)  
    
    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
    face = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    for x, y, w, h in face:
        face_roi = hsv[y:y + h, x:x + w]
        
        mask = cv2.inRange(face_roi, sk_lower, sk_upper)
        
        total_pixels = w * h
        skin_pixels = cv2.countNonZero(mask)
        sk_prc = (skin_pixels / total_pixels) * 100
        
        text = ""
        if 0 < sk_prc <= 50:  
            text = "dark skin"
        elif 50 < sk_prc <= 60:  
            text = "light brown skin"
        elif 60 < sk_prc <= 65:  
            text = "olive skin"
        elif 65 < sk_prc <= 85:  
            text = "medium skin"
        else:
            text = "fair skin"
        
        cv2.putText(resized, text, (x, y - 10), cv2.FONT_HERSHEY_DUPLEX, 0.7, (0, 255, 0), 2)
        cv2.rectangle(resized, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    cv2.imshow('Detected Faces', resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def start_skin_recognition():
    folder_path = filedialog.askdirectory(initialdir=os.getcwd(), title="Select Subject Folder")
    if folder_path:
        files_paths = glob.glob(os.path.join(folder_path, '*.jpg'))

        for file_ in files_paths: 
            print(f"Processing file: {file_}")
            detect_skin_and_label(file_)

def open_subject_folder():
    folder_path = filedialog.askdirectory(initialdir=os.getcwd(), title="Select Subject Folder")
    if folder_path:
        try:
            subprocess.Popen(['explorer', folder_path])
        except Exception as e:
            print(f"Error opening folder: {e}")


root = tk.Tk()
root.title("Anagnorisis")
root.geometry("500x300")  


title_label = tk.Label(root, text="Anagnorisis", font=("@ Malgun Gothic", 20, "bold"))
title_label.pack(pady=20)

subtitle_label = tk.Label(root, text="Simple program that *guesses* skin tone based on HSV.\n Just press start and choose a directory!", font=("Terminal", 10))
subtitle_label.pack(pady=10)
subtitle_label2 = tk.Label(root, text="this project was created as a means \n to get more into cv2 and haar \n and in no way shape or form is 100% accurate \n (in fact it's about 68.7% accurate(for the time being))", font=("Terminal", 8, "bold"))
subtitle_label2.pack(pady=10)


start_button = tk.Button(root, text="Start", font=("Terminal", 10), command=start_skin_recognition)
start_button.pack(pady=5)


root.mainloop()
