class Person:
    moods = ("happy", "tired", "lazy")
    
    def __init__(self, name, money, mood, healthRate):
        self.name = name
        self.money = money
        self.mood = mood
        self.healthRate = max(0, min(healthRate, 100))
    
    def sleep(self, hours):
        if hours == 7:
            self.mood = "happy"
        elif hours < 7:
            self.mood = "tired"
        else:
            self.mood = "lazy"
    
    def eat(self, meals):
        self.healthRate = max(0, min(100, meals * 50))
    
    def buy(self, items):
        self.money -= items * 10
