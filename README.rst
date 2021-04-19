CommCare FHIR Web App
=====================

A reference implementation of a web application that integrates with
CommCare using FHIR


Running in a development environment
------------------------------------

Requires Python 3.9+.

1. Create a virtual environment::

       $ python3.9 -m venv venv
       $ source venv/bin/activate

2. Install requirements::

       $ pip install -r requirements.txt

3. Configure environment variables::

       $ cp _env_example .env
       $ $EDITOR .env    # (where $EDITOR is your favorite editor)
       $ source .env

4. Run the development web server::

       $ uvicorn web_app.main:app --reload

