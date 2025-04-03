# Importing all neccesary libraries
import copy
import pandas as pd
from faker import Faker
import random
from datetime import datetime, timedelta
import pandas as pd

fake = Faker()



# Inserting in user Table

# -------------- users.user_ids
user_ids = []

for i in range(1000):
    ids = 'U' + str(i+1)
    user_ids.append(ids)

# print(user_ids)



# ------------ users.name

users_name = []

# All Pharmcies names
pharmacy_names = [
    "Apex Health Solutions",
    "Beacon Pharmacy",
    "Blue Ridge Remedies",
    "Cardinal Care Pharmacy",
    "Cedar Creek Apothecary",
    "Centennial Wellness Center",
    "Charter Oak Pharmacy",
    "Clearview Rx",
    "Compass Point Pharmacy",
    "Cornerstone Health",
    "Crestview Pharmacy",
    "Diamond Drug Center",
    "Eagle Rock Pharmacy",
    "Emerald Coast Pharmacy",
    "Evergreen Wellness",
    "Fairview Pharmacy",
    "First Coast Remedies",
    "Forest Hill Pharmacy",
    "Gateway Health",
    "Golden Gate Pharmacy",
    "Grand Central Pharmacy",
    "Green Valley Apothecary",
    "Harbor View Pharmacy",
    "Heritage Health Center",
    "Highland Park Pharmacy",
    "Horizon Rx",
    "Ivy League Pharmacy",
    "Jasper Wellness",
    "Keystone Pharmacy",
    "Lakeview Pharmacy",
    "Liberty Drug Store",
    "Magnolia Health",
    "Maplewood Pharmacy",
    "Meadowbrook Pharmacy",
    "Midtown Pharmacy",
    "Mill Creek Apothecary",
    "Mountain View Pharmacy",
    "Northwood Pharmacy",
    "Oak Lane Pharmacy",
    "Ocean View Rx",
    "Pacific Coast Pharmacy",
    "Park Avenue Pharmacy",
    "Pine Ridge Wellness",
    "Pinnacle Health Center",
    "Plaza Pharmacy",
    "Redwood Pharmacy",
    "Riverbend Pharmacy",
    "Rock Creek Apothecary",
    "Rolling Hills Pharmacy",
    "Rosewood Pharmacy",
    "Seaside Pharmacy",
    "Shadow Creek Wellness",
    "Skyline Pharmacy",
    "South Beach Pharmacy",
    "Springfield Pharmacy",
    "Summit Health",
    "Sunnyside Pharmacy",
    "Sycamore Pharmacy",
    "The Balanced Rx",
    "The Care Collective",
    "The Health Emporium",
    "The Medicine Tree",
    "The Remedy Hub",
    "The Wellness Oasis",
    "Timberline Pharmacy",
    "Twin Peaks Pharmacy",
    "Valley View Pharmacy",
    "Vista Health Center",
    "Walnut Creek Pharmacy",
    "Waterfront Pharmacy",
    "Westwood Pharmacy",
    "Willow Creek Apothecary",
    "Windy Hill Pharmacy",
    "Woodland Pharmacy",
    "Zenith Wellness",
    "A+ Health Pharmacy",
    "Best Care Rx",
    "Complete Health Pharmacy",
    "Direct Rx Solutions",
    "Elite Wellness Center",
    "Family First Pharmacy",
    "Genuine Health",
    "Holistic Care Pharmacy",
    "Infinite Wellness",
    "Just Rx",
    "Keen Health Pharmacy",
    "LifeSource Pharmacy",
    "Maximum Health",
    "New Dawn Pharmacy",
    "Optimum Wellness",
    "Prime Care Pharmacy",
    "Quality Rx",
    "Reliant Health",
    "Superior Wellness",
    "True Health Pharmacy",
    "Ultimate Care Rx",
    "Vitality Pharmacy",
    "WellLife Center",
    "Xtra Care Pharmacy",
    "Your Best Health"
]

# Names of Customers and Delivery Persons
for i in range(899):
    u_name = fake.name()
    users_name.append(u_name)

users_name = pharmacy_names + users_name

# Adding the Admin name
users_name.insert(0, 'Vivek Karnakar')

# print(users_name)



# ------------ users.email

users_email = []

# Generating Fake email ids
for i in range(1000):
    first_half = users_name[i].replace(' ', '') 
    domain_name = fake.free_email_domain()

    email_add = f'{first_half}@{domain_name}'
    users_email.append(email_add)

# print(users_email)
# print(len(users_email))


# ----------- users.phone_numbers

users_phoneNumber = []

# Generating Fake phone numbers
for i in range(1000):
    phone_number = fake.phone_number()[0:15]
    users_phoneNumber.append(phone_number)

# print(users_phoneNumber)



# ----------------- users.user_types

user_types = []
customer = []
pharmacy = []
delivery_person = []

for i in range(100):
    pharmacy.append('Pharmacy')
    delivery_person.append('DeliveryPerson')

for i in range(799):
    customer.append('Customer')

user_types = pharmacy + delivery_person + customer
# print(len(user_types))

user_types.insert(0, 'Admin')

# print(user_types)
# print(len(user_types))



# ------------- users.address

user_address = []

for i in range(1000):
    address = fake.address()
    user_address.append(address)

# print(user_address)




# ----------- users.registered_on

# These are the registration date of pharmacies and delivery persons
company_partners = []

for i in range(201):
    company_partners.append(datetime(2024, 1, 1, 0, 0, 0))

# print(len(company_partners))

# Function to generate random dates :
def generate_random_date(start_date, end_date):
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    random_date = start_date + timedelta(days=random_days)
    return random_date

# Define the date range
start_date = datetime(2024, 1, 1)
end_date = datetime(2024, 12, 31)

# Generate 100 random dates
random_dates = [generate_random_date(start_date, end_date) for _ in range(799)]
random_dates = sorted(random_dates)

# Defining Hours and Minutes
def change_hours_mins(x):
    hours = random.randint(9, 18)
    minutes = random.randint(0, 59)
    return x.replace(hour = hours, minute = minutes)

