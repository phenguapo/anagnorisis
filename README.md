# Anagnorisis - Skin Tone Detection with OpenCV

## Overview
Anagnorisis is a simple Python application built using OpenCV and Tkinter for guessing skin tone based on HSV (Hue, Saturation, Value) values. This project aims to provide an introduction to OpenCV's capabilities in facial detection, color space manipulation and image mapping.

## Requirements
### To run this project, ensure you have:

- Python 3.x installed
- Required Python packages:
    - cv2 (OpenCV)
    - numpy
    - tkinter
You can install the necessary packages via pip:
```bash
pip install opencv-python numpy tk
```
## How to Use
1. **Clone the Repository**
```bash
git clone https://github.com/phenguapo/anagnorisis.git
cd anagnorisis
```
2. **Run the Application**
Run the anagnorisis.py file using Python:
```bash
python anagnorisis.py
```
3. **Using the Application**
- Upon running the application, a GUI window will appear.
- Click the **"Start"** button to select a directory containing JPEG images for skin tone detection.
- The application will process each image, detecting faces and guessing skin tones based on HSV values.
- The results will be displayed in separate windows for each image.
4. **Understanding Skin Tone Labels**
- The application categorizes skin tones into labels based on a heuristic evaluation of skin pixel percentages in detected faces.
- Labels: "dark skin", "light brown skin", "olive skin", "medium skin", "fair skin".
- The accuracy of these labels may vary based on the lighting, image quality, diversity of the dataset and my own mistakes.

## Contributing
Contributions to improve accuracy, optimize code, or add new features are more than welcome!

## Acknowledgments
This project was inspired by the need to learn more about face detection using OpenCV and a deep itch to find out more about haar cascading.

## /subj/ Copyrights
### !!!THIS PROJECT IS COMPLETELY NON-PROFIT!!!
None of the pictures in this project belong to me and were uploaded because they were the ones i used while making this project. If any copyright owner wants them down i'm more than happy to do that, just shoot me a message!
