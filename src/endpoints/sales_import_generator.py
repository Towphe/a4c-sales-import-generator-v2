from flask import Flask, abort, flash, request, redirect, url_for, render_template, send_from_directory, Blueprint, current_app
import os
from ..modules import extract_from_ginee, generate_sales_import, sales_persons_dict
from werkzeug.utils import secure_filename
from dateutil import parser
from datetime import datetime
import pandas as pd
from src.endpoints import sales_import_generator

# # directory
# UPLOAD_FOLDER = 'temp'
# ALLOWED_EXTENSIONS = {'xlsx'}

# app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

#upload_manager = init_upload_manager(app)

sales_import_generator = Blueprint('sales_import_generator', __name__, template_folder='templates')


@sales_import_generator.route("/single-sales-import", methods=['POST'])
def processFile():
    #print(request.form.get('store'))
    file = request.files['file']
    if file.filename == '':
        return redirect(url_for('index'))
    if file:
        file_path = os.path.join("".join(["src/", current_app.config['UPLOAD_FOLDER']]), secure_filename(file.filename))

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

        output_path = os.path.join("".join(["src/", current_app.config['UPLOAD_FOLDER']]), output_file_name)
        generate_sales_import(df, int(request.form.get('starting_num')), output_path)

    # return file name
    return output_file_name

@sales_import_generator.route('/download-file', methods=['GET'])
def downloadFile():
    query = request.args.to_dict(flat=False)
    print(query['file'][0])
    if query['file'][0] == '':
        # set to 404
        return abort(404)

    # add background task that deletes the file after 10 minutes
    return send_from_directory(current_app.config['UPLOAD_FOLDER'], query['file'][0])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
