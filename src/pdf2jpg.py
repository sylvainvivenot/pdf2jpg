from flask import Flask, render_template, request, send_file
from pdf2image import convert_from_path
import os
import io
import uuid
app = Flask(__name__)

@app.route('/', methods = ['POST'])
def upload_file():
   if request.method == 'POST':
      pdf = request.files['pdf']
      guid = uuid.uuid1()
      pdfFileName = str(guid) + '.pdf'
      jpgFileName = str(guid) + '.jpg'

      pdf.save(pdfFileName)
      
      images_from_path = convert_from_path(pdfFileName, output_folder=".", last_page=1, first_page =0)
      
      for page in images_from_path:
        page.save(jpgFileName, 'JPEG')
      with open(jpgFileName, 'rb') as bites:
        result = send_file(
          io.BytesIO(bites.read()),
          attachment_filename=jpgFileName,
          mimetype='image/jpg'
          )
      os.remove(pdfFileName)
      os.remove(jpgFileName)
      return result
@app.route('/healthcheck', methods = ['GET'])
def healthcheck():
  return "OK"



if __name__ == '__main__':
    app.run(host='0.0.0.0')
