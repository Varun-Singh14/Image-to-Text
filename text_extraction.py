import io
from google.cloud import vision

def extract_text(image_path):
    client = vision.ImageAnnotatorClient()

    with io.open(image_path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)
    response = client.text_detection(image=image)
    texts = response.text_annotations

    extracted_text = []
    for text in texts:
        extracted_text.append(text.description)

    if response.error.message:
        raise Exception(f'{response.error.message}')

    return extracted_text
