# HEIGHT, WEIGHT & BMI CALCULATOR

human_input = input("Do you want to calculate 'Height', 'Weight' or 'BMI'?: ")

# Height calculation
if human_input == "Height" or human_input == "height":
    height = int(input("Enter your height: "))
    convert_unit_height = input("Did you enter your height in 'm' or 'cm'?: ")

    if (
        convert_unit_height == "cm"
        or convert_unit_height == "CM"
        or convert_unit_height == "Cm"
        or convert_unit_height == "cM"
    ):
        converted_height_cm = height / 100
        print(f"Your height in metres is {converted_height_cm}m.")

    elif convert_unit_height == "m" or convert_unit_height == "M":
        converted_height_m = height * 100
        print(f"Your height in centimetres is {converted_height_m}cm.")

    else:
        print("Error: Invalid unit.")

# Weight calculation
elif human_input == "Weight" or human_input == "weight":
    weight = int(input("Enter your weight: "))
    convert_unit_weight = input("Did you enter your height in 'kg' or 'g'?: ")

    if (
        convert_unit_weight == "kg"
        or convert_unit_weight == "Kg"
        or convert_unit_weight == "kG"
        or convert_unit_weight == "KG"
    ):
        converted_weight_kg = weight * 1000
        print(f"Your weight in grams is {converted_weight_kg}g.")

    elif convert_unit_weight == "g" or convert_unit_weight == "G":
        converted_weight_g = weight / 1000
        print(f"Your weight in kilograms is {converted_weight_g}kg.")

    else:
        print("Error: Invalid unit.")

# BMI calculation
elif human_input == "bmi" or human_input == "Bmi" or human_input == "BMI":
    height_bmi = int(input("Enter your height: "))
    unit_bmi_height = input("Did you enter your height in 'cm' or 'm'?: ")

    if (
        unit_bmi_height == "cm"
        or unit_bmi_height == "CM"
        or unit_bmi_height == "Cm"
        or unit_bmi_height == "cM"
    ):
        bmi_height_in_m = height_bmi / 100

    elif unit_bmi_height == "m" or unit_bmi_height == "M":
        bmi_height_in_m = height_bmi

    else:
        print("Error: Invalid unit.")

    weight_bmi = int(input("Enter your weight: "))
    unit_bmi_weight = input("Did you enter your weight in 'g' or 'kg'?: ")

    if (
        unit_bmi_weight == "kg"
        or unit_bmi_weight == "Kg"
        or unit_bmi_weight == "kG"
        or unit_bmi_weight == "KG"
    ):
        bmi_weight_in_kg = weight_bmi

    elif unit_bmi_weight == "g" or unit_bmi_weight == "G":
        unit_bmi_weight = weight_bmi / 1000

    else:
        print("Error: Invalid unit.")

    calculated_bmi = bmi_weight_in_kg / (bmi_height_in_m ** 2)

    if calculated_bmi < 18.5:
        print(f"Your BMI is {calculated_bmi}. You are underweight.")

    elif calculated_bmi >= 18.5 and calculated_bmi <= 24.9:
        print(f"Your BMI is {calculated_bmi}. You are having a normal weight.")

    elif calculated_bmi >= 25.0 and calculated_bmi <= 29.9:
        print(f"Your BMI is {calculated_bmi}. You are overweight.")

    elif calculated_bmi >= 30.0 and calculated_bmi <= 34.9:
        print(f"Your BMI is {calculated_bmi}. You are having a obesity class I.")

    elif calculated_bmi >= 35.0 and calculated_bmi <= 39.9:
        print(f"Your BMI is {calculated_bmi}. You are having a obesity class II.")

    elif calculated_bmi > 40:
        print(f"Your BMI is {calculated_bmi}. You are having obesity class III.")

    else:
        print("Error: Cannot calculate BMI.")

else:
    print("Error: Invalid input")

print("Thank you for using 'HEIGHT, WEIGHT & BMI CALCULATOR'!")