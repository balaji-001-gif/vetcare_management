import frappe

def create_demo_data():
    frappe.flags.in_setup = True
    print("Starting Demo Data Setup for Vetcare Management...")

    # 1. Masters
    create_branch_clinic()
    create_species_and_breeds()
    create_vaccines()
    create_lab_tests()
    create_hospital_wards_beds()

    # 2. Staff
    create_veterinarians()

    # 3. Clients and Patients
    create_pet_owners_and_pets()

    # 4. Transactions
    create_appointments_and_consultations()

    frappe.db.commit()
    frappe.flags.in_setup = False
    print("Demo Data Setup Completed successfully!")

def create_branch_clinic():
    print("Creating Branch Clinics...")
    branches = ["Main Vet Hospital", "City Branch Clinic"]
    for branch in branches:
        if not frappe.db.exists("Branch Clinic", branch):
            frappe.get_doc({
                "doctype": "Branch Clinic",
                "branch_name": branch,
                "contact_number": "+1234567890",
                "email": "contact@vethospital.com",
                "address": "123 Vet Street, City"
            }).insert(ignore_permissions=True)

def create_species_and_breeds():
    print("Creating Animal Species and Breeds...")
    species_breeds = {
        "Dog": ["Labrador Retriever", "Golden Retriever", "German Shepherd", "Bulldog"],
        "Cat": ["Persian", "Maine Coon", "Siamese", "Bengal"],
        "Bird": ["Parrot", "Canary"]
    }
    for species, breeds in species_breeds.items():
        if not frappe.db.exists("Animal Species", species):
            frappe.get_doc({
                "doctype": "Animal Species",
                "species_name": species
            }).insert(ignore_permissions=True)

        for breed in breeds:
            if not frappe.db.exists("Animal Breed", breed):
                frappe.get_doc({
                    "doctype": "Animal Breed",
                    "breed_name": breed,
                    "species": species
                }).insert(ignore_permissions=True)

def create_vaccines():
    print("Creating Vaccines...")
    vaccines = [
        {"name": "Rabies", "species": "Dog", "validity_months": 12},
        {"name": "DHPP", "species": "Dog", "validity_months": 12},
        {"name": "FVRCP", "species": "Cat", "validity_months": 12}
    ]
    for v in vaccines:
        if not frappe.db.exists("Vaccine", v["name"]):
            frappe.get_doc({
                "doctype": "Vaccine",
                "vaccine_name": v["name"],
                "target_species": v["species"],
                "validity_period_months": v["validity_months"]
            }).insert(ignore_permissions=True)

def create_lab_tests():
    print("Creating Lab Test Types...")
    tests = ["Complete Blood Count (CBC)", "Urinalysis", "X-Ray", "Ultrasound"]
    for t in tests:
        if not frappe.db.exists("Lab Test Type", t):
            frappe.get_doc({
                "doctype": "Lab Test Type",
                "test_name": t,
                "description": f"Standard {t}"
            }).insert(ignore_permissions=True)

def create_hospital_wards_beds():
    print("Creating Wards and Beds...")
    wards = ["General Ward", "ICU", "Recovery"]
    for ward in wards:
        if not frappe.db.exists("Hospital Ward", ward):
            frappe.get_doc({
                "doctype": "Hospital Ward",
                "ward_name": ward,
                "capacity": 5
            }).insert(ignore_permissions=True)
            
            for i in range(1, 4):
                bed_num = f"{ward}-Bed-{i}"
                if not frappe.db.exists("Hospital Bed", bed_num):
                    frappe.get_doc({
                        "doctype": "Hospital Bed",
                        "bed_number": bed_num,
                        "ward": ward,
                        "status": "Available"
                    }).insert(ignore_permissions=True)

def create_veterinarians():
    print("Creating Veterinarians...")
    vets = [
        {"name": "Dr. John Smith", "specialization": "General Practitioner"},
        {"name": "Dr. Sarah Patel", "specialization": "Surgery"},
        {"name": "Dr. Emily Chen", "specialization": "Dermatology"}
    ]
    for vet in vets:
        if not frappe.db.exists("Veterinarian", {"full_name": vet["name"]}):
            frappe.get_doc({
                "doctype": "Veterinarian",
                "full_name": vet["name"],
                "specialization": vet["specialization"],
                "mobile_no": "9876543210"
            }).insert(ignore_permissions=True)

def create_pet_owners_and_pets():
    print("Creating Pet Owners and Pets...")
    owners = [
        {"name": "Alice Johnson", "mobile": "555-0101", "email": "alice@example.com"},
        {"name": "Bob Williams", "mobile": "555-0202", "email": "bob@example.com"}
    ]
    for o in owners:
        if not frappe.db.exists("Pet Owner", {"full_name": o["name"]}):
            owner_doc = frappe.get_doc({
                "doctype": "Pet Owner",
                "full_name": o["name"],
                "mobile_no": o["mobile"],
                "email_id": o["email"],
                "city": "Metropolis"
            }).insert(ignore_permissions=True)
            
            if o["name"] == "Alice Johnson":
                frappe.get_doc({
                    "doctype": "Patient Pet",
                    "pet_name": "Max",
                    "owner": owner_doc.name,
                    "species": "Dog",
                    "breed": "Labrador Retriever",
                    "gender": "Male",
                    "weight_kg": 25.0
                }).insert(ignore_permissions=True)
            else:
                frappe.get_doc({
                    "doctype": "Patient Pet",
                    "pet_name": "Luna",
                    "owner": owner_doc.name,
                    "species": "Cat",
                    "breed": "Persian",
                    "gender": "Female",
                    "weight_kg": 4.5
                }).insert(ignore_permissions=True)

def create_appointments_and_consultations():
    print("Creating Appointments and Consultations...")
    pet_max = frappe.db.get_value("Patient Pet", {"pet_name": "Max"}, "name")
    dr_john = frappe.db.get_value("Veterinarian", {"full_name": "Dr. John Smith"}, "name")
    
    if pet_max and dr_john:
        max_doc = frappe.get_doc("Patient Pet", pet_max)
        if not frappe.db.exists("Vet Appointment", {"patient": pet_max}):
            apt = frappe.get_doc({
                "doctype": "Vet Appointment",
                "patient": pet_max,
                "owner": max_doc.owner,
                "veterinarian": dr_john,
                "appointment_date": frappe.utils.today(),
                "appointment_time": "10:00:00",
                "appointment_type": "Consultation",
                "chief_complaint": "Annual Checkup",
                "status": "Completed"
            }).insert(ignore_permissions=True)
            apt.submit()

            con = frappe.get_doc({
                "doctype": "Vet Consultation",
                "appointment": apt.name,
                "patient": pet_max,
                "owner": max_doc.owner,
                "veterinarian": dr_john,
                "consultation_date": frappe.utils.today(),
                "weight_kg": 25.0,
                "temperature_c": 38.5,
                "heart_rate": 80,
                "chief_complaint": "Annual Checkup",
                "diagnosis": "Healthy, routine checkup clear",
                "treatment_plan": "Continue regular diet and exercise"
            }).insert(ignore_permissions=True)
            con.submit()
