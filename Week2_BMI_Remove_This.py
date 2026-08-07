
# BMI Calculator using Class and Object

class BMI:
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height

    # 'self' is not needed here because this method doesn't read or
    # modify any instance attributes (self.weight / self.height).
    # It only computes a result from the arguments it's given, so it
    # behaves like a plain, stateless function -> mark it @staticmethod.
    @staticmethod
    def calculate_bmi(weight, height):
        return weight / (height ** 2)

    # 'self' IS needed here because this method reads data that
    # belongs to this specific object (self.weight, self.height) and
    # calls another method on it. Without self, there's no way to
    # access that instance's stored state.
    def show_result(self):
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