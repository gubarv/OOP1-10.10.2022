class student():
    def __init__(self, name, napr, nomer, sr):
        self.name = name
        self.napr = napr
        self.nomer = nomer
        self.sr = sr

    def l(self):
        li.append([self.name, self.napr, self.nomer, self.sr])


li = []
n = int(input('Колличество студентов: '))
for i in range(n):
    new_stud = student(input(), input(), int(input()), float(input()))
    new_stud.l()
print(li)