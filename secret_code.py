import random


class SecretCode:
    def generate_code(self):
        # letters of code
        self.secret_first_letter = random.choice("ABC")
        self.secret_second_letter = random.choice("ABC")

        # numbers of code
        self.secret_first_number = str(random.randint(1, 3))
        self.secret_second_number = str(random.randint(1, 3))

        self.inital_code = []

        self.inital_code.append(self.secret_first_letter)
        self.inital_code.append(self.secret_second_letter)
        self.inital_code.append(self.secret_first_number)
        self.inital_code.append(self.secret_second_number)

    def authenticate_code(self):
        print(self.inital_code)

        self.final_code = []

        self.counter = 1
        self.correct = 0

        while self.counter <= 10:
            print(f"try #{self.counter}")
            self.count = 0
            while self.count <= 3:
                self.user_code = input(
                    f"Enter the caracters #{self.count} of code: "
                ).upper()
                self.final_code.append(self.user_code)

                if self.final_code in self.inital_code:
                    print("The caracter is in code...")
                else:
                    print("The caracter is no in code")

                if self.final_code[self.count] == self.inital_code[self.count]:
                    print(f"The caracter is correct and his position is {self.count}")
                    self.correct += 1
                else:
                    print("The caracter incorrect")

                self.count += 1

            if self.correct == 4:
                print("The code is correct")
                break
            else:
                print(f"The code is incorrect {self.final_code}")
            self.counter += 1


code = SecretCode()
code.generate_code()
code.authenticate_code()