registered_on = list(map(change_hours_mins, random_dates))
# print(len(registered_on))

registered_on = company_partners + registered_on

# print(registered_on)
# print(len(registered_on))

# Print the random dates
# for date in registered_on:
#     print(date.strftime('%Y-%m-%d %H:%M:%S'))





# ------------ Creating users table dataframe and exporting data to a csv file

users_df = pd.DataFrame({
    'user_id': user_ids,
    'name': users_name,
    'email': users_email,
    'phone_number': users_phoneNumber,
    'user_type': user_types,
    'address': user_address,
    'registered_on': registered_on
})

# Exporting users_df dataframe to a csv file

users_df.to_csv('users.csv', index = False)





# Inserting into Medications Table


# ----------- medication.medication_id

medication_ids = []

for i in range(310):
    ids = f'M{i + 1}'
    medication_ids.append(ids)

# print(medication_ids)
# print(len(medication_ids))




# ----------- medications.names

# Medicines names
medication_names = [
    'Paracetamol', 'Ibuprofen', 'Amoxicillin', 'Metformin', 'Atorvastatin',
    'Lisinopril', 'Amlodipine', 'Omeprazole', 'Albuterol', 'Simvastatin',
    'Losartan', 'Levothyroxine', 'Cetirizine', 'Furosemide', 'Fluoxetine',
    'Clopidogrel', 'Gabapentin', 'Hydrochlorothiazide', 'Montelukast', 'Prednisone',
    'Tramadol', 'Azithromycin', 'Ciprofloxacin', 'Pantoprazole', 'Aspirin',
    'Warfarin', 'Ranitidine', 'Carvedilol', 'Doxycycline', 'Sertraline',
    'Loratadine', 'Metoprolol', 'Zolpidem', 'Glipizide', 'Clonazepam',
    'Escitalopram', 'Lorazepam', 'Diazepam', 'Omeprazole', 'Oxycodone',
    'Meloxicam', 'Naproxen', 'Amiodarone', 'Cyclobenzaprine', 'Cephalexin',
    'Tamsulosin', 'Bupropion', 'Venlafaxine', 'Ezetimibe', 'Sulfamethoxazole',
    'Triamterene', 'Nitroglycerin', 'Allopurinol', 'Baclofen', 'Lantus',
    'Lamotrigine', 'Simvastatin', 'Amlodipine', 'Methotrexate', 'Duloxetine',
    'Lansoprazole', 'Lisinopril', 'Methocarbamol', 'Ondansetron', 'Phenytoin',
    'Plavix', 'Potassium Chloride', 'Pravastatin', 'Propranolol', 'Quetiapine',
    'Ramipril', 'Risperidone', 'Seroquel', 'Spironolactone', 'Suboxone',
    'Sulfasalazine', 'Synthroid', 'Tamoxifen', 'Trazodone', 'Valsartan',
    'Verapamil', 'Wellbutrin', 'Zolpidem', 'Advair', 'Alendronate',
    'Alprazolam', 'Amitriptyline', 'Aripiprazole', 'Atenolol', 'Avapro',
    'Benicar', 'Betamethasone', 'Bisoprolol', 'Buspirone', 'Captopril',
    'Carisoprodol', 'Cefadroxil', 'Cefixime', 'Cefuroxime', 'Celecoxib',
    'Clarithromycin', 'Clobetasol', 'Clonidine', 'Clozapine', 'Colchicine',
    'Cyclobenzaprine', 'Cyclosporine', 'Desloratadine', 'Desvenlafaxine', 'Dexamethasone',
    'Diclofenac', 'Digoxin', 'Diltiazem', 'Diphenhydramine', 'Divalproex',
    'Donepezil', 'Doxazosin', 'Drospirenone', 'Duloxetine', 'Enalapril',
    'Enoxaparin', 'Esomeprazole', 'Estradiol', 'Estrogen', 'Ethambutol',
    'Famotidine', 'Fentanyl', 'Ferrous Sulfate', 'Flomax', 'Folic Acid',
    'Fosamax', 'Gemfibrozil', 'Glyburide', 'Hydrochlorothiazide', 'Hydrocodone',
    'Hydrocortisone', 'Hydroxyzine', 'Imipramine', 'Indapamide', 'Indomethacin',
    'Insulin', 'Irbesartan', 'Isosorbide', 'Isotretinoin', 'Ketorolac',
    'Lansoprazole', 'Levofloxacin', 'Levothyroxine', 'Lidocaine', 'Liraglutide',
    'Loratadine', 'Losartan', 'Lovastatin', 'Lurasidone', 'Meloxicam',
    'Mesalamine', 'Metformin', 'Methadone', 'Methimazole', 'Methotrexate',
    'Metoclopramide', 'Metoprolol', 'Metronidazole', 'Minocycline', 'Mirtazapine',
    'Montelukast', 'Morphine', 'Mupirocin', 'Nabumetone', 'Naproxen',
    'Nebivolol', 'Niacin', 'Nifedipine', 'Nitrofurantoin', 'Norethindrone',
    'Nortriptyline', 'Olanzapine', 'Omeprazole', 'Ondansetron', 'Oxybutynin',
    'Oxycodone', 'Pantoprazole', 'Paroxetine', 'Penicillin', 'Phentermine',
    'Phenytoin', 'Pioglitazone', 'Pravastatin', 'Prednisone', 'Pregabalin',
    'Prochlorperazine', 'Promethazine', 'Propranolol', 'Quetiapine', 'Quinapril',
    'Rabeprazole', 'Raloxifene', 'Ramipril', 'Ranolazine', 'Ranitidine',
    'Repaglinide', 'Risperidone', 'Rivaroxaban', 'Rizatriptan', 'Rosuvastatin',
    'S-adenosylmethionine', 'Salmeterol', 'Saxagliptin', 'Secukinumab', 'Senna',
    'Sertraline', 'Sildenafil', 'Simvastatin', 'Sitagliptin', 'Sodium Bicarbonate',
    'Solifenacin', 'Spironolactone', 'Sulfasalazine', 'Sulfamethoxazole', 'Sumatriptan',
    'Tacrolimus', 'Tadalafil', 'Tamoxifen', 'Tamsulosin', 'Terazosin',
    'Terbinafine', 'Testosterone', 'Tetracycline', 'Tiotropium', 'Tizanidine',
    'Tobramycin', 'Tolterodine', 'Topiramate', 'Torsemide', 'Tramadol',
    'Trazodone', 'Triamcinolone', 'Triamterene', 'Trimethoprim', 'Valacyclovir',
    'Valproate', 'Valsartan', 'Venlafaxine', 'Verapamil', 'Vildagliptin',
    'Warfarin', 'Zaleplon', 'Zidovudine', 'Ziprasidone', 'Zoledronic Acid',
    'Zolmitriptan', 'Zolpidem', 'Zonisamide', 'Zoster Vaccine', 'Acyclovir',
    'Adapalene', 'Albuterol', 'Allopurinol', 'Alprazolam', 'Amantadine',
    'Amiodarone', 'Amitriptyline', 'Amlodipine', 'Amoxicillin', 'Amphetamine',
    'Anastrozole', 'Apixaban', 'Aripiprazole', 'Atazanavir', 'Atenolol',
    'Atomoxetine', 'Atorvastatin', 'Azathioprine', 'Azithromycin', 'Baclofen',
    'Beclomethasone', 'Benazepril', 'Benzonatate', 'Bicalutamide', 'Bisoprolol',
    'Brimonidine', 'Budesonide', 'Bumetanide', 'Bupropion', 'Buspirone',
    'Butalbital', 'Canagliflozin', 'Candesartan', 'Capecitabine', 'Captopril',
    'Carbamazepine', 'Carbidopa', 'Carisoprodol', 'Carvedilol', 'Cefdinir',
    'Cefprozil', 'Cefuroxime', 'Celecoxib', 'Cephalexin', 'Cetirizine',
    'Chloramphenicol', 'Chloroquine', 'Cholecalciferol', 'Cilostazol', 'Ciprofloxacin',
    'Citalopram', 'Clarithromycin', 'Clindamycin', 'Clobetasol', 'Clomiphene'
]

