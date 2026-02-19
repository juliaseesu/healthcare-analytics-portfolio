-- Patients Table
CREATE TABLE patients (
   patient_id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    gender TEXT,
    blood_type TEXT
);

-- Admissions Table
CREATE TABLE admissions (
    admission_id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id INTEGER,
    hospital TEXT,
    doctor TEXT,
    admission_type TEXT,
    admission_date DATE,
    discharge_date DATE,
    length_of_stay INTEGER,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id)
);

-- Diagnoses Table
CREATE TABLE diagnoses (
    diagnosis_id INTEGER PRIMARY KEY AUTOINCREMENT,
    admission_id INTEGER,
    medical_condition TEXT,
    test_results TEXT,
    medication TEXT,
    FOREIGN KEY (admission_id) REFERENCES admissions(admission_id)
);

-- Billing Table
CREATE TABLE billing (
    billing_id INTEGER PRIMARY KEY AUTOINCREMENT,
    admission_id INTEGER,
    insurance_provider TEXT,
    billing_amount REAL,
    room_number INTEGER,
    high_cost_flag BOOLEAN,
    long_stay_flag BOOLEAN,
    FOREIGN KEY (admission_id) REFERENCES admissions(admission_id)
);
