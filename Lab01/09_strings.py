if __name__ == "__main__":
    # Subtopic Python Strings
    print(f"\n{'Example 1'}")
    print("Hello")
    print('Hello')

    print(f"\n{'Example 2'}")
    print("It's alright")
    print("He is called 'Johnny'")
    print('He is called "Johnny"')

    print(f"\n{'Example 3'}")
    a = "Hello"
    print(a)

    print(f"\n{'Example 4'}")
    a = """Lorem ipsum dolor sit amet,
    consectetur adipiscing elit,
    sed do eiusmod tempor incididunt
    ut labore et dolore magna aliqua."""
    print(a)

    print(f"\n{'Example 5'}")
    a = '''Lorem ipsum dolor sit amet,
    consectetur adipiscing elit,
    sed do eiusmod tempor incididunt
    ut labore et dolore magna aliqua.'''
    print(a)

    print(f"\n{'Example 6'}")
    a = "Hello, World!"
    print(a[1])

    print(f"\n{'Example 7'}")
    for x in "banana":
        print(x)

    print(f"\n{'Example 8'}")
    a = "Hello, World!"
    print(len(a))

    print(f"\n{'Example 9'}")
    txt = "The best things in life are free!"
    print("free" in txt)

    print(f"\n{'Example 10'}")
    txt = "The best things in life are free!"
    if "free" in txt:
        print("Yes, 'free' is present.")

    print(f"\n{'Example 11'}")
    txt = "The best things in life are free!"
    print("expensive" not in txt)

    print(f"\n{'Example 12'}")
    txt = "The best things in life are free!"
    if "expensive" not in txt:
        print("No, 'expensive' is NOT present.")

    print(f"\n{'Exercise 1'}")
    print("What will be the result of the following code:",
          "\nx = 'Welcome' \nprint(x[3])")
    print(f"Ans {'c'}")

    # Subtopic Slicing Strings
    print(f"\n{'Example 1'}")
    b = "Hello, World!"
    print(b[2:5])

    print(f"\n{'Example 2'}")
    b = "Hello, World!"
    print(b[:5])

    print(f"\n{'Example 3'}")
    b = "Hello, World!"
    print(b[2:])

    print(f"\n{'Example 4'}")
    b = "Hello, World!"
    print(b[-5:-2])

    print(f"\n{'Exercise 1'}")
    print("What will be the result of the following code:",
          "\nx = 'Welcome'", "\nprint(x[3:5])")
    print(f"Ans {'co'}")

    # Subtopic Modify Strings
    print(f"\n{'Example 1'}")
    a = "Hello, World!"
    print(a.upper())

    print(f"\n{'Example 2'}")
    a = "Hello, World!"
    print(a.lower())

    print(f"\n{'Example 3'}")
    a = " Hello, World! "
    print(a.strip())  # returns "Hello, World!"

    print(f"\n{'Example 4'}")
    a = "Hello, World!"
    print(a.replace("H", "J"))

    print(f"\n{'Example 5'}")
    a = "Hello, World!"
    print(a.split(","))  # returns ['Hello', ' World!']

    print(f"\n{'Exercise 1'}")
    print("What is a correct syntax to print a string in upper case letters?")
    print("Ans 'Welcome'.upper()")

    # Subtopic String Concatenation
    print(f"\n{'Example 1'}")
    a = "Hello"
    b = "World"
    c = a + b
    print(c)

    print(f"\n{'Example 2'}")
    a = "Hello"
    b = "World"
    c = a + " " + b
    print(c)

    print(f"\n{'Exercise 1'}")
    print(" What is a correct syntax to merge", 
          "variable x and y into variable z?")
    print("Ans z = x + y")

    # Subtopic Format - Strings
    print(f"\n{'Example 1'}")
    age = 36
    txt = f"My name is John, I am {age}"
    print(txt)

    print(f"\n{'Example 2'}")
    price = 59
    txt = f"The price is {price} dollars"
    print(txt)

    print(f"\n{'Example 3'}")
    price = 59
    txt = f"The price is {price:.2f} dollars"
    print(txt)

    print(f"\n{'Example 4'}")
    txt = f"The price is {20 * 59} dollars"
    print(txt)

    print("Exercise 1")
    print("If x = 9, what is a correct syntax to print",
          "'The price is 9.00 dollars'?")
    print("Ans 'print(f'The price is {x:.2f} dollars')'")

    # Subtopic Escape Characters
    print(f"\n{'Example 1'}")
    txt = "We are the so-called \"Vikings\" from the north."
