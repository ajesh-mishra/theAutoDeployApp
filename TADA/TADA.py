import panda_excel2xml as PEX
from pandas import read_excel
from flask import Flask, render_template, request, make_response

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
  excel_file = request.files['inputFile']
  df = read_excel(excel_file)
  response = PEX.import_excel(df)

  # return response
  # return render_template('showxml.html', response=response)
  
  template = make_response(response)
  template.headers['Content-Type'] = 'application/xml'

  return template

if __name__ == '__main__':
  app.run(debug=True)





























# from flask_sqlalchemy import SQLAlchemy

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://///Users/lipu/Downloads/Python Programs/TADA/filestorage.db'
# db = SQLAlchemy(app)

# class FileContents(db.Model):
#   id = db.Column(db.Integer, primary_key=True)
#   name = db.Column(db.String(300))
#   data = db.Column(db.LargeBinary)

  # newFile = FileContents(name=file.filename, data=file.read())
  # db.session.add(newFile)
  # db.session.commit()
