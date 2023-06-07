import pytesseract
import cv2  # pip install opencv-python


def search_text(image, lang1='eng', lang2='rus'):
    image_path = image
    image = cv2.imread(image_path)

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    text = pytesseract.image_to_string(gray_image, lang=f"{lang1}+{lang2}")

    return text
