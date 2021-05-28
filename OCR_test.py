import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:\Users\klys\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

text = pytesseract.image_to_string(Image.open('Capture.JPG'))
print(text)