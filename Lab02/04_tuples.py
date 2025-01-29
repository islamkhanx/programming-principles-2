if __name__ == "__main__":
    # subtopic python tuples
    print(f"\n{'Example 1'}")
    thistuple = ("apple", "banana", "cherry")
    print(thistuple)

    print(f"\n{'Example 2'}")
    thistuple = ("apple", "banana", "cherry", "apple", "cherry")
    print(thistuple)

    print(f"\n{'Example 3'}")
    thistuple = ("apple", "banana", "cherry")
    print(len(thistuple))

    print(f"\n{'Example 4'}")
    thistuple = ("apple",)
    print(type(thistuple))

    # NOT a tuple
    thistuple = ("apple")
    print(type(thistuple))

    print(f"\n{'Example 5'}")
    tuple1 = ("apple", "banana", "cherry")
    tuple2 = (1, 5, 7, 9, 3)
    tuple3 = (True, False, False)

    print(f"\n{'Example 6'}")
    tuple1 = ("abc", 34, True, 40, "male")

    print(f"\n{'Example 7'}")
    mytuple = ("apple", "banana", "cherry")
    print(type(mytuple))

    print(f"\n{'Example 8'}")
    thistuple = tuple(("apple", "banana", "cherry"))
    print(thistuple)

    print(f"\n{'Exercise 1'}")
    print("Which one of these is a tuple?")
    print("Ans: thistuple = ('apple', 'banana', 'cherry')")

    # Subtopic Access tuple items
    print(f"\n{'Example 1'}")
    thistuple = ("apple", "banana", "cherry")
    print(thistuple[1])

    print(f"\n{'Example 2'}")
    thistuple = ("apple", "banana", "cherry")
    print(thistuple[-1])

    print(f"\n{'Example 3'}")
    thistuple = ("apple", "banana", "cherry", "orange",
                 "kiwi", "melon", "mango")
    print(thistuple[2:5])

    print(f"\n{'Example 4'}")
    thistuple = ("apple", "banana", "cherry", "orange",
                 "kiwi", "melon", "mango")
    print(thistuple[:4])

    print(f"\n{'Example 5'}")
    thistuple = ("apple", "banana", "cherry", "orange",
                 "kiwi", "melon", "mango")
    print(thistuple[2:])

    print(f"\n{'Example 6'}")
    thistuple = ("apple", "banana", "cherry", "orange",
                 "kiwi", "melon", "mango")
    print(thistuple[-4:-1])

    print(f"\n{'Example 7'}")
    thistuple = ("apple", "banana", "cherry")
    if "apple" in thistuple:
        print("Yes, 'apple' is in the fruits tuple")

    print(f"\n{'Exercise 1'}")
    print("You can access tuple items by referring to the index number,",
          "but what is the index number of the first item?")
    print("Ans: 0")

    # Subtopic update tuples
    print(f"\n{'Example 1'}")
    x = ("apple", "banana", "cherry")
    y = list(x)
    y[1] = "kiwi"
    x = tuple(y)
    print(x)

    print(f"\n{'Example 2'}")
    thistuple = ("apple", "banana", "cherry")
    y = list(thistuple)
    y.append("orange")
    thistuple = tuple(y)

    print(f"\n{'Example 3'}")
    thistuple = ("apple", "banana", "cherry")
    y = ("orange",)
    thistuple += y
    print(thistuple)

    print(f"\n{'Example 4'}")
    thistuple = ("apple", "banana", "cherry")
    y = list(thistuple)
    y.remove("apple")
    thistuple = tuple(y)

    print(f"\n{'Example 5'}")
    thistuple = ("apple", "banana", "cherry")
    del thistuple
    print(thistuple)

    print(f"\n{'Exercise 1'}")
    print("You cannot change the items of a tuple, but there are workarounds.",
          "Which of the following suggestion will work?")
    print("Ans: NONE")

    # Subtopic unpack tuples
    print(f"\n{'Example 1'}")
    fruits = ("apple", "banana", "cherry")

    print(f"\n{'Example 2'}")
    fruits = ("apple", "banana", "cherry")
    (green, yellow, red) = fruits
    print(green)
    print(yellow)
    print(red)

    print(f"\n{'Example 3'}")
    fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
    (green, yellow, *red) = fruits
    print(green)
    print(yellow)
    print(red)

    print(f"\n{'Example 4'}")
    fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
    (green, *tropic, red) = fruits
    print(green)
    print(tropic)
    print(red)

    print(f"\n{'Exercise 1'}")
    print("Consider the following code:\n",
          "\tfruits = ('apple', 'banana', 'cherry')\n",
          "\t(x, y, z) = fruits\n",
          "\tprint(y)\n",
          "What will be the value of y?")
    print("Ans: banana")

    # Subtopic loop tuples
    print(f"\n{'Example 1'}")
    thistuple = ("apple", "banana", "cherry")
    for x in thistuple:
        print(x)

    print(f"\n{'Example 2'}")
    thistuple = ("apple", "banana", "cherry")
    for i in range(len(thistuple)):
        print(thistuple[i])

    print(f"\n{'Example 3'}")
    thistuple = ("apple", "banana", "cherry")
    i = 0
    while i < len(thistuple):
        print(thistuple[i])
        i = i + 1

    print(f"\n{'Exercise 1'}")
    print("What is correct syntx for looping through the items of a tuple?\n")
    print("Ans: \n\tfor x in ('apple', 'banana', 'cherry'):\n\t\tprint(x)")

    # Subtopic join tuples
    print(f"\n{'Example 1'}")
    tuple1 = ("a", "b", "c")
    tuple2 = (1, 2, 3)
    tuple3 = tuple1 + tuple2
    print(tuple3)

    print(f"\n{'Example 2'}")
    fruits = ("apple", "banana", "cherry")
    mytuple = fruits * 2
    print(mytuple)

    print("What is a correct syntax for joining",
          "tuple1 and tuple2 into tuple3?")
    print("Ans: \n\ttuple3 = tuple1 + tuple2")
