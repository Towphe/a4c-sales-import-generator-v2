from flask import Flask, flash, request, redirect, url_for, render_template, send_from_directory
import os
from .modules import extract_from_ginee, generate_sales_import, sales_persons_dict
from werkzeug.utils import secure_filename
from dateutil import parser
from datetime import datetime
import pandas as pd

# directory
UPLOAD_FOLDER = 'temp'
ALLOWED_EXTENSIONS = {'xlsx'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

#upload_manager = init_upload_manager(app)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/download")
def download():
    # return file
    query = request.args.to_dict(flat=False)
    return render_template('download.html', file=query['file'][0])

@app.route("/api/process-file", methods=['POST'])
def processFile():
    #print(request.form.get('store'))
    file = request.files['file']
    if file.filename == '':
        return redirect(url_for('index'))
    if file:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(file.filename))

        # print(file_path)
        file.save(file_path)

        # then process file
        current_date = datetime.now()

        output = None
        df = pd.DataFrame()
        try:
            #df = extract_from_ginee(file_path)
            output = extract_from_ginee(file_path)
            df = output['output']
        except Exception as e:
            # print(e)
            return redirect(url_for('index', s='file-error'))
        output_file_name = str(current_date.month) + "-" + str(current_date.day)+ "-" + str(current_date.year) + " " + output['filename'] +".xlsx"
        # os.remove(file_path)

        if (type(df) == bool):
            return redirect(url_for('index'))

        output_path = os.path.join(app.config['UPLOAD_FOLDER'], output_file_name)
        generate_sales_import(df, int(request.form.get('starting_num')), output_path)

    return redirect(url_for('download', file=output_file_name))

@app.route('/api/download-file', methods=['POST'])
def downloadFile():
    if request.form.get('filename') == '':
        return "non-existent"
    # add background task that deletes the file after 10 minutes
    return send_from_directory(app.config['UPLOAD_FOLDER'], request.form.get('filename'))

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
