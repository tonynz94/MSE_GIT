class BMI:
    height = 0
    weight = 0
    bmi = 0
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight
        self.bmi = weight / height ** 2

    def printState(self):
        if self.bmi < 18.5:
            result = "underweight"
        elif self.bmi < 23:
            result = "Normal weight"
        elif self.bmi < 25:
            result = "Overweight"
        else:
            result = "Obese"

        print(f"BMI : {self.bmi:.2f}, result : {result}")


def main():
    weight = float(input("Please enter your weight : "))
    height = float(input("Please enter your height : "))

    myBmi = BMI(height, weight)
    myBmi.printState()

if __name__ == "__main__":
    main()