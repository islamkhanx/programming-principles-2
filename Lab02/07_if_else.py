if __name__ == "__main__":
    # subtopic python dictiionaries
    print(f"\n{'Example 1'}")
    a = 33
    b = 200
    if b > a:
        print("b is greater than a")

    print(f"\n{'Example 2'}")
    a = 33
    b = 33
    if b > a:
        print("b is greater than a")
    elif a == b:
        print("a and b are equal")

    print(f"\n{'Example 3'}")
    a = 200
    b = 33
    if b > a:
        print("b is greater than a")
    elif a == b:
        print("a and b are equal")
    else:
        print("a is greater than b")

    print(f"\n{'Example 4'}")
    a = 200
    b = 33
    if b > a:
        print("b is greater than a")
    else:
        print("b is not greater than a")

    print(f"\n{'Example 5'}")
    a = 2
    b = 330
    print("A") if a > b else print("B")

    print(f"\n{'Example 6'}")
    a = 330
    b = 330
    print("A") if a > b else print("=") if a == b else print("B")

    print(f"\n{'Example 7'}")
    a = 200
    b = 33
    c = 500
    if a > b and c > a:
        print("Both conditions are True")

    print(f"\n{'Example 8'}")
    a = 200
    b = 33
    c = 500
    if a > b or a > c:
        print("At least one of the conditions is True")

    print(f"\n{'Example 9'}")
    a = 33
    b = 200
    if not a > b:
        print("a is NOT greater than b")

    print(f"\n{'Example 10'}")
    x = 41
    if x > 10:
        print("Above ten,")
        if x > 20:
            print("and also above 20!")
        else:
            print("but not above 20.")

    print(f"\n{'Example 11'}")
    a = 33
    b = 200
    if b > a:
        pass

    print(f"\n{'Exercise 1'}")
    print("What will be the result of the following code:")
    print("""
            x = 5
            y = 8
            if x > y:
                print('Hello')
            else:
                print('Welcome')
        """)
    print("Ans: Welcome")
