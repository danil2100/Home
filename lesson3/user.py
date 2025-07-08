class User:

    def __init__(self, first_name, last_name):
        self.first_mame = first_name
        self.last_name = last_name

    def print_first_name(self):
        print(self.first_mame)

    def print_last_name(self):
        print(self.last_name)

    def print_full_name(self):
        print(f"{self.first_mame} {self.last_name}")


Daniil = User("Daniil", "Chekmarev")
Chekmarev = User("Daniil", "Chekmarev")
Daniil_Chekmarev = User("Daniil", "Chekmarev")
