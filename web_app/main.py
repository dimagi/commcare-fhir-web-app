from flask import Flask, render_template, request

from web_app.fhir_client import fetch_patient_data

app = Flask(__name__)


@app.route('/')
def root():
    return render_template('root.html')


@app.route('/patient/')
def view_patient():
    patient_id = request.args['patient_id']
    patient, observations, diag_reports = fetch_patient_data(patient_id)
    return render_template(
        "patient.html",
        patient=patient,
        observations=observations,
        diag_reports=diag_reports,
    )