# print(len(medication_names))




# ----------------- medication.description

medication_descriptions = [
    "Pain reliever, fever reducer.",
    "Pain and inflammation reliever.",
    "Antibiotic.",
    "Diabetes medication.",
    "Cholesterol-lowering.",
    "Blood pressure medication.",
    "Blood pressure medication.",
    "Reduces stomach acid.",
    "Bronchodilator (for breathing).",
    "Cholesterol-lowering.",
    "Blood pressure medication.",
    "Thyroid hormone.",
    "Allergy relief.",
    "Diuretic (water pill).",
    "Antidepressant.",
    "Blood thinner.",
    "Nerve pain, seizures.",
    "Diuretic.",
    "Asthma, allergies.",
    "Steroid (anti-inflammatory).",
    "Pain reliever.",
    "Antibiotic.",
    "Antibiotic.",
    "Reduces stomach acid.",
    "Pain, fever, blood thinner.",
    "Blood thinner.",
    "Reduces stomach acid (less common now).",
    "Blood pressure, heart failure.",
    "Antibiotic.",
    "Antidepressant.",
    "Allergy relief.",
    "Blood pressure.",
    "Sleep aid.",
    "Diabetes medication.",
    "Anxiety, seizures.",
    "Antidepressant.",
    "Anxiety.",
    "Anxiety, seizures.",
    "Pain reliever.",
    "Pain, inflammation.",
    "Pain, inflammation.",
    "Heart rhythm.",
    "Muscle relaxant.",
    "Antibiotic.",
    "Prostate.",
    "Antidepressant, smoking cessation.",
    "Antidepressant.",
    "Cholesterol-lowering.",
    "Antibiotic.",
    "Diuretic.",
    "Chest pain.",
    "Gout.",
    "Muscle relaxant.",
    "Long-acting insulin.",
    "Seizures, mood stabilizer.",
    "Cancer, autoimmune.",
    "Antidepressant, pain.",
    "Reduces stomach acid.",
    "Muscle relaxant.",
    "Nausea, vomiting.",
    "Seizures.",
    "Blood thinner.",
    "Potassium supplement.",
    "Cholesterol-lowering.",
    "Blood pressure, anxiety.",
    "Antipsychotic.",
    "Blood pressure.",
    "Antipsychotic.",
    "Antipsychotic.",
    "Diuretic.",
    "Opioid dependence.",
    "Inflammation.",
    "Thyroid hormone.",
    "Breast cancer.",
    "Antidepressant, sleep.",
    "Blood pressure.",
    "Blood pressure, heart.",
    "Antidepressant.",
    "Asthma, COPD.",
    "Osteoporosis.",
    "Anxiety.",
    "Antidepressant, pain.",
    "Antipsychotic.",
    "Blood pressure.",
    "Blood pressure.",
    "Blood pressure.",
    "Steroid.",
    "Blood pressure.",
    "Anxiety.",
    "Blood pressure.",
    "Muscle relaxant.",
    "Antibiotic.",
    "Antibiotic.",
    "Antibiotic.",
    "Pain, inflammation.",
    "Antibiotic.",
    "Steroid (topical).",
    "Blood pressure.",
    "Antipsychotic.",
    "Gout.",
    "Immunosuppressant.",
    "Allergy relief.",
    "Antidepressant.",
    "Steroid.",
    "Pain, inflammation.",
    "Heart.",
    "Blood pressure, heart.",
    "Allergy, sleep.",
    "Seizures, mood.",
    "Alzheimer's.",
    "Prostate, blood pressure.",
    "Birth control.",
    "Blood pressure.",
    "Blood thinner.",
    "Reduces stomach acid.",
    "Hormone replacement.",
    "Hormone replacement.",
    "Antibiotic (TB).",
    "Reduces stomach acid.",
    "Pain reliever.",
    "Iron supplement.",
    "Prostate.",
    "Vitamin.",
    "Osteoporosis.",
    "Cholesterol.",
    "Diabetes.",
    "Pain reliever.",
    "Steroid.",
    "Anxiety, allergy.",
    "Antidepressant.",
    "Diuretic.",
    "Pain, inflammation.",
    "Diabetes.",
    "Blood pressure.",
    "Chest pain.",
    "Acne.",
    "Pain.",
    "Antibiotic.",
    "Numbing.",
    "Diabetes.",
    "Cholesterol.",
    "Antipsychotic.",
    "Inflammatory bowel disease.",
    "Pain, opioid dependence.",
    "Thyroid.",
    "Nausea, stomach emptying.",
    "Antibiotic.",
    "Antibiotic.",
    "Antidepressant.",
    "Pain reliever.",
    "Antibiotic (topical).",
    "Pain, inflammation.",
    "Blood pressure.",
    "Cholesterol.",
    "Blood pressure.",
    "Antibiotic.",
    "Birth control.",
    "Antidepressant.",
    "Antipsychotic.",
    "Overactive bladder.",
    "Antidepressant.",
    "Antibiotic.",
    "Weight loss.",
    "Diabetes.",
    "Nausea, vomiting.",
    "Antipsychotic.",
    "Blood pressure.",
    "Reduces stomach acid.",
    "Blood pressure.",
    "Antiarrhythmic.",
    "Blood thinner.",
    "Headaches.",
    "Cholesterol-lowering.",
    "Supplement.",
    "Bronchodilator.",
    "Diabetes.",
    "Supplement.",
    "Overactive bladder.",
    "Inflammation.",
    "Antibiotic.",
    "Headaches.",
    "Immunosuppressant.",
    "Erectile dysfunction.",
    "Breast cancer.",
    "Prostate.",
    "Prostate.",
    "Antifungal.",
    "Hormone replacement.",
    "Antibiotic.",
    "Bronchodilator.",
    "Muscle relaxant.",
    "Antibiotic.",
    "Overactive bladder.",
    "Seizures.",
    "Diuretic.",
    "Pain reliever.",
    "Antidepressant, sleep.",
    "Steroid.",
    "Diuretic.",
    "Antibiotic.",
    "Antiviral.",
    "Seizures, mood.",
    "Blood pressure.",
    "Antidepressant.",
    "Blood pressure, heart.",
    "Diabetes.",
    "Blood thinner.",
    "Sleep aid.",
    "Antiviral.",
    "Antipsychotic.",
    "Osteoporosis.",
    "Headaches.",
    "Sleep aid.",
    "Seizures.",
    "Vaccine.",
    "Antiviral.",
    "Acne.",
    "Bronchodilator.",
    "Gout.",
    "Anxiety.",
    "Antiviral.",
    "Heart rhythm.",
    "Antidepressant, pain.",
    "Blood pressure medication.",
    "Antibiotic.",
    "Stimulant.",
    "Breast cancer.",
    "Blood thinner.",
    "Antipsychotic.",
    "Antiviral.",
    "Blood pressure.",
    "ADHD.",
    "Cholesterol-lowering.",
    "Immunosuppressant.",
    "Antibiotic.",
    "Muscle relaxant.",
    "Steroid.",
    "Blood pressure.",
    "Cough suppressant.",
    "Prostate cancer.",
    "Blood pressure.",
    "Eye drops.",
    "Steroid.",
    "Diuretic.",
    "Antidepressant, smoking cessation.",
    "Anxiety.",
    "Headaches.",
    "Diabetes.",
    "Blood pressure.",
    "Cancer.",
    "Blood pressure.",
    "Muscle relaxant.",
    "Heart rhythm.",
    "Antibiotic.",
    "Antibiotic.",
    "Antibiotic.",
    "Pain, inflammation.",
    "Antibiotic.",
    "Steroid (topical).",
    "Contraception.",
    "Antipsychotic.",
    "Gout.",
    "Immunosuppressant.",
    "Allergy relief.",
    "Antidepressant.",
    "Steroid.",
    "Pain, inflammation.",
    "Heart.",
    "Blood pressure, heart.",
    "Allergy, sleep.",
    "Seizures, mood.",
    "Alzheimer's.",
    "Prostate, blood pressure.",
    "Contraception.",
    "Blood pressure.",
    "Blood thinner.",
    "Reduces stomach acid.",
    "Hormone replacement.",
    "Hormone replacement.",
    "Antibiotic (TB).",
    "Reduces stomach acid.",
    "Pain reliever.",
    "Iron supplement.",
    "Prostate.",
    "Vitamin.",
    "Osteoporosis.",
    "Cholesterol.",
    "Diabetes.",
    "Pain reliever.",
    "Steroid.",
    "Anxiety, allergy.",
    "Antidepressant.",
    "Diuretic.",
    "Pain, inflammation.",
    "Hormone replacement.",
    "Antibiotic (TB).",
    "Reduces stomach acid.",
    "Pain reliever.",
    "Iron supplement.",
    "Prostate.",
    "Vitamin.",
    "Osteoporosis.",
    "Cholesterol.",
    "Diabetes.",
    "Pain reliever.",
    "Steroid.",
    "Anxiety, allergy.",
    "Antidepressant.",
    "Diuretic.",
    "Pain, inflammation."]

