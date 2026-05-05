# Vetcare Management

Vetcare Management is a comprehensive, production-ready Frappe / ERPNext application specifically designed for veterinary hospitals, clinics, and pet care centers. It provides an end-to-end operational framework for managing everything from basic pet registration and appointments to advanced hospitalization and surgical records.

## 🚀 Key Features

*   **Client & Patient Management**: Maintain detailed records for Pet Owners and their Pets, including breed, species, microchip IDs, and medical history.
*   **Appointment Scheduling**: Seamlessly book and manage veterinary appointments with urgency levels, types (consultation, surgery, grooming, etc.), and automated reminders.
*   **Clinical Consultations**: Dedicated modules for veterinarians to record vital signs, clinical findings, diagnoses, treatment plans, and prescriptions.
*   **Laboratory & Diagnostics**: Manage in-house or outsourced lab tests, record results, and handle imaging requests (X-rays, Ultrasound).
*   **Inpatient Hospitalization**: Full ward and bed management for pets requiring overnight or extended care, complete with daily monitoring logs and discharge alerts.
*   **Surgical & Vaccination Records**: Keep logs of surgeries performed and maintain a schedule for pet vaccinations with automated follow-up reminders.
*   **Ancillary Services**: Integrated modules for Pet Boarding (hotel) and Grooming services.

---

## 👥 User Roles & Permissions

The application is structured around specific roles to ensure data privacy and workflow efficiency:
*   **Vet Admin**: Full access to all modules, settings, and configuration.
*   **Veterinarian**: Access to appointments, consultations, prescriptions, lab results, surgeries, and inpatient records.
*   **Vet Receptionist**: Access to manage clients (Pet Owners), register pets, book appointments, and handle billing/payments.
*   **Vet Lab Technician**: Access to view lab requests, process tests, and upload results.
*   **Vet Groomer**: Access to grooming service appointments and boarding records.

---

## 📖 How to Use: Functional Workflow

Here is a step-by-step guide for a clinic to utilize the Vetcare Management system effectively:

### 1. Initial Setup (Admin Workflow)
Before taking in patients, the clinic administrator should configure the foundational data:
*   **Settings & Branches**: Go to **Vet Settings** and **Branch Clinic** to set up hospital branches and general preferences.
*   **Staff**: Register your doctors in the **Veterinarian** DocType.
*   **Medical Masters**: Populate **Animal Species** (e.g., Dog, Cat, Bird) and **Animal Breed**. Setup **Lab Test Types** and **Vaccines**.
*   **Facilities**: Create **Hospital Wards** (e.g., ICU, Recovery) and generate **Hospital Beds** within those wards.

### 2. Client & Patient Registration (Reception Workflow)
When a new client walks in:
1.  Navigate to **Pet Owner** and create a new profile with the owner's contact details and address. (This optionally links to standard ERPNext Customers for billing).
2.  Navigate to **Patient Pet**, click "Add", and select the previously created Owner. Fill in the pet's details (Name, Species, Breed, Gender, DOB, Microchip ID, Allergies).

### 3. Booking an Appointment (Reception Workflow)
To schedule a visit:
1.  Open **Vet Appointment** and create a new record.
2.  Select the **Patient Pet** (the owner is automatically fetched).
3.  Choose the **Appointment Date/Time**, **Veterinarian**, and **Appointment Type** (e.g., Consultation, Vaccination).
4.  Optionally log the **Chief Complaint** and update the status to "Scheduled" or "Confirmed".

### 4. Consultation & Treatment (Veterinarian Workflow)
When the patient is in the examination room:
1.  The Doctor opens the relevant **Vet Appointment** and creates a **Vet Consultation** from it.
2.  **Vitals**: Record Weight, Temperature, Heart Rate, and Respiratory Rate.
3.  **Clinical Notes**: Document the Clinical Examination, Diagnosis, and Treatment Plan.
4.  **Prescription**: If medication is needed, the doctor can generate a **Prescription** directly linked to this consultation.

### 5. Laboratory & Imaging
If diagnostics are required during the consultation:
1.  The Doctor creates a **Lab Test** request or an **Imaging Request**.
2.  The **Vet Lab Technician** processes the test, enters the findings/results into the same record, and submits it.
3.  The Doctor reviews the submitted Lab Test.

### 6. Hospitalization & Surgeries
For severe cases requiring admission:
1.  Create a **Pet Hospitalization** record. Select the Patient, assigned Veterinarian, Ward, and Bed.
2.  The nursing staff can log daily notes and vitals on this hospitalization record.
3.  If a procedure is required, a **Surgery Record** is created logging the surgical notes, anesthesia used, and outcomes.
4.  Once recovered, the pet is marked for Discharge.

### 7. Preventive Care & Ancillary Services
*   **Vaccinations**: Log shots administered in the **Vaccination Record**. The system will track the next due date and can automatically send reminders to the pet owner.
*   **Boarding**: When a pet is staying at the clinic while the owner travels, use the **Boarding Record** to track check-in/check-out dates, feeding instructions, and belongings.
*   **Grooming**: Log spa, washing, or trimming sessions via **Grooming Service**.
