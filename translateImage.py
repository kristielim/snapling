import io
import os

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types
from google.cloud import translate

def get_translation(image_path, target_language):
	# returns the description of an image
	def detect_labels(path):
	    client = vision.ImageAnnotatorClient()

	    with io.open(path, 'rb') as image_file:
	        content = image_file.read()

	    image = types.Image(content=content)

	    response = client.label_detection(image=image)
	    labels = response.label_annotations
	    return (labels[0].description)
	# returns a the given text in English and the translation in target language, separated by a comma
	def translate_text(target, text):
	    # Instantiates a client
	    translate_client = translate.Client()

	    # Translates some text into Russian
	    translation = translate_client.translate(
	        text,
	        target_language=target)

	    return text + ',' + translation['translatedText']

	#Actual calls to helpers    
	text = detect_labels(image_path)
	return translate_text(target_language, text)