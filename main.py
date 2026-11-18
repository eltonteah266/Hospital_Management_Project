import csv
import os

# Define CSV filenames
PATIENTS_FILE = 'patients.csv'
DOCTORS_FILE = 'doctors.csv'
APPOINTMENTS_FILE = 'appointments.csv'
VISITS_FILE = 'visits.csv'
PAYMENTS_FILE = 'payments.csv'

# Ensure all CSV files exist with proper headers when the program starts
def initialize_files():
    files_and_headers = {
        PATIENTS_FILE: ['patient_id', 'full_name', 'age', 'gender', 'phone', 'address'],
        DOCTORS_FILE: ['doctor_id', 'full_name', 'specialty', 'phone'],
        APPOINTMENTS_FILE: ['appointment_id', 'patient_id', 'doctor_id', 'date', 'time', 'status'],
        VISITS_FILE: ['visit_id', 'patient_id', 'doctor_id', 'visit_date', 'notes'],
        PAYMENTS_FILE: ['payment_id', 'patient_id', 'bill_amount', 'amount_paid', 'balance']
    }
    
    for filename, headers in files_and_headers.items():
        if not os.path.exists(filename):
            try:
                with open(filename, mode='w', newline='', encoding='utf-8') as file:
                    writer = csv.writer(file)
                    writer.writerow(headers)
            except Exception as e:
                print(f"Error initializing {filename}: {e}")

# Helper function to check if an ID exists in a CSV file
def id_exists(filename, id_column, target_id):
    if not os.path.exists(filename):
        return False
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row.get(id_column) == target_id:
                    return True
    except Exception:
        pass
    return False

# --- 1. PATIENT MANAGEMENT ---
def patient_management():
    while True:
        print("\n--- PATIENT MANAGEMENT ---")
        print("1. Register New Patient")
        print("2. List All Patients")
        print("3. Search Patient by ID")
        print("4. Update Patient Phone/Address")
        print("5. Delete Patient")
        print("6. Back to Main Menu")
        
        choice = input("Select an option (1-6): ").strip()
        
        if choice == '1':
            patient_id = input("Enter Patient ID (e.g., P001): ").strip()
            if id_exists(PATIENTS_FILE, 'patient_id', patient_id):
                print("Error: Patient ID already exists!")
                continue
            name = input("Enter Full Name: ").strip()
            age = input("Enter Age: ").strip()
            gender = input("Enter Gender: ").strip()
            phone = input("Enter Phone: ").strip()
            address = input("Enter Address: ").strip()
            
            try:
                with open(PATIENTS_FILE, mode='a', newline='', encoding='utf-8') as file:
                    writer = csv.writer(file)
                    writer.writerow([patient_id, name, age, gender, phone, address])
                print("Patient registered successfully!")
            except Exception as e:
                print(f"Error saving patient: {e}")
                
        elif choice == '2':
            try:
                with open(PATIENTS_FILE, mode='r', encoding='utf-8') as file:
                    reader = csv.DictReader(file)
                    print("\n--- REGISTERED PATIENTS ---")
                    count = 0
                    for row in reader:
                        count += 1
                        print(f"ID: {row['patient_id']} | Name: {row['full_name']} | Age: {row['age']} | Phone: {row['phone']}")
                    if count == 0:
                        print("No patients found.")
            except Exception as e:
                print(f"Error reading file: {e}")
                
        elif choice == '3':
            target_id = input("Enter Patient ID to search: ").strip()
            found = False
            try:
                with open(PATIENTS_FILE, mode='r', encoding='utf-8') as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        if row['patient_id'] == target_id:
                            print(f"\nFound: {row}")
                            found = True
                            break
                if not found:
                    print("Patient ID not found.")
            except Exception as e:
                print(f"Error searching: {e}")
                
        elif choice == '4':
            target_id = input("Enter Patient ID to update: ").strip()
            rows = []
            updated = False
            try:
                with open(PATIENTS_FILE, mode='r', encoding='utf-8') as file:
                    reader = csv.DictReader(file)
                    headers = reader.fieldnames
                    for row in reader:
                        if row['patient_id'] == target_id:
                            print(f"Current Phone: {row['phone']} | Address: {row['address']}")
                            row['phone'] = input("Enter new phone: ").strip()
                            row['address'] = input("Enter new address: ").strip()
                            updated = True
                        rows.append(row)
                
                if updated:
                    with open(PATIENTS_FILE, mode='w', newline='', encoding='utf-8') as file:
                        writer = csv.DictWriter(file, fieldnames=headers)
                        writer.writeheader()
                        writer.writerows(rows)
                    print("Patient updated successfully!")
                else:
                    print("Patient ID not found.")
            except Exception as e:
                print(f"Error updating: {e}")
                
        elif choice == '5':
            target_id = input("Enter Patient ID to delete: ").strip()
            rows = []
            deleted = False
            try:
                with open(PATIENTS_FILE, mode='r', encoding='utf-8') as file:
                    reader = csv.DictReader(file)
                    headers = reader.fieldnames
                    for row in reader:
                        if row['patient_id'] == target_id:
                            deleted = True
                            continue
                        rows.append(row)
                
                if deleted:
                    with open(PATIENTS_FILE, mode='w', newline='', encoding='utf-8') as file:
                        writer = csv.DictWriter(file, fieldnames=headers)
                        writer.writeheader()
                        writer.writerows(rows)
                    print("Patient deleted successfully!")
                else:
                    print("Patient ID not found.")
            except Exception as e:
                print(f"Error deleting: {e}")
                
        elif choice == '6':
            break
        else:
            print("Invalid option. Choose between 1 and 6.")