# print(len(medication_descriptions))



#  ------------------ medication.categories

medication_categories = [
    "Analgesics (Pain relievers)",
    "Opioid Analgesics",
    "NSAIDs (Nonsteroidal Anti-inflammatory Drugs)",
    "Antibiotics",
    "Penicillins",
    "Macrolides",
    "Fluoroquinolones",
    "Tetracyclines",
    "Cardiovascular Medications",
    "Antihypertensives",
    "ACE Inhibitors",
    "ARBs (Angiotensin II Receptor Blockers)",
    "Calcium Channel Blockers",
    "Beta-Blockers",
    "Diuretics",
    "Statins",
    "Antiarrhythmics",
    "Antianginals",
    "Antiplatelets",
    "Anticoagulants",
    "Central Nervous System (CNS) Medications",
    "Antidepressants",
    "SSRIs (Selective Serotonin Reuptake Inhibitors)",
    "SNRIs (Serotonin-Norepinephrine Reuptake Inhibitors)",
    "Antipsychotics",
    "Anticonvulsants/Antiepileptics",
    "Anxiolytics",
    "Sedative-Hypnotics",
    "Muscle Relaxants",
    "Endocrine Medications",
    "Thyroid Hormones",
    "Antidiabetics",
    "Gastrointestinal Medications",
    "Proton Pump Inhibitors (PPIs)",
    "H2 Receptor Antagonists",
    "Antiemetics",
    "Respiratory Medications",
    "Bronchodilators",
    "Leukotriene Receptor Antagonists",
    "Corticosteroids (Inhaled)",
    "Allergy Medications",
    "Antihistamines",
    "Dermatological Medications",
    "Topical Corticosteroids",
    "Immunosuppressants",
    "Antivirals",
    "Antifungals",
    "Vitamins and Supplements",
    "Bone Health Medications",
    "Weight Loss Medications",
    "Urinary Medications",
    "Herbal Remedies",
    "Vaccines",
    "Analgesics (Pain relievers)",
    "Opioid Analgesics",
    "NSAIDs (Nonsteroidal Anti-inflammatory Drugs)",
    "Antibiotics",
    "Penicillins",
    "Macrolides",
    "Fluoroquinolones",
    "Tetracyclines",
    "Cardiovascular Medications",
    "Antihypertensives",
    "ACE Inhibitors",
    "ARBs (Angiotensin II Receptor Blockers)",
    "Calcium Channel Blockers",
    "Beta-Blockers",
    "Diuretics",
    "Statins",
    "Antiarrhythmics",
    "Antianginals",
    "Antiplatelets",
    "Anticoagulants",
    "Central Nervous System (CNS) Medications",
    "Antidepressants",
    "SSRIs (Selective Serotonin Reuptake Inhibitors)",
    "SNRIs (Serotonin-Norepinephrine Reuptake Inhibitors)",
    "Antipsychotics",
    "Anticonvulsants/Antiepileptics",
    "Anxiolytics",
    "Sedative-Hypnotics",
    "Muscle Relaxants",
    "Endocrine Medications",
    "Thyroid Hormones",
    "Antidiabetics",
    "Gastrointestinal Medications",
    "Proton Pump Inhibitors (PPIs)",
    "H2 Receptor Antagonists",
    "Antiemetics",
    "Respiratory Medications",
    "Bronchodilators",
    "Leukotriene Receptor Antagonists",
    "Corticosteroids (Inhaled)",
    "Allergy Medications",
    "Antihistamines",
    "Dermatological Medications",
    "Topical Corticosteroids",
    "Immunosuppressants",
    "Antivirals",
    "Antifungals",
    "Vitamins and Supplements",
    "Bone Health Medications",
    "Weight Loss Medications",
    "Urinary Medications",
    "Herbal Remedies",
    "Vaccines",
    "Analgesics (Pain relievers)",
    "Opioid Analgesics",
    "NSAIDs (Nonsteroidal Anti-inflammatory Drugs)",
    "Antibiotics",
    "Penicillins",
    "Macrolides",
    "Fluoroquinolones",
    "Tetracyclines",
    "Cardiovascular Medications",
    "Antihypertensives",
    "ACE Inhibitors",
    "ARBs (Angiotensin II Receptor Blockers)",
    "Calcium Channel Blockers",
    "Beta-Blockers",
    "Diuretics",
    "Statins",
    "Antiarrhythmics",
    "Antianginals",
    "Antiplatelets",
    "Anticoagulants",
    "Central Nervous System (CNS) Medications",
    "Antidepressants",
    "SSRIs (Selective Serotonin Reuptake Inhibitors)",
    "SNRIs (Serotonin-Norepinephrine Reuptake Inhibitors)",
    "Antipsychotics",
    "Anticonvulsants/Antiepileptics",
    "Anxiolytics",
    "Sedative-Hypnotics",
    "Muscle Relaxants",
    "Endocrine Medications",
    "Thyroid Hormones",
    "Antidiabetics",
    "Gastrointestinal Medications",
    "Proton Pump Inhibitors (PPIs)",
    "H2 Receptor Antagonists",
    "Antiemetics",
    "Respiratory Medications",
    "Bronchodilators",
    "Leukotriene Receptor Antagonists",
    "Corticosteroids (Inhaled)",
    "Allergy Medications",
    "Antihistamines",
    "Dermatological Medications",
    "Topical Corticosteroids",
    "Immunosuppressants",
    "Antivirals",
    "Antifungals",
    "Vitamins and Supplements",
    "Bone Health Medications",
    "Weight Loss Medications",
    "Urinary Medications",
    "Herbal Remedies",
    "Vaccines",
    "Analgesics (Pain relievers)",
    "Opioid Analgesics",
    "NSAIDs (Nonsteroidal Anti-inflammatory Drugs)",
    "Antibiotics",
    "Penicillins",
    "Macrolides",
    "Fluoroquinolones",
    "Tetracyclines",
    "Cardiovascular Medications",
    "Antihypertensives",
    "ACE Inhibitors",
    "ARBs (Angiotensin II Receptor Blockers)",
    "Calcium Channel Blockers",
    "Beta-Blockers",
    "Diuretics",
    "Statins",
    "Antiarrhythmics",
    "Antianginals",
    "Antiplatelets",
    "Anticoagulants",
    "Central Nervous System (CNS) Medications",
    "Antidepressants",
    "SSRIs (Selective Serotonin Reuptake Inhibitors)",
    "SNRIs (Serotonin-Norepinephrine Reuptake Inhibitors)",
    "Antipsychotics",
    "Anticonvulsants/Antiepileptics",
    "Anxiolytics",
    "Sedative-Hypnotics",
    "Muscle Relaxants",
    "Endocrine Medications",
    "Thyroid Hormones",
    "Antidiabetics",
    "Gastrointestinal Medications",
    "Proton Pump Inhibitors (PPIs)",
    "H2 Receptor Antagonists",
    "Antiemetics",
    "Respiratory Medications",
    "Bronchodilators",
    "Leukotriene Receptor Antagonists",
    "Corticosteroids (Inhaled)",
    "Allergy Medications",
    "Antihistamines",
    "Dermatological Medications",
    "Topical Corticosteroids",
    "Immunosuppressants",
    "Antivirals",
    "Antifungals",
    "Vitamins and Supplements",
    "Bone Health Medications",
    "Weight Loss Medications",
    "Urinary Medications",
    "Herbal Remedies",
    "Vaccines",
    "Analgesics (Pain relievers)",
    "Opioid Analgesics",
    "NSAIDs (Nonsteroidal Anti-inflammatory Drugs)",
    "Antibiotics",
    "Penicillins",
    "Macrolides",
    "Fluoroquinolones",
    "Tetracyclines",
    "Cardiovascular Medications",
    "Antihypertensives",
    "ACE Inhibitors",
    "ARBs (Angiotensin II Receptor Blockers)",
    "Calcium Channel Blockers",
    "Beta-Blockers",
    "Diuretics",
    "Statins",
    "Antiarrhythmics",
    "Antianginals",
    "Antiplatelets",
    "Anticoagulants",
    "Central Nervous System (CNS) Medications",
    "Antidepressants",
    "SSRIs (Selective Serotonin Reuptake Inhibitors)",
    "SNRIs (Serotonin-Norepinephrine Reuptake Inhibitors)",
    "Antipsychotics",
    "Anticonvulsants/Antiepileptics",
    "Anxiolytics",
    "Sedative-Hypnotics",
    "Muscle Relaxants",
    "Endocrine Medications",
    "Thyroid Hormones",
    "Antidiabetics",
    "Gastrointestinal Medications",
    "Proton Pump Inhibitors (PPIs)",
    "H2 Receptor Antagonists",
    "Antiemetics",
    "Respiratory Medications",
    "Bronchodilators",
    "Leukotriene Receptor Antagonists",
    "Corticosteroids (Inhaled)",
    "Allergy Medications",
    "Antihistamines",
    "Dermatological Medications",
    "Topical Corticosteroids",
    "Immunosuppressants",
    "Antivirals",
    "Antifungals",
    "Vitamins and Supplements",
    "Bone Health Medications",
    "Weight Loss Medications",
    "Urinary Medications",
    "Herbal Remedies",
    "Vaccines",
    "Analgesics (Pain relievers)",
    "Opioid Analgesics",
    "NSAIDs (Nonsteroidal Anti-inflammatory Drugs)",
    "Antibiotics",
    "Penicillins",
    "Macrolides",
    "Fluoroquinolones",
    "Tetracyclines",
    "Cardiovascular Medications",
    "Antihypertensives",
    "ACE Inhibitors",
    "ARBs (Angiotensin II Receptor Blockers)",
    "Calcium Channel Blockers",
    "Beta-Blockers",
    "Diuretics",
    "Statins",
    "Antiarrhythmics",
    "Antianginals",
    "Antiplatelets",
    "Anticoagulants",
    "Central Nervous System (CNS) Medications",
    "Antidepressants",
    "SSRIs (Selective Serotonin Reuptake Inhibitors)",
    "SNRIs (Serotonin-Norepinephrine Reuptake Inhibitors)",
    "Antipsychotics",
    "Anticonvulsants/Antiepileptics",
    "Anxiolytics",
    "Sedative-Hypnotics",
    "Muscle Relaxants",
    "Endocrine Medications",
    "Thyroid Hormones",
    "Antidiabetics",
    "Gastrointestinal Medications",
    "Proton Pump Inhibitors (PPIs)",
    "H2 Receptor Antagonists",
    "Antiemetics",
    "Respiratory Medications",
    "Bronchodilators",
    "Leukotriene Receptor Antagonists",
    "Corticosteroids (Inhaled)",
    "Allergy Medications",
    "Antihistamines",
    "Dermatological Medications",
    "Topical Corticosteroids",
    "Immunosuppressants"
]

