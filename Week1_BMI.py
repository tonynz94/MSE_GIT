def calBMI():
    weight = 0
    height = 0
    
     # Get weight and height input from the use
    weight = float(input("input your weight(kg) : "))
    height = float(input("input your height(m) : "))

    #BMI => weight(kg) / height(m)^2
    bmi = weight / (float)(height * height)
    
    if bmi < 18.5:
        result = "underweight"
    elif bmi < 23:
        result = "Normal weight"
    elif bmi < 25:
        result = "Overweight"
    else:
        result = "Obese"

    # Print the result
    print(f"BMI: {bmi:.2f}")
    print(f"Result: {result}")


def main():
    calBMI()

if __name__ == "__main__":
    main()