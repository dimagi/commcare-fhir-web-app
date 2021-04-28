import logging
from typing import Optional

import requests

from web_app.http import slash_join, base_url, auth_header


def fetch_patient_data(patient_id):
    """
    Fetches a Patient resource, and Observation and DiagnosticReport
    resources filtered by the Patient's ID.
    """
    patient = fetch_resource('Patient', patient_id)
    observations = search_resources('Observation', patient_id)
    diag_reports = search_resources('DiagnosticReport', patient_id)
    return patient, observations, diag_reports


def fetch_resource(resource_type, resource_id):
    """
    Fetches a single resource.
    """
    url = slash_join(base_url(), f'/{resource_type}/{resource_id}/')
    return fetch_json(url)


def search_resources(resource_type, patient_id):
    """
    Search resources of ``resource_type`` by ``patient_id``
    """
    url = slash_join(base_url(), f'/{resource_type}/')
    params = {'patient_id': patient_id}
    resp = requests.get(url, params=params, headers=auth_header())
    if resp.status_code != 200:
        logging.warning(f'URL: {url}: {resp.status_code}: {resp.text}')
        return None
    searchset_bundle = resp.json()
    urls = (e['fullUrl'] for e in searchset_bundle['entry'])
    resources = [fetch_json(u) for u in urls]
    return resources


def fetch_json(url) -> Optional[dict]:
    """
    Sends a GET request to ``url`` and returns the response JSON as a
    ``dict``. If the response status code is not 200, returns ``None``.
    """
    resp = requests.get(url, headers=auth_header())
    if resp.status_code != 200:
        logging.warning(f'URL: {url}: {resp.status_code}: {resp.text}')
        return None
    return resp.json()
