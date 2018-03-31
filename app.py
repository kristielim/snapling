import os
from translateImage import get_translation
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def normal():
	return render_template('ind.html')

@app.route('/pic', methods=["POST"])
def pic_to_word():
	print(1)
	file = request.files['file']
	path_name = 'temp_pics/testpic.jpg'
	file.save(path_name)
	translation = get_translation(path_name, 'fr')
	print("translation",translation)
	os.remove(path_name)
	return translation[1]
