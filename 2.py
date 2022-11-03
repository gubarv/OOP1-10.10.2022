class year():
    def __init__(self, y):
        self.y = y
    def pr(self):
        if self.y % 4 != 0 or (self.y % 100 == 0 and self.y % 400 != 0):
            print("Обычный")
        else:
            print("Високосный")

this_year = year(int(input('Введите год: ')))
this_year.pr()