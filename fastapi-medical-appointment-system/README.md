# 🚀 Medical Appointment System - FastAPI Project

This is a complete backend application built using FastAPI as part of internship training.

---

##  Project Description

The Medical Appointment System allows users to:
- Manage patients
- Book appointments with doctors
- Search and filter data
- Perform CRUD operations
- Handle complete appointment workflow

---

##  Tech Stack

- Python
- FastAPI
- Pydantic
- Uvicorn

---

##  Features Implemented

###  Day 1 - GET APIs
- Home route
- Get all patients
- Get patient by ID
- Summary endpoint
- Get all appointments

###  Day 2 & 3 - POST + Validation
- Create appointment
- Pydantic validation
- Field constraints

###  Helper Functions
- find_patient()
- find_doctor()
- find_appointment()
- calculate_fee()

###  Day 4 - CRUD Operations
- Add patient
- Update patient
- Delete patient

###  Day 5 - Workflow
- Book appointment
- Complete appointment

### Day 6 - Advanced APIs
- Search doctors
- Search appointments
- Sorting appointments
- Pagination
- Combined browsing

---

##  API Endpoints

### Patients
- GET /patients
- GET /patients/{id}
- GET /patients/filter
- GET /patients/summary
- POST /patients
- PUT /patients/{id}
- DELETE /patients/{id}

### Appointments
- GET /appointments
- POST /appointments
- POST /appointments/complete/{id}
- GET /appointments/search
- GET /appointments/sort
- GET /appointments/page
- GET /appointments/browse

### Doctors
- GET /doctors/search



##  How to Run the Project

1. Install dependencies:
```bash
pip install -r requirements.txt