random.shuffle(medication_categories)

# print(len(medication_categories))




# ------------ medications.price

medication_price = []

for i in range(310):
    price = random.uniform(278, 5000)
    medication_price.append(round(price, 2))

# print(medication_price)





# -------------- mediciation.quantity

medication_quantity = []

for i in range(310):
    quantity = random.randint(10, 389)
    medication_quantity.append(quantity)

# print(medication_quantity)




# --------------- medications.prescription

prescription_required = []

for i in range(310):
    num = random.randint(0, 1)
    prescription_required.append(num)

# print(prescription_required)




# ------------ Creating medications table dataframe and exporting data to a csv file

medication_df = pd.DataFrame({
    'medication_id': medication_ids,
    'name': medication_names,
    'description': medication_descriptions,
    'price': medication_price,
    'stock_quantity': medication_quantity,
    'category': medication_categories,
    'prescription_required': prescription_required
})

# Exporting medication_df to a csv file

medication_df.to_csv('medications.csv', index = False)






# ------ Inserting into orders table

# -------- orders.order_id

order_id = []

for i in range(1000):
    ids = f'Ord{i + 1}'
    order_id.append(ids)

# print(order_id)




# ---------- orders.phamacy_id

pharmacy_id = []

for i in range(1000):
    num = random.randint(2, 101)
    ids = f'U{num}'
    pharmacy_id.append(ids)

