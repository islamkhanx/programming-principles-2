from typing import List


class University:
    def __init__(self):
        self.string = None

    def get_string(self):
        string = input()
        self.string = string

    def print_string(self):
        print(self.string)


class Shape:
    def __init__(self):
        self.his_area = 0

    def area(self):
        print(self.his_area)


class Square(Shape):
    def __init__(self, lenght: float):
        super().__init__()
        self.his_area = lenght * lenght


class Rectangle(Shape):
    def __init__(self, lenght: float, width: float):
        super().__init__()
        self.his_area = lenght * lenght


class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def show(self):
        print(self.x, self.y)

    def move(self, x_new: float, y_new: float):
        self.x, self.y = x_new, y_new

    def dist(self, other: "Point"):
        horz_dist = (self.x - other.x) ** 2
        vert_dist = (self.y - other.y) ** 2
        return (horz_dist + vert_dist) ** 0.5


class Account:
    def __init__(self, owner: str, initial_balance: float):
        self.owner = owner
        self.balance = initial_balance

    def deposit(self, amount: float):
        self.balance += amount
        print("Transaction Succesful")

    def wighdraw(self, amount: float):
        if amount <= self.balance:
            self.balance -= amount
            print("Transaction Succesful")
        else:
            print("Not enough Balance")


def filter_prime(numbers: List[int]) -> List[int]:
    return list(
        filter(
            lambda x: x < 3 or all([x % i != 0 for i in range(2, int(x**0.5) + 1)]),
            numbers,
        )
    )
