
# BMI Calculator using Class and Object

class BMI:
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height

    #you dont need here
    def calculate_bmi(weight, height):
        return weight / (height ** 2)

    def show_result():
        bmi = self.calculate_bmi(self.weight, self.height)
        print(f"Your BMI is: {bmi:.2f}")


def main():
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in metres: "))

    # Create an object
    person = BMI(weight, height)

    # Call the function
    person.show_result()


if __name__ == "__main__":
    main()