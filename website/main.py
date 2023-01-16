import os
from flask import Flask, render_template, redirect, flash, request, send_from_directory
from werkzeug.utils import secure_filename
from utils import *

app = Flask(__name__)
app.config['UPLOADS_FOLDER'] = '/media/pics'
app.config['SECRET_KEY'] = 'my secret'

@app.route('/', methods=["GET", "POST"])
def index():
  if request.method == "GET":
    return render_template('index.html')
  
  if not 'file' in request.files:
    flash('No file part in request')
    return redirect(request.url)

  files = request.files.getlist('file')

  for file in files:
    if file.filename == '':
      flash('No file uploaded')
      return redirect(request.url)

    if file_valid(file.filename):
      filename = secure_filename(file.filename)
      file.save(os.path.join(app.config['UPLOADS_FOLDER'], filename))
    else:
      flash('Invalid file type')
      return redirect(request.url) 
      
  return "Files uploaded successfully"

@app.route('/media/pics/<path:filename>')
def send_attachment(filename):
  return send_from_directory(app.config['UPLOADS_FOLDER'], 
    filename=filename, as_attachment=True)
