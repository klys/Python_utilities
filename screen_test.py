from PIL import ImageGrab

cap = ImageGrab.grab(bbox =(0, 0, 100, 100))
cap.save("picture.png")