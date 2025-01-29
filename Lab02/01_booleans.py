if __name__ == "__main__":

    print(f"\n{'Example 1'}")
    print(10 > 9)
    print(10 == 9)
    print(10 < 9)

    print(f"\n{'Example 2'}")
    a = 200
    b = 33

    if b > a:
        print("b is greater than a")
    else:
        print("b is not greater than a")

    print(f"\n{'Example 3'}")
    print(bool("Hello"))
    print(bool(15))

    print(f"\n{'Example 4'}")
    x = "Hello"
    y = 15

    print(bool(x))
    print(bool(y))

    print(f"\n{'Example 5'}")
    bool("abc")
    bool(123)
    bool(["apple", "cherry", "banana"])

    print(f"\n{'Example 6'}")
    bool(False)
    bool(None)
    bool(0)
    bool("")
    bool(())
    bool([])
    bool({})

    print(f"\n{'Example 7'}")

    class myclass():
        def __len__(self):
            return 0

    myobj = myclass()
    print(bool(myobj))

    print(f"\n{'Example 8'}")

    def myFunction():
        return True

    print(myFunction())

    print(f"\n{'Example 9'}")

    def myFunction():
        return True

    if myFunction():
        print("YES!")
    else:
        print("NO!")

    print(f"\n{'Example 10'}")
    x = 200
    print(isinstance(x, int))

    print(f"\n{'Exercise 1'}")
    print("What will be the result of the following syntax: print(5 > 3)?")
    print(f"Ans: {'True'}")
