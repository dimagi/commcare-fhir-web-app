import os


def slash_join(*args: str) -> str:
    """
    Joins ``args`` with a single "/"

    >>> slash_join('http://example.com', 'a/', '/foo/')
    'http://example.com/a/foo/'

    """
    if not args:
        return ''
    append_slash = args[-1].endswith('/')
    url = '/'.join([arg.strip('/') for arg in args])
    return url + '/' if append_slash else url


def base_url() -> str:
    """
    Returns the FHIR API base URL based on environment variables.
    """
    https_commcarehq_org = os.environ['CCHQ_BASE_URL']
    proj = os.environ['CCHQ_PROJECT_SPACE']
    return slash_join(https_commcarehq_org, f'/a/{proj}/fhir/R4/')


def auth_header() -> dict:
    """
    Returns the API Key auth header based on environment variables.
    """
    username = os.environ['CCHQ_USERNAME']
    api_key = os.environ['CCHQ_API_KEY']
    return {'Authorization': f'ApiKey {username}:{api_key}'}
