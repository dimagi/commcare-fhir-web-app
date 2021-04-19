from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from web_app.fhir_client import fetch_patient

app = FastAPI(default_response_class=HTMLResponse)
templates = Jinja2Templates(directory="templates")


@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("root.html", {
        'request': request,
    })


@app.get("/patient/")
async def view_patient(request: Request):
    patient_id = request.query_params['patient_id']
    patient = await fetch_patient(patient_id)
    return templates.TemplateResponse("patient.html", {
        'request': request,
        'patient': patient,
    })
