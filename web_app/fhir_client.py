def fetch_patient_data(patient_id):
    """
    Fetches a Patient resource, and Observation and DiagnosticReport
    resources filtered by the Patient's ID.
    """
    patient = {
        'name': [{
            'text': 'Alice APPLE'
        }],
        'birthDate': '1991-04-28',
        'id': patient_id,
        'resourceType': 'Patient',
    }
    observations = []
    diag_reports = []
    return patient, observations, diag_reports
