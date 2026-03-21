from fastapi import FastAPI, HTTPException, Query, status, Response
from pydantic import BaseModel, Field
from typing import List, Optional

app = FastAPI(title="Medical Appointment System")


patients = [
    {"id": 1, "name": "John", "age": 25, "gender": "Male"},
    {"id": 2, "name": "Sara", "age": 30, "gender": "Female"},
]

doctors = [
    {"id": 1, "name": "Dr. Smith", "specialization": "Cardiology", "fee": 500},
    {"id": 2, "name": "Dr. Lee", "specialization": "Dermatology", "fee": 300},
]

appointments = [
    {
        "id": 1,
        "patient": "John",
        "doctor": "Dr. Smith",
        "specialization": "Cardiology",
        "symptoms": "Fever",
        "type": "offline",
        "fee": 500,
        "status": "booked"
    },
    {
        "id": 2,
        "patient": "Sara",
        "doctor": "Dr. Lee",
        "specialization": "Dermatology",
        "symptoms": "Skin allergy",
        "type": "online",
        "fee": 300,
        "status": "completed"
    },
    {
        "id": 3,
        "patient": "John",
        "doctor": "Dr. Lee",
        "specialization": "Dermatology",
        "symptoms": "Acne issue",
        "type": "offline",
        "fee": 300,
        "status": "booked"
    },
    {
        "id": 4,
        "patient": "Sara",
        "doctor": "Dr. Smith",
        "specialization": "Cardiology",
        "symptoms": "Chest pain",
        "type": "offline",
        "fee": 500,
        "status": "completed"
    },
    {
        "id": 5,
        "patient": "John",
        "doctor": "Dr. Smith",
        "specialization": "Cardiology",
        "symptoms": "High BP",
        "type": "online",
        "fee": 500,
        "status": "booked"
    }
]

appointment_counter = 6
patient_counter = 3


def find_patient(pid):
    for p in patients:
        if p["id"] == pid:
            return p
    return None

def find_doctor(did):
    for d in doctors:
        if d["id"] == did:
            return d
    return None

def find_appointment(aid):
    for a in appointments:
        if a["id"] == aid:
            return a
    return None

def calculate_fee(fee):
    return fee




class Patient(BaseModel):
    name: str = Field(min_length=2, json_schema_extra={"example": "Amit Kumar"})
    age: int = Field(gt=0, lt=120, json_schema_extra={"example": 28})
    gender: str = Field(json_schema_extra={"example": "Male"})

class AppointmentRequest(BaseModel):
    patient_id: int = Field(gt=0, json_schema_extra={"example": 1})
    doctor_id: int = Field(gt=0, json_schema_extra={"example": 2})
    symptoms: str = Field(min_length=3, json_schema_extra={"example": "Persistent cough and fever"})
    consultation_type: str = Field(default="offline", json_schema_extra={"example": "online"})


@app.get("/")
def home():
    return {"message": "Welcome to Medical Appointment System"}

@app.get("/patients")
def get_patients():
    return {"total": len(patients), "data": patients}

@app.get("/patients/summary")
def patient_summary():
    return {
        "total": len(patients),
        "male": len([p for p in patients if p["gender"] == "Male"]),
        "female": len([p for p in patients if p["gender"] == "Female"])
    }


@app.get("/patients/filter")
def filter_patients(
    gender: Optional[str] = None,
    min_age: Optional[int] = None
):
    result = patients

    if gender is not None:
        result = [p for p in result if p["gender"].lower() == gender.lower()]

    if min_age is not None:
        result = [p for p in result if p["age"] >= min_age]

    return {"count": len(result), "data": result}

@app.get("/patients/{patient_id}")
def get_patient(patient_id: int):
    patient = find_patient(patient_id)
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patient

@app.get("/appointments")
def get_appointments():
    return {"total": len(appointments), "data": appointments}


@app.post("/appointments", status_code=201)
def create_appointment(req: AppointmentRequest):
    global appointment_counter

    patient = find_patient(req.patient_id)
    doctor = find_doctor(req.doctor_id)

    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")

    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")

    total_fee = calculate_fee(doctor["fee"])

    appointment = {
        "id": appointment_counter,
        "patient": patient["name"],
        "doctor": doctor["name"],
        "specialization": doctor["specialization"],
        "symptoms": req.symptoms,
        "type": req.consultation_type,
        "fee": total_fee,
        "status": "booked"
    }

    appointments.append(appointment)
    appointment_counter += 1

    return appointment


@app.post("/patients", status_code=201)
def add_patient(p: Patient):
    global patient_counter

    new_patient = {
        "id": patient_counter,
        **p.dict()
    }
    patients.append(new_patient)
    patient_counter += 1

    return new_patient

@app.put("/patients/{patient_id}")
def update_patient(
    patient_id: int,
    name: Optional[str] = None,
    age: Optional[int] = None
):
    patient = find_patient(patient_id)

    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")

    if name is not None:
        patient["name"] = name
    if age is not None:
        patient["age"] = age

    return patient

@app.delete("/patients/{patient_id}")
def delete_patient(patient_id: int):
    patient = find_patient(patient_id)

    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")

    patients.remove(patient)
    return {"message": "Patient deleted"}


@app.post("/appointments/complete/{appointment_id}")
def complete_appointment(appointment_id: int):
    appointment = find_appointment(appointment_id)

    if not appointment:
        raise HTTPException(status_code=404, detail="Appointment not found")

    appointment["status"] = "completed"
    return appointment


@app.get("/doctors/search")
def search_doctors(keyword: str):
    result = [
        d for d in doctors
        if keyword.lower() in d["name"].lower()
        or keyword.lower() in d["specialization"].lower()
    ]

    return {"total_found": len(result), "data": result}

@app.get("/appointments/search")
def search_appointments(name: str):
    result = [
        a for a in appointments
        if name.lower() in a["patient"].lower()
    ]

    return {"total": len(result), "data": result}

@app.get("/appointments/sort")
def sort_appointments(order: str = "asc"):
    sorted_data = sorted(
        appointments,
        key=lambda x: x["fee"],
        reverse=True if order == "desc" else False
    )

    return {"order": order, "data": sorted_data}

@app.get("/appointments/page")
def paginate_appointments(page: int = 1, limit: int = 2):
    start = (page - 1) * limit
    end = start + limit

    total = len(appointments)
    total_pages = (total + limit - 1) // limit

    return {
        "page": page,
        "limit": limit,
        "total": total,
        "total_pages": total_pages,
        "data": appointments[start:end]
    }

@app.get("/appointments/browse")
def browse_appointments(
    keyword: Optional[str] = None,
    order: str = "asc",
    page: int = 1,
    limit: int = 2
):
    data = appointments

    if keyword:
        data = [
            a for a in data
            if keyword.lower() in a["patient"].lower()
        ]

    data = sorted(
        data,
        key=lambda x: x["fee"],
        reverse=True if order == "desc" else False
    )

    start = (page - 1) * limit
    end = start + limit

    total = len(data)
    total_pages = (total + limit - 1) // limit

    return {
        "total": total,
        "total_pages": total_pages,
        "data": data[start:end]
    }
