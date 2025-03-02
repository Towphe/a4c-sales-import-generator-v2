from flask import request, redirect, url_for, render_template, send_from_directory, Blueprint, current_app, Response
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
def process_single_file():
    file = request.files['file']
    output_file_name = ""

    # handle error here
    # if file.filename == '':
    #     return redirect(url_for('index'))

    if file:
        file_path = os.path.join("".join(["src/", current_app.config['UPLOAD_FOLDER']]), secure_filename(file.filename))

        # print(file_path)
        file.save(file_path)

        # then process file
        current_date = datetime.now()

        df = pd.DataFrame()

        print(request.form.get("version"))

        output = extract_from_ginee(file_path, request.form.get("version"))

        # validate output
        if output == None:
            return Response("{'message':'Invalid file input'", status=400, mimetype="application/json")

        df = output['output']

        output_file_name = str(current_date.month) + "-" + str(current_date.day)+ "-" + str(current_date.year) + " " + "SALES IMPORTS" +".xlsx"

        # handle error here
        if (type(df) == bool):
            return Response("{'message':'Invalid file input'", status=400, mimetype="application/json")

        output_path = os.path.join("".join(["src/", current_app.config['UPLOAD_FOLDER']]), output_file_name)
        generate_sales_import(df, int(request.form.get('starting_num')), output_path)

    # return file name
    return Response(output_file_name, status=200, mimetype='application/json')

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
