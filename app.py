from dotenv import find_dotenv , load_dotenv
from transformers import pipeline


load_dotenv(find_dotenv())

def img2text(url):
    img_to_text = pipeline("image-to-text",model="Salesforce/blip-image-captioning-base")
    text = img_to_text(url)
    print(text)
    return text

img2text("Screenshot (72).png")