# print(pharmacy_id)




# --------- orders.customer_id

customer_id = []

for i in range(1000):
    num = random.randint(202, 1000)
    ids = f'U{num}'
    customer_id.append(ids)

# print(customer_id)




# -------- orders.order_date

order_date = []

for i in range(1000):
    dates = generate_random_date(start_date, end_date)
    dates = change_hours_mins(dates)
    order_date.append(dates)

order_date = sorted(order_date)

# print(order_date)




# ------------ orders.order_status

status = [ 'Pending', 'Processed', 'Shipped', 'Delivered', 'Cancelled']
starting_930 = []
cancelled_50 = []
remianing_60 = []

for i in range(890):
    starting_930.append('Delivered')

for i in range(50):
    cancelled_50.append('Cancelled')

for i in range(60):
    choice = random.choice(status)
    remianing_60.append(choice)

order_status = starting_930 + cancelled_50
random.shuffle(order_status)
order_status = order_status + remianing_60

# print(order_status)
# print(len(order_status))




# ------------- orders.payment_status

payment_status = []

choice = ['Completed', 'Pending']
for i in order_status:
    if i == 'Delivered':
        payment_status.append('Completed')
    elif i == 'Cancelled':
        payment_status.append('Refunded')
    else:
        pmt_sts = random.choice(choice)
        payment_status.append(pmt_sts)