# --- 2. DOCTOR MANAGEMENT ---
def doctor_management():
    while True:
        print("\n--- DOCTOR MANAGEMENT ---")
        print("1. Register New Doctor")
        print("2. List All Doctors")
        print("3. Search Doctor by ID")
        print("4. Update Doctor Phone")
        print("5. Delete Doctor")
        print("6. Back to Main Menu")
        
        choice = input("Select an option (1-6): ").strip()
        
        if choice == '1':
            doc_id = input("Enter Doctor ID (e.g., D001): ").strip()
            if id_exists(DOCTORS_FILE, 'doctor_id', doc_id):
                print("Error: Doctor ID already exists!")
                continue
            name = input("Enter Full Name: ").strip()
            specialty = input("Enter Specialty: ").strip()
            phone = input("Enter Phone: ").strip()
            
            try:
                with open(DOCTORS_FILE, mode='a', newline='', encoding='utf-8') as file:
                    writer = csv.writer(file)
                    writer.writerow([doc_id, name, specialty, phone])
                print("Doctor registered successfully!")
            except Exception as e:
                print(f"Error saving doctor: {e}")
                
        elif choice == '2':
            try:
                with open(DOCTORS_FILE, mode='r', encoding='utf-8') as file:
                    reader = csv.DictReader(file)
                    print("\n--- REGISTERED DOCTORS ---")
                    count = 0
                    for row in reader:
                        count += 1
                        print(f"ID: {row['doctor_id']} | Name: {row['full_name']} | Specialty: {row['specialty']} | Phone: {row['phone']}")
                    if count == 0:
                        print("No doctors found.")
            except Exception as e:
                print(f"Error reading file: {e}")
                
        elif choice == '3':
            target_id = input("Enter Doctor ID to search: ").strip()
            found = False
            try:
                with open(DOCTORS_FILE, mode='r', encoding='utf-8') as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        if row['doctor_id'] == target_id:
                            print(f"\nFound: {row}")
                            found = True
                            break
                if not found:
                    print("Doctor ID not found.")
            except Exception as e:
                print(f"Error searching: {e}")
                
        elif choice == '4':
            target_id = input("Enter Doctor ID to update: ").strip()
            rows = []
            updated = False
            try:
                with open(DOCTORS_FILE, mode='r', encoding='utf-8') as file:
                    reader = csv.DictReader(file)
                    headers = reader.fieldnames
                    for row in reader:
                        if row['doctor_id'] == target_id:
                            print(f"Current Phone: {row['phone']}")
                            row['phone'] = input("Enter new phone: ").strip()
                            updated = True
                        rows.append(row)
                
                if updated:
                    with open(DOCTORS_FILE, mode='w', newline='', encoding='utf-8') as file:
                        writer = csv.DictWriter(file, fieldnames=headers)
                        writer.writeheader()
                        writer.writerows(rows)
                    print("Doctor updated successfully!")
                else:
                    print("Doctor ID not found.")
            except Exception as e:
                print(f"Error updating: {e}")
                
        elif choice == '5':
            target_id = input("Enter Doctor ID to delete: ").strip()
            rows = []
            deleted = False
            try:
                with open(DOCTORS_FILE, mode='r', encoding='utf-8') as file:
                    reader = csv.DictReader(file)
                    headers = reader.fieldnames
                    for row in reader:
                        if row['doctor_id'] == target_id:
                            deleted = True
                            continue
                        rows.append(row)
                
                if deleted:
                    with open(DOCTORS_FILE, mode='w', newline='', encoding='utf-8') as file:
                        writer = csv.DictWriter(file, fieldnames=headers)
                        writer.writeheader()
                        writer.writerows(rows)
                    print("Doctor deleted successfully!")
                else:
                    print("Doctor ID not found.")
            except Exception as e:
                print(f"Error deleting: {e}")
                
        elif choice == '6':
            break
        else:
            print("Invalid option. Choose between 1 and 6.")

