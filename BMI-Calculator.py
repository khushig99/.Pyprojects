Height_in_cm = float(input("Enter your height in Centimeter (cm):"))
Weight = float(input("Enter your Weight in kilograms (kg):"))
if Height_in_cm <= 0 or Weight <= 0:
    raise ValueError("Please enter valid positive values for height and weight.")

Height_meter = Height_in_cm * 0.01

if Height_meter > 0 and  Weight > 0:
    BMI = Weight / (Height_meter ** 2)
    print("We are calculating your BMI, please wait.... ")
    
    if BMI <= 18.5:
        print(f"Your BMI is {BMI:.2f}")
        print("Category : " + "You are underweight and health risks are Minimal")
    elif 18.5<  BMI <= 24.9:
        print(f"Your BMI is : {BMI:.2f}")
        print("Category : " + "You are Normal weight and health risks are Minimal")
    elif 25 < BMI <= 29:
        print(f"Your BMI is : {BMI:.2f}")
        print("Category : " + "You are Over weight and health risks are Increased")
    elif 30< BMI <=34.9:
        print(f"Your BMI is : {BMI:.2f}")
        print("Category : " + "You are Obese and health risks are Very High")
    elif BMI > 35:
        print(f"Your BMI is : {BMI:.2f}")
        print("Category : " + "You are Morbidly Obese and health risks are Extremely High")
else:
    print("we are sorry , you are out of the range, we can't calculate your BMI")





#advance level
# import logging

# def get_user_input():
#     """
#     Get user input for height in centimeters and weight in kilograms,
#     and validate that the entered values are positive.
#     """
#     try:
#         height_in_cm = float(input("Enter your height in Centimeter (cm): "))
#         weight = float(input("Enter your Weight in kilograms (kg): "))

#         if height_in_cm <= 0 or weight <= 0:
#             raise ValueError("Please enter valid positive values for height and weight.")

#         return height_in_cm, weight
#     except ValueError as ve:
#         logging.error(f"Invalid input: {ve}")
#         return None, None

# def calculate_bmi(height_in_cm, weight):
#     """
#     Calculate BMI based on height in centimeters and weight in kilograms.
#     """
#     try:
#         # Convert height from centimeters to meters (1 cm = 0.01 meters)
#         height_in_meters = height_in_cm * 0.01
#         bmi = weight / (height_in_meters ** 2)
#         return bmi
#     except ZeroDivisionError:
#         logging.error("Error: Height should not be zero.")
#         return None
#     except Exception as e:
#         logging.error(f"An unexpected error occurred during BMI calculation: {e}")
#         return None

# def interpret_bmi(bmi):
#     """
#     Interpret BMI and provide category based on predefined ranges.
#     """
#     if bmi is None:
#         return "Unable to calculate BMI. Please check your input."

#     if bmi <= 18.5:
#         return f"Your BMI is {bmi:.2f}. Category: You are underweight and health risks are Minimal."
#     elif 18.5 < bmi <= 24.9:
#         return f"Your BMI is {bmi:.2f}. Category: You are Normal weight and health risks are Minimal."
#     elif 25 < bmi <= 29.9:
#         return f"Your BMI is {bmi:.2f}. Category: You are Overweight and health risks are Increased."
#     elif 30 < bmi <= 34.9:
#         return f"Your BMI is {bmi:.2f}. Category: You are Obese and health risks are Very High."
#     elif bmi > 35:
#         return f"Your BMI is {bmi:.2f}. Category: You are Morbidly Obese and health risks are Extremely High."

# def main():
#     """
#     Main function to orchestrate the BMI calculation program.
#     """
#     logging.basicConfig(filename='bmi_calculator.log', level=logging.INFO)
z
#     logging.info("BMI Calculator Program - Start")

#     try:
#         height, weight = get_user_input()
#         bmi = calculate_bmi(height, weight)

#         if bmi is not None:
#             logging.info(f"BMI calculated successfully: {bmi}")
#             result = interpret_bmi(bmi)
#             print(result)
#         else:
#             print("An error occurred during BMI calculation. Please check your input.")

#     except Exception as e:
#         logging.error(f"An unexpected error occurred: {e}")
#         print("An unexpected error occurred. Please check the logs for details.")

#     logging.info("BMI Calculator Program - End")

# if __name__ == "__main__":
#     main()