# print(payment_status)




# ----------- orders.delivery_address

orders_delivery_address = []

for i in range(1000):
    address = fake.address()
    orders_delivery_address.append(address)




# ------------ Creating orders table dataframe and exporting data to a csv file

orders_df = pd.DataFrame({
    'order_id': order_id,
    'customer_id': customer_id,
    'pharmacy_id': pharmacy_id,
    'order_status': order_status,
    'order_date': order_date,
    'delivery_address': orders_delivery_address,
    'payment_status': payment_status
})

# Exporting medication_df to a csv file

orders_df.to_csv('orders.csv', index = False)






# Inserting into orders details Table

# ----------- order_details.order_details_id

order_detail_id = []
order_details_OID = []

for i in order_id:
    num_of_order_details = random.randint(1,3)
    for j in range(num_of_order_details):
        order_details_OID.append(i)
        order_detail_id.append(f'{i}_{j + 1}')

# print(order_detail_id)
# print(order_details_OID)
# print(len(order_details_OID))
# print(len(order_detail_id))




# ----------- order_details.medications_id

OD_medication_id = []

for i in range(len(order_detail_id)):
    medicine = random.choice(medication_ids)
    OD_medication_id.append(medicine)

# print(OD_medication_id)
# print(len(OD_medication_id))




# ------------- order_details.quantity

OD_quantiy = []

for i in range(len(order_detail_id)):
    quantity = random.choice([1, 2, 3, 4, 5])
    OD_quantiy.append(quantity)

# print(OD_quantiy)
# print(len(OD_quantiy))





# ---------------- order_detail.unit_price

OD_unit_price = []

for i in OD_medication_id:
    idx = medication_ids.index(i)
    OD_unit_price.append(medication_price[idx])

# print(OD_unit_price)
# print(len(OD_unit_price))




# ----------- order_details.total_price

OD_total_price = []

OD_total_price = [a * b for a, b in zip(OD_unit_price, OD_quantiy)]

# print(OD_total_price)
# print(len(OD_total_price))





# ------------ Creating order details table dataframe and exporting data to a csv file

order_detail_df = pd.DataFrame({
    'order_detail_id': order_detail_id,
    'order_id': order_details_OID,
    'medication_id': OD_medication_id,
    'quantity': OD_quantiy,
    'unit_price': OD_unit_price,
    'total_price': OD_total_price
})

# Exporting medication_df to a csv file

order_detail_df.to_csv('order_details.csv', index = False)






# --------- Inserting into payments Table

# ----------  payments.payment_id 

payment_id = []

for i in range(1000):
    ids = f'PM{i}'
    payment_id.append(ids)




# --------------- payment.order_id

payments_OID = []
payments_OID = copy.deepcopy(order_id)





# ---------------- payments.amount


payments_amount = []

df = pd.DataFrame({
    'Order_id': order_details_OID,
    'Amt': OD_total_price
})

ser = df.groupby('Order_id')['Amt'].sum()
payments_amount = ser.tolist()

# print(payments_amount)
# print(len(payments_amount))




# ------------ payments.payment_date

payment_date = []

def paymentDate(rows):

    num = random.randint(0,7)

    if rows['payment_status'] == 'Completed' or rows['payment_status'] == 'Refunded':
        order_date = rows['order_date']
        order_date = order_date.to_pydatetime()
        return order_date + timedelta(days = num)
    else:
        return 'NULL'


df = pd.DataFrame({
    'order_date': order_date,
    'payment_status': payment_status
})

df['payment_date'] = df.apply(paymentDate ,axis = 1)

# print(df.tail(20))

payment_date = df['payment_date'].tolist()
print(len(payment_date))





# ---------- payments.payment_method

payment_method = []
types_of_payment_method = ['Credit Card', 'Debit Card', 'Wallet', 'Cash']

for i in payment_status:
    if i != 'Pending':
        method = random.choice(types_of_payment_method)
        payment_method.append(method)
    else:
        payment_method.append('NULL')

# print(payment_method)
# print(len(payment_method))




# ------------ payments.payment_status

payments_payment_status = copy.deepcopy(payment_status)
# print(payments_payment_status)
# print(len(payments_payment_status))







# ------------ Creating payments table dataframe and exporting data to a csv file

payment_df = pd.DataFrame({
    'payment_id': payment_id,
    'order_id': payments_OID,
    'amount': payments_amount,
    'payment_date': payment_date,
    'payment_method': payment_method,
    'payment_status': payments_payment_status
})

# Exporting medication_df to a csv file

payment_df.to_csv('payments.csv', index = False)







# ---------------- Inserting into Feedback Table

