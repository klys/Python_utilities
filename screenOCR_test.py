from PIL import ImageGrab
import pytesseract
from PIL import Image

cap = ImageGrab.grab(bbox =(0, 0, 100, 100))
cap.save("picture1.png")

pytesseract.pytesseract.tesseract_cmd = r"C:\Users\klys\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

text = pytesseract.image_to_string(Image.open("picture1.png"))
print(text)