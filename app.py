import os
import base64
#from translateImage import get_translation
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def normal():
	return render_template('ind.html')

@app.route('/pic', methods=["POST"])
def pic_to_word():
	file = request.files["file"]
	path_name = 'temp_pics/testpic.jpg'
	file.save(path_name)
	translation = get_translation(path_name, 'fr')
	#translation has original word and translation, separated by a comma
	print("translation",translation)
	os.remove(path_name)
	return translation

@app.route('/picURL', methods=["POST"])
def picURL_to_word():
	dataurl = request.data[22:]
	imgdata = base64.b64decode(dataurl)
	path_name = 'temp_pics/testpic.jpg'
	with open(path_name, 'wb') as file:
		file.write(imgdata)
	translation = get_translation(path_name, 'fr')
	#translation has original word and translation, separated by a comma
	print("translation",translation)
	os.remove(path_name)
	return translation