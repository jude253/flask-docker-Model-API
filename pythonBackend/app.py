from flask import Flask, render_template, request, send_from_directory
import json
from pythonBackend.static.Gender_age_classifier.gender_text_classifier import gender_text_classifier
from pythonBackend.static.Name_classifier.nameClassifier import name_classifier
from pythonBackend.blueprints.page import page


def create_app():
    """
    Create a Flask application using the app factory pattern.

    :return: Flask app
    """
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object('config.settings')
    app.config.from_pyfile('settings.py', silent=True)

    @app.route('/api/textGender', methods=['POST'])
    def get_text_gender():
        textInput = request.json['textInput']
        response = gender_text_classifier(textInput)
        return json.dumps(response)

    @app.route('/api/nameGender', methods=['POST'])
    def get_name_gender():
        textInput = request.json['nameInput']
        response = name_classifier(textInput)
        return json.dumps(response)

    app.register_blueprint(page)
    return app
