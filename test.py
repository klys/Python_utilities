# cv2.cvtColor takes a numpy ndarray as an argument
import numpy as nm

import pytesseract

# importing OpenCV
import cv2

from PIL import ImageGrab


def imToString():

	# Path of tesseract executable
	pytesseract.pytesseract.tesseract_cmd = r"C:\Users\klys\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"
	#while(True):

		# ImageGrab-To capture the screen image in a loop.
		# Bbox used to capture a specific area.
	cap = ImageGrab.grab(bbox =(20, 20, 50, 50))
    #cap.save("screen", "JPEG")
		# Converted the image to monochrome for it to be easily
		# read by the OCR and obtained the output String.
	tesstr = pytesseract.image_to_string(
			cap,
			lang ='eng')
	print(tesstr)

# Calling the function
imToString()
