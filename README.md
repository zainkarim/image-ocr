# image-ocr 🔍
A simple image based OCR program written in Python using EasyOCR, Matplotlib, and OpenCV.

## Goals:
- The user is asked to specify a filename or path to an image which the program will then attempt to read.
- Once entered, the program will attempt open the file.
- Next, the program utilizes EasyOCR to search for and identify any English-language text in the image.
- Once any text has been identified, bounding boxes are drawn around each letter using OpenCV and any text read by EasyOCR is superimposed onto the image.
- Finally, the image is opened using Matplotlib. 

## Knowledge gained
1. Introduction to OpenCV, EasyOCR, Matplotlib, and Python.
2. Learning the imread, imshow, rectangle, and putText CV2 functions.
3. Learning about adjusting EasyOCR parameters to dial in sensitivity.
4. Introduction to computer vision.