# Comments for 1 ratings
rating_1_comments = [
    "Delivery was late, and the medicines were not properly packaged.",
    "I did not receive all the items I ordered.",
    "The delivery person was rude and unprofessional.",
    "Medicines were damaged during delivery.",
    "Very poor service, I am not satisfied at all.",
    "The website was not user-friendly, and the ordering process was complicated.",
    "I had to call customer service multiple times to resolve issues.",
    "There were no updates provided about the delivery status.",
    "The wrong medicines were delivered to me.",
    "The delivery was delayed, and no explanation was given."
]

# Comments for 2 ratings
rating_2_comments = [
    "Delivery was late, but at least the medicines were intact.",
    "The website needs improvement; it was challenging to navigate.",
    "Customer service was slow to respond to my queries.",
    "The delivery packaging was subpar.",
    "Medicines were out of stock, causing a delay in delivery.",
    "The delivery person arrived much later than the estimated time.",
    "Communication about the delivery status was lacking.",
    "The ordering process was tedious and time-consuming.",
    "My delivery was incomplete, missing some items.",
    "Overall experience was below average."
]

# Comments for 3 ratings
rating_3_comments = [
    "The delivery was on time, but packaging could be better.",
    "The website is functional but could use some updates for better usability.",
    "Customer service was helpful, but the response time was slow.",
    "Medicines arrived in good condition, but the packaging was not very secure.",
    "Delivery was late, but customer service resolved the issue.",
    "The delivery person was polite and professional.",
    "Ordering process was straightforward, but some items were out of stock.",
    "Communication about delivery status was adequate but could be improved.",
    "Medicines were delivered as ordered, but the packaging could be improved.",
    "Overall experience was average, with room for improvement."
]

# Comments for 4 ratings
rating_4_comments = [
    "Delivery was on time, and the medicines were well-packaged.",
    "The website is easy to use and navigate.",
    "Customer service was prompt and helpful.",
    "Medicines arrived in excellent condition.",
    "Delivery was delayed slightly, but communication was clear.",
    "The delivery person was courteous and professional.",
    "Ordering process was smooth and hassle-free.",
    "Updates about delivery status were timely and accurate.",
    "Medicines were delivered as ordered, and the packaging was secure.",
    "Overall experience was good, with minor room for improvement."
]

# Comments for 5 ratings
rating_5_comments = [
    "Delivery was super fast, and the medicines were perfectly packaged.",
    "The website is very user-friendly and easy to navigate.",
    "Excellent customer service, very prompt and helpful.",
    "Medicines arrived in perfect condition and on time.",
    "Delivery was exactly as scheduled, with great communication.",
    "The delivery person was very polite and professional.",
    "Ordering process was seamless and quick.",
    "I received timely updates about my delivery status.",
    "Medicines were delivered accurately and securely.",
    "Overall, an outstanding experience! Highly recommended."
]




# ---------- feedback.feedback_id

feedback_id = []

for i in range(1000):
    ids = f'FB{i + 1}'
    feedback_id.append(ids)

# print(feedback_id)




# ---------- feedback.order_id

feedback_order_id = copy.deepcopy(order_id)
# print(feedback_order_id)




# ---------- feedback.user_id

feedback_user_id = copy.deepcopy(customer_id)
# print(feedback_order_id)





# ---------- feedback.ratings

feedback_ratings = []
for i in range(1000):
    rating = random.randint(1, 5)
    feedback_ratings.append(rating)

# print(feedback_ratings)




# ----------- feedback.comments

feedback_comments = []

for i in feedback_ratings:
    if i == 1:
        comment = random.choice(rating_1_comments)
        feedback_comments.append(comment)
    elif i == 2:
        comment = random.choice(rating_2_comments)
        feedback_comments.append(comment)
    elif i == 3:
        comment = random.choice(rating_3_comments)
        feedback_comments.append(comment)
    elif i == 4:
        comment = random.choice(rating_4_comments)
        feedback_comments.append(comment)
    else:
        comment = random.choice(rating_5_comments)
        feedback_comments.append(comment)

# print(feedback_comments)






# ------------ Creating feedback table dataframe and exporting data to a csv file

feedback_df = pd.DataFrame({
    'feedback_id': feedback_id,
    'order_id': feedback_order_id,
    'user_id': feedback_user_id,
    'rating': feedback_ratings,
    'comments': feedback_comments
})

# Exporting medication_df to a csv file

feedback_df.to_csv('feedback.csv', index = False)







# ------------ Inserting into Deliveries Table


# ------------ deliveries.delivery_id

delivery_id = []

for i in range(1000):
    ids = f'DEL{i+1}'
    delivery_id.append(ids)

# print(delivery_id)




# ----------- deliveries.order_id

delivery_order_id = copy.deepcopy(order_id)
# print(delivery_order_id)




# ----------- deliveries.person_id

delivery_person_id = []

delivery_person_userids = user_ids[101: 201]
# print(delivery_person_userids)
# print(len(delivery_person_userids))

for i in range(1000):
    delivery_person = random.choice(delivery_person_userids)
    delivery_person_id.append(delivery_person)

# print(delivery_person_id)




# ---------------- deliveries.delivery_status

delivery_status = []

for i in order_status:
    if i == 'Delivered':
        delivery_status.append('Delivered')
    elif i == 'Cancelled':
        delivery_status.append('NULL')
    else:
        delivery_status.append('Pending')

# print(delivery_status)
# print(len(delivery_status))






# ------------- deliveries.delivery_date

delivery_date = []

number_of_days = random.randint(1,3)
for i in order_date:
    del_date = i + timedelta(days = number_of_days)
    delivery_date.append(del_date)

for i in range(1000):
    if delivery_status[i] != 'Delivered':
        delivery_date[i] = 'NULL'


# print(delivery_date)
# print(len(delivery_date))






# ------------ Creating deliveries table dataframe and exporting data to a csv file

deliveries_df = pd.DataFrame({
    'delivery_id': delivery_id,
    'order_id': delivery_order_id,
    'delivery_person_id': delivery_person_id,
    'delivery_status': delivery_status,
    'delivery_date': delivery_date
})

# Exporting medication_df to a csv file

deliveries_df.to_csv('deliveries.csv', index = False)

