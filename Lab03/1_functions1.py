from typing import Tuple, List, Hashable
from itertools import permutations
from math import pi
from random import randint


def grams_to_ounces(grams: float) -> float:
    return 28.3495231 * grams


def fahrenheit_to_celsius(F: float) -> float:
    return (5 / 9) * (F - 32)


def solve(numheads: int, numlegs: int) -> Tuple[int, int]:
    chickens = 2 * numheads - numlegs // 2
    rabbits = numheads - chickens
    return chickens, rabbits


def filter_prime(number_string: str) -> str:
    def is_prime(num: int) -> bool:
        for i in range(2, int(2 + num**0.5)):
            if num % i == 0:
                return False
        return True

    nums = [int(x) for x in number_string.split()]
    nums = [x for x in nums if is_prime(x)]

    return " ".join(nums)


def print_permutations() -> None:
    s = input()
    perms = ["".join(p) for p in permutations(s)]

    for perm in perms:
        print(perm)


def reverse_string(sentence: str) -> str:
    words = sentence.split()
    return " ".join(words[::-1])


def has_33(nums: List[int]) -> bool:
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1] == 3:
            return True
    return False


def spy_game(nums: List[int]) -> bool:
    idx = 0
    spy = (0, 0, 7)

    for i, x in enumerate(nums):
        if x == spy[idx]:
            idx += 1
        if idx == len(spy):
            return True
    return False


def calculate_sphere_volume(radius: float) -> float:
    return (4 / 3) * pi * radius**3


def unique_el_list(elements: List[Hashable]) -> List[Hashable]:
    return list(dict.fromkeys(elements).keys())


def is_palindrome(sequence: str) -> bool:
    return sequence == sequence[::-1]


def histogram(heights: List[int]) -> None:
    for height in heights:
        print("*" * height)


def guess_the_number():
    name = input("Hello! What is your name?\n")
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    number = randint(0, 20)
    cnt = 0

    while True:
        guess = input("Take a guess.\n")
        cnt += 1
        if guess == number:
            break
        elif guess < number:
            print("Your guess is too low.")
        else:
            print("Your guess is too high.")

    print(
        f"Good job, {name}!",
        f"You guessed my number in {cnt}",
        f"guess{'ss' if cnt > 0 else ''}!",
    )
