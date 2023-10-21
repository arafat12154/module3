gender = input("Enter your biological gender (male or female): ").lower()
hemoglobin_value = float(input("Enter your hemoglobin value (g/l): "))
if gender == "female":
    normal_range = (117, 155)
elif gender == "male":
    normal_range = (134, 167)
else:
    print("Error: Invalid gender input. Please enter 'male' or 'female'.")
    exit()
if hemoglobin_value < normal_range[0]:
    print(f"Your hemoglobin value is low for a {gender}.")
elif normal_range[0] <= hemoglobin_value <= normal_range[1]:
    print(f"Your hemoglobin value is normal for a {gender}.")
else:
    print(f"Your hemoglobin value is high for a {gender}.")
