class Cat():

    def __init__(self, name, age):

        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + " сейчас сидит.")

    def roll_over(self):
        print(self.name.title() + " перевернулся!")

my_cat = Cat('Пушок', 6)

print("Моего кота зовут " + my_cat.name.title() + ".")
print("Моему коту " + str(my_cat.age) + " лет.")

ur_cat = Cat('Черныш', 8)
ur_cat.sit()
ur_cat.roll_over()