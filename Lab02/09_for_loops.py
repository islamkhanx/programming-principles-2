if __name__ == "__main__":
    # subtopic python dictiionaries
    print(f"\n{'Example 1'}")
    fruits = ["apple", "banana", "cherry"]
    for x in fruits:
        print(x)

    print(f"\n{'Example 2'}")
    for x in "banana":
        print(x)

    print(f"\n{'Example 3'}")
    fruits = ["apple", "banana", "cherry"]
    for x in fruits:
        print(x)
        if x == "banana":
            break

    print(f"\n{'Example 4'}")
    fruits = ["apple", "banana", "cherry"]
    for x in fruits:
        if x == "banana":
            break
        print(x)

    print(f"\n{'Example 5'}")
    fruits = ["apple", "banana", "cherry"]
    for x in fruits:
        if x == "banana":
            continue
        print(x)

    print(f"\n{'Example 6'}")
    for x in range(6):
        print(x)

    print(f"\n{'Example 7'}")
    for x in range(2, 6):
        print(x)

    print(f"\n{'Example 8'}")
    for x in range(2, 30, 3):
        print(x)

    print(f"\n{'Example 9'}")
    for x in range(6):
        print(x)
    else:
        print("Finally finished!")

    print(f"\n{'Example 10'}")
    for x in range(6):
        if x == 3:
            break
        print(x)
    else:
        print("Finally finished!")

    print(f"\n{'Example 11'}")
    adj = ["red", "big", "tasty"]
    fruits = ["apple", "banana", "cherry"]
    for x in adj:
        for y in fruits:
            print(x, y)

    print(f"\n{'Example 12'}")
    for x in [0, 1, 2]:
        pass

    print(f"\n{'Exercise 1'}")
    print("What will be the result of the following code:",
          "\n\tfor x in range(3):\n\t\tprint(x)")
    print("Ans: \n0\n1\n2")
