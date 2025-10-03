# 1. Create a patient tuple
patient = ("Alice", 34, "120/80", 72)

# 2. Access age and heart rate
print("Age:", patient[1], "Heart rate:", patient[3])

# 3. Why tuples?  --> They are immutable, ensuring vital records are not
# accidentally modified, preserving data integrity.

# 4. Update heart rate
patient_list = list(patient)
patient_list[3] = 75
patient = tuple(patient_list)
print("Updated patient tuple:", patient)

# 5. Tuple of 5 patients & extract names
patients = (
    ("Alice", 34, "120/80", 75),
    ("Bob", 45, "130/85", 70),
    ("Carol", 29, "110/70", 65),
    ("David", 52, "135/90", 78),
    ("Eve", 40, "125/80", 68)
)
names = [p[0] for p in patients]
print("All names:",names)