if __name__ == "__main__":

    # Subtopic Python Variables

    print(f"\n{'Example 1'}")
    print("E")
    x = 5
    y = "John"
    print(x)
    print(y)

    print(f"\n{'Example 2'}")
    x = 4        # x is of type int
    x = "Sally"  # x is now of type str
    print(x)

    print(f"\n{'Example 3'}")
    x = str(3)    # x will be '3'
    y = int(3)    # y will be 3
    z = float(3)  # z will be 3.0

    print(f"\n{'Example 4'}")
    x = 5
    y = "John"
    print(type(x))
    print(type(y))

    print(f"\n{'Example 5'}")
    x = "John"
    # is the same as
    x = 'John'

    print(f"\n{'Example 6'}")
    a = 4
    A = "Sally"
    # A will not overwrite a

    print(f"\n {'Exercise 1'}")
    print("What is a correct way to declare a Python variable?")
    print(f"Ans {'x = 5'}")

    # Subtopic Variable Names

    print(f"\n{'Example 1'}")
    myvar = "John"
    my_var = "John"
    _my_var = "John"
    myVar = "John"
    MYVAR = "John"
    myvar2 = "John"

    print(f"\n {'Exercise 1'}")
    print("Which is NOT a legal variable name?")
    print(f"Ans {'my-var = 20'}")

    # Subtopic Assign Multiple Values
    print(f"\n{'Example 1'}")
    x, y, z = "Orange", "Banana", "Cherry"
    print(x)
    print(y)
    print(z)

    print(f"\n{'Example 2'}")
    x = y = z = "Orange"
    print(x)
    print(y)
    print(z)

    print(f"\n{'Example 3'}")
    fruits = ["apple", "banana", "cherry"]
    x, y, z = fruits
    print(x)
    print(y)
    print(z)

    print(f"\n {'Exercise 1'}")
    print("What is a correct syntax to add the value 'Hello World'",
          "to 3 variables in one statement?")
    print(f"Ans {'x = y = z = Hello World'}")

    # Subtopic Output Variables
    print(f"\n{'Example 1'}")
    x = "Python is awesome"
    print(x)

    print(f"\n{'Example 2'}")
    x = "Python"
    y = "is"
    z = "awesome"
    print(x, y, z)

    print(f"\n{'Example 3'}")
    x = "Python "
    y = "is "
    z = "awesome"
    print(x + y + z)

    print(f"\n{'Example 4'}")
    x = 5
    y = 10
    print(x + y)

    print(f"\n{'Example 5'}")
    x = 5
    y = "John"
    print(x, y)

    print(f"\n {'Exercise 1'}")
    print("Consider the following code:print('Hello', 'World')"
          "What will be the printed result??")
    print(f"Ans {'Hello World'}")

    # Subtopics Global Variables
    print(f"\n{'Example 1'}")
    x = "awesome"

    def myfunc():
        print("Python is " + x)

    myfunc()
    x = "awesome"

    print(f"\n{'Example 2'}")

    def myfunc():
        x = "fantastic"

    print("Python is " + x)

    myfunc()
    print("Python is " + x)

    print(f"\n{'Example 3'}")

    def myfunc():
        global x
        x = "fantastic"

        myfunc()

    print("Python is " + x)

    print(f"\n{'Example 4'}")
    x = "awesome"

    def myfunc():
        global x
        x = "fantastic"

    myfunc()

    print("Python is " + x)

    print(f"\n {'Exercise 1'}")
    print("""
        Consider the following code:
            x = 'awesome'
            def myfunc():
                x = 'fantastic'
            myfunc()
            print('Python is ' + x)
            What will be the printed result?
        """)
    print(f"Ans {'Python is awesome'}")
