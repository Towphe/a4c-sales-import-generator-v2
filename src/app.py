import os
from flask import Flask, render_template
from .endpoints import sales_import_generator

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    UPLOAD_FOLDER = 'temp'
    ALLOWED_EXTENSIONS = {'xlsx'}
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

    # if test_config is None:
    #     # load the instance config, if it exists, when not testing
    #     app.config.from_pyfile('config.py', silent=True)
    # else:
    #     # load the test config if passed in
    #     app.config.from_mapping(test_config)

    # # ensure the instance folder exists
    # try:
    #     os.makedirs(app.instance_path)
    # except OSError:
    #     pass

    app.register_blueprint(sales_import_generator, url_prefix="/api")

    # root page
    @app.route("/")
    def index():
        return render_template('index.html')

    return app
