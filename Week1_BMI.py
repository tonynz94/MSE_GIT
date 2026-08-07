def calBMI():
    weight = 0
    height = 0
    
    weight = float(input("input your weight(kg) : "))
    height = float(input("input your height(m) : "))
    
    bmi = weight / (float)(height * height)
    
    if bmi < 18.5:
        result = "underweight"
    elif bmi < 23:
        result = "Normal weight"
    elif bmi < 25:
        result = "Overweight"
    else:
        result = "Obese"
    
    print(f"BMI: {bmi:.2f}")
    print(f"Result: {result}")


def main():
    calBMI()

if __name__ == "__main__":
    main()