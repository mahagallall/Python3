class Person:
    moods = ("Happy", "Tired", "Lazy")

    def __init__(self, name, money, mood, healthRate):
        self.name = name
        self.money = money
        self.mood = mood
        self.healthRate = healthRate

    def sleep(self, hours):
        if hours == 7:
            self.mood = self.moods[0]  
        elif hours < 7:
            self.mood = self.moods[1]  
        else:
            self.mood = self.moods[2]  

    def eat(self, meals):
        if meals == 3:
            self.healthRate = 100
        elif meals == 2:
            self.healthRate = 75
        elif meals == 1:
            self.healthRate = 50

    def buy(self, items):
        self.money -= items * 10  



person1 = Person("Maha", 500, "Happy", 100)

