import panda_excel2xml as PEX
from pandas import read_excel
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
  excel_file = request.files['inputFile']
  df = read_excel(excel_file)
  response = PEX.import_excel(df)

  # template_xml = make_response(response)
  # template_xml.headers['Content-Type'] = 'application/xml'
  # return template_xml

  return render_template('index.html', template_xml=response)

if __name__ == '__main__':
  app.run(port=5000, debug=True)





























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