# --- 3. SCHEDULE APPOINTMENT ---
def schedule_appointment():
    print("\n--- SCHEDULE APPOINTMENT ---")
    app_id = input("Enter Appointment ID (e.g., A001): ").strip()
    if id_exists(APPOINTMENTS_FILE, 'appointment_id', app_id):
        print("Error: Appointment ID already exists!")
        return
        
    patient_id = input("Enter Patient ID: ").strip()
    if not id_exists(PATIENTS_FILE, 'patient_id', patient_id):
        print("Error: Patient ID does not exist! Register patient first.")
        return
        
    doctor_id = input("Enter Doctor ID: ").strip()
    if not id_exists(DOCTORS_FILE, 'doctor_id', doctor_id):
        print("Error: Doctor ID does not exist! Register doctor first.")
        return
        
    date = input("Enter Date (YYYY-MM-DD): ").strip()
    time = input("Enter Time (HH:MM): ").strip()
    status = "Scheduled"
    
    try:
        with open(APPOINTMENTS_FILE, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([app_id, patient_id, doctor_id, date, time, status])
        print("Appointment scheduled successfully!")
    except Exception as e:
        print(f"Error saving appointment: {e}")

# --- 4. VIEW / SEARCH APPOINTMENTS ---
def view_appointments():
    while True:
        print("\n--- VIEW/SEARCH APPOINTMENTS ---")
        print("1. List All Appointments")
        print("2. Search Appointments by Date (YYYY-MM-DD)")
        print("3. Cancel/Delete an Appointment")
        print("4. Back to Main Menu")
        
        choice = input("Select an option (1-4): ").strip()
        
        if choice == '1':
            try:
                with open(APPOINTMENTS_FILE, mode='r', encoding='utf-8') as file:
                    reader = csv.DictReader(file)
                    print("\n--- ALL APPOINTMENTS ---")
                    count = 0
                    for row in reader:
                        count += 1
                        print(f"App ID: {row['appointment_id']} | Patient: {row['patient_id']} | Doctor: {row['doctor_id']} | Date: {row['date']} | Time: {row['time']} | Status: {row['status']}")
                    if count == 0:
                        print("No appointments found.")
            except Exception as e:
                print(f"Error reading file: {e}")
                
        elif choice == '2':
            target_date = input("Enter Date to search (YYYY-MM-DD): ").strip()
            found = False
            try:
                with open(APPOINTMENTS_FILE, mode='r', encoding='utf-8') as file:
                    reader = csv.DictReader(file)
                    print(f"\n--- APPOINTMENTS ON {target_date} ---")
                    for row in reader:
                        if row['date'] == target_date:
                            print(f"App ID: {row['appointment_id']} | Patient: {row['patient_id']} | Doctor: {row['doctor_id']} | Time: {row['time']} | Status: {row['status']}")
                            found = True
                if not found:
                    print("No appointments found for this date.")
            except Exception as e:
                print(f"Error searching: {e}")
                
        elif choice == '3':
            target_id = input("Enter Appointment ID to cancel: ").strip()
            rows = []
            deleted = False
            try:
                with open(APPOINTMENTS_FILE, mode='r', encoding='utf-8') as file:
                    reader = csv.DictReader(file)
                    headers = reader.fieldnames
                    for row in reader:
                        if row['appointment_id'] == target_id:
                            deleted = True
                            continue
                        rows.append(row)
                
                if deleted:
                    with open(APPOINTMENTS_FILE, mode='w', newline='', encoding='utf-8') as file:
                        writer = csv.DictWriter(file, fieldnames=headers)
                        writer.writeheader()
                        writer.writerows(rows)
                    print("Appointment canceled successfully!")
                else:
                    print("Appointment ID not found.")
            except Exception as e:
                print(f"Error canceling: {e}")
                
        elif choice == '4':
            break
        else:
            print("Invalid option. Choose between 1 and 4.")

# --- 5. VISIT RECORDS ---
def visit_records():
    while True:
        print("\n--- VISIT RECORDS ---")
        print("1. Add Visit Note")
        print("2. View Visits by Patient ID")
        print("3. Back to Main Menu")
        
        choice = input("Select an option (1-3): ").strip()
        
        if choice == '1':
            visit_id = input("Enter Visit ID (e.g., V001): ").strip()
            patient_id = input("Enter Patient ID: ").strip()
            if not id_exists(PATIENTS_FILE, 'patient_id', patient_id):
                print("Error: Patient ID does not exist!")
                continue
            doctor_id = input("Enter Doctor ID: ").strip()
            if not id_exists(DOCTORS_FILE, 'doctor_id', doctor_id):
                print("Error: Doctor ID does not exist!")
                continue
            visit_date = input("Enter Visit Date (YYYY-MM-DD): ").strip()
            notes = input("Enter Visit Reason / Administrative Note: ").strip()
            
            try:
                with open(VISITS_FILE, mode='a', newline='', encoding='utf-8') as file:
                    writer = csv.writer(file)
                    writer.writerow([visit_id, patient_id, doctor_id, visit_date, notes])
                print("Visit record added successfully!")
            except Exception as e:
                print(f"Error saving visit: {e}")
                
        elif choice == '2':
            target_patient = input("Enter Patient ID to view visits: ").strip()
            found = False
            try:
                with open(VISITS_FILE, mode='r', encoding='utf-8') as file:
                    reader = csv.DictReader(file)
                    print(f"\n--- VISITS FOR PATIENT {target_patient} ---")
                    for row in reader:
                        if row['patient_id'] == target_patient:
                            print(f"Visit ID: {row['visit_id']} | Doctor: {row['doctor_id']} | Date: {row['visit_date']} | Notes: {row['notes']}")
                            found = True
                if not found:
                    print("No visit records found for this patient.")
            except Exception as e:
                print(f"Error reading visits: {e}")
                
        elif choice == '3':
            break
        else:
            print("Invalid option. Choose between 1 and 3.")

# --- 6. PAYMENTS AND BALANCES ---
def payments_management():
    while True:
        print("\n--- PAYMENTS AND BALANCES ---")
        print("1. Record Payment / Bill")
        print("2. View All Payments and Balances")
        print("3. Back to Main Menu")
        
        choice = input("Select an option (1-3): ").strip()
        
        if choice == '1':
            payment_id = input("Enter Payment ID (e.g., Pay001): ").strip()
            patient_id = input("Enter Patient ID: ").strip()
            if not id_exists(PATIENTS_FILE, 'patient_id', patient_id):
                print("Error: Patient ID does not exist!")
                continue
            
            try:
                bill_amount = float(input("Enter Bill Amount: "))
                amount_paid = float(input("Enter Amount Paid: "))
                if bill_amount < 0 or amount_paid < 0:
                    print("Amounts cannot be negative.")
                    continue
            except ValueError:
                print("Invalid input! Please enter numbers for amounts.")
                continue
                
            balance = bill_amount - amount_paid
            
            try:
                with open(PAYMENTS_FILE, mode='a', newline='', encoding='utf-8') as file:
                    writer = csv.writer(file)
                    writer.writerow([payment_id, patient_id, bill_amount, amount_paid, balance])
                print(f"Payment recorded! Calculated Balance: {balance}")
            except Exception as e:
                print(f"Error saving payment: {e}")
                
        elif choice == '2':
            try:
                with open(PAYMENTS_FILE, mode='r', encoding='utf-8') as file:
                    reader = csv.DictReader(file)
                    print("\n--- PAYMENT RECORDS ---")
                    count = 0
                    for row in reader:
                        count += 1
                        print(f"Payment ID: {row['payment_id']} | Patient: {row['patient_id']} | Bill: ${row['bill_amount']} | Paid: ${row['amount_paid']} | Balance: ${row['balance']}")
                    if count == 0:
                        print("No payment records found.")
            except Exception as e:
                print(f"Error reading payments: {e}")
                
        elif choice == '3':
            break
        else:
            print("Invalid option. Choose between 1 and 3.")

# --- 7. BASIC REPORTS ---
def basic_reports():
    print("\n--- BASIC REPORTS ---")
    
    # Count patients
    patient_count = 0
    if os.path.exists(PATIENTS_FILE):
        try:
            with open(PATIENTS_FILE, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                patient_count = sum(1 for row in reader)
        except Exception:
            pass
            
    # Count doctors
    doctor_count = 0
    if os.path.exists(DOCTORS_FILE):
        try:
            with open(DOCTORS_FILE, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                doctor_count = sum(1 for row in reader)
        except Exception:
            pass
            
    print(f"Total Registered Patients: {patient_count}")
    print(f"Total Registered Doctors: {doctor_count}")
    
    # List appointments for a selected date
    target_date = input("\nEnter a date to list appointments (YYYY-MM-DD): ").strip()
    found = False
    if os.path.exists(APPOINTMENTS_FILE):
        try:
            with open(APPOINTMENTS_FILE, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                print(f"\n--- APPOINTMENTS ON {target_date} ---")
                for row in reader:
                    if row['date'] == target_date:
                        print(f"App ID: {row['appointment_id']} | Patient: {row['patient_id']} | Doctor: {row['doctor_id']} | Time: {row['time']}")
                        found = True
            if not found:
                print("No appointments found on this date.")
        except Exception as e:
            print(f"Error reading appointments: {e}")

# --- MAIN PROGRAM LOOP ---
def main():
    initialize_files()
    
    while True:
        print("\n==============================")
        print("   HOSPITAL MANAGEMENT SYSTEM ")
        print("==============================")
        print("1. Patient Management")
        print("2. Doctor Management")
        print("3. Schedule Appointment")
        print("4. View/Search Appointments")
        print("5. Visit Records")
        print("6. Payments and Balances")
        print("7. Basic Reports")
        print("8. Exit")
        
        choice = input("Select an option (1-8): ").strip()
        
        if choice == '1':
            patient_management()
        elif choice == '2':
            doctor_management()
        elif choice == '3':
            schedule_appointment()
        elif choice == '4':
            view_appointments()
        elif choice == '5':
            visit_records()
        elif choice == '6':
            payments_management()
        elif choice == '7':
            basic_reports()
        elif choice == '8':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice! Please select a number from 1 to 8.")

if __name__ == "__main__":
    main()