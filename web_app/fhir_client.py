import asyncio
import logging
from typing import Optional

import aiohttp

from web_app.http import auth_header, base_url, slash_join


async def fetch_patient_data(patient_id):
    """
    Fetches a Patient resource, and Observation and DiagnosticReport
    resources filtered by the Patient's ID.
    """
    async with aiohttp.ClientSession() as session:
        patient, observations, diag_reports = await asyncio.gather(
            fetch_resource(session, 'Patient', patient_id),
            search_resources(session, 'Observation', patient_id),
            search_resources(session, 'DiagnosticReport', patient_id),
        )
        return patient, observations, diag_reports


async def fetch_resource(session, resource_type, resource_id):
    """
    Fetches a single resource.
    """
    url = slash_join(base_url(), f'/{resource_type}/{resource_id}/')
    return await fetch_json(session, url)


async def search_resources(session, resource_type, patient_id):
    """
    Search resources of ``resource_type`` by ``patient_id``
    """
    url = slash_join(base_url(), f'/{resource_type}/')
    params = {'patient_id': patient_id}
    async with session.get(url, params=params, headers=auth_header()) as resp:
        if resp.status != 200:
            text = await resp.text()
            logging.warning(f'URL: {url}: {resp.status}: {text}')
            return None
        searchset_bundle = await resp.json()
        urls = (e['fullUrl'] for e in searchset_bundle['entry'])
        coroutines = (fetch_json(session, u) for u in urls)
        return await asyncio.gather(*coroutines)


async def fetch_json(session, url) -> Optional[dict]:
    """
    Sends a GET request to ``url`` and returns the response JSON as a
    ``dict``. If the response status code is not 200, returns ``None``.
    """
    async with session.get(url, headers=auth_header()) as resp:
        if resp.status != 200:
            text = await resp.text()
            logging.warning(f'URL: {url}: {resp.status}: {text}')
            return None
        return await resp.json()
