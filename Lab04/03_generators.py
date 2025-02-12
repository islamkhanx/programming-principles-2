from typing import Iterator


def generate_range(n: int) -> Iterator[int]:
    """generates the squares of numbers up to some number N."""
    for i in range(n):
        yield i ** 2


def cli_generator() -> None:
    """print the even numbers between 0 and n
    in comma separated form where n is input from console.
    """
    def gen_num(n) -> Iterator[int]:
        for i in range(n):
            yield i

    n = int(input())
    for i in gen_num(n):
        print(i, end=', ')


def iter_12_divisor(n) -> Iterator[int]:
    """n iterate the numbers, which are divisible by 3 and 4,
    between a given range 0 and n.
    """
    for i in range(n):
        if i % 12 == 0:
            yield i


def squares(a: int, b: int) -> Iterator[int]:
    """
    generator squares to yield the square of all numbers from (a) to (b).
    Test it with a "for" loop and print each of the yielded values.
    """
    for i in range(a, b + 1):
        yield i ** 2


def down_generator(n: int) -> Iterator[int]:
    """ generator that returns all numbers from (n) down to 0."""
    for i in range(n, 0, -1):
        yield i


if __name__ == "__main__":

    for i, x in enumerate(squares(1, 10)):
        print(x)
