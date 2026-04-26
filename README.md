# Legal-Compliance-API

Backend API buil with FastAPI to simulate LGPD compliance, incluling consent management, data validation, and audit logging.

# 📜 Legal Compliance API (FastAPI)

## 📌 Overview

The **Legal Compliance API** is a backend project designed to simulate a legal compliance system based on **LGPD (Brazilian General Data Protection Law)** principles.

This API demonstrates how legal requirements can be translated into business rules and validation logic, focusing on data protection, user consent, and compliance enforcement.

The project is intended for portfolio, academic purposes (TCC), and backend skill development.

---

## 🎯 Objectives

- Implement LGPD-based data validation
- Register and manage user consent
- Apply legal rules to data processing flows
- Simulate a real-world compliance system
- Demonstrate backend best practices

---

## 🧱 Tech Stack

- Python 3.11+
- FastAPI
- Pydantic
- Uvicorn
- Pytest
- SQLite (optional / future implementation)

---

## 📂 Project Structure (Initial)

```
app/
├── main.py
├── routers/
│   └── compliance.py
├── services/
│   └── compliance_service.py
├── schemas/
│   └── compliance.py
├── core/
│   └── rules.py

tests/
└── ...
```

---

## ⚙️ Features (V1)

- Data validation for sensitive information
- User consent registration
- Basic legal rule enforcement
- Layered architecture (router, service, schema)
- Automatic API documentation (Swagger)

---

## 🚧 Roadmap

### V1 (Current)

- Basic validations
- Simple consent handling
- API structure

### V2 (Planned)

- Database persistence
- Legal logging system
- Consent history tracking
- Advanced LGPD rules

---

## ▶️ How to Run

```bash
# create virtual environment
python -m venv venv

# activate (Windows)
venv\Scripts\activate

# install dependencies
pip install -r requirements.txt

# run server
uvicorn app.main:app --reload
```

Access:
http://127.0.0.1:8000/docs

---

## 🧪 Tests

```bash
python -m pytest
```

---

## 📖 Documentation

The API provides interactive documentation via Swagger UI.

---

## 📌 Use Cases

- Register users with sensitive data
- Enforce mandatory consent validation
- Block operations that violate compliance rules

---

## ⚖️ Disclaimer

This project is for educational purposes only and does not replace real legal systems or professional legal advice.

---

## 📄 License

MIT License
