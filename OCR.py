import pytesseract
from PIL import Image

# Path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\keroy\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

def ocr(image_path):
    # Open the image using PIL
    image = Image.open(image_path)

    # Perform OCR using Tesseract
    text = pytesseract.image_to_string(image)

    return text

# Path to the input image
image_path = r'C:\Users\keroy\OneDrive\Desktop\IdeaJam\Test.jpg'

# Perform OCR on the image
result = ocr(image_path)

# Print the extracted text
print(result)

