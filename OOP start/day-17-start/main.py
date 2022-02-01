class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.name = username

user_1 = User("001","angela")
#or
user_1.id = "001"
user_1.name = "angela"

print(user_1.name)

class Car:
    def __init__(self, seats):
        self.seats = seats

    def enter_rade_mode():
        self.searts = 2

my_car = Car(5)
# equivalent to
my_car.seats = 5
