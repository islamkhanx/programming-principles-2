if __name__ == "__main__":
    # subtopic python sets
    print(f"\n{'Example 1'}")
    thisset = {"apple", "banana", "cherry"}
    print(thisset)

    print(f"\n{'Example 2'}")
    thisset = {"apple", "banana", "cherry", "apple"}
    print(thisset)

    print(f"\n{'Example 3'}")
    thisset = {"apple", "banana", "cherry", True, 1, 2}
    print(thisset)

    print(f"\n{'Example 4'}")
    thisset = {"apple", "banana", "cherry", False, True, 0}
    print(thisset)

    print(f"\n{'Example 5'}")
    thisset = {"apple", "banana", "cherry"}
    print(len(thisset))

    print(f"\n{'Example 6'}")
    set1 = {"apple", "banana", "cherry"}
    set2 = {1, 5, 7, 9, 3}
    set3 = {True, False, False}

    print(f"\n{'Example 7'}")
    set1 = {"abc", 34, True, 40, "male"}

    print(f"\n{'Example 8'}")
    myset = {"apple", "banana", "cherry"}
    print(type(myset))

    print(f"\n{'Example 9'}")
    thisset = set(("apple", "banana", "cherry"))
    print(thisset)

    print(f"\n{'Exercise 1'}")
    print("Which one of these is a set?")
    print("Ans: myset = {'apple', 'banana', 'cherry'}")

    # Subtopic acces set items
    print(f"\n{'Example 1'}")
    thisset = {"apple", "banana", "cherry"}
    for x in thisset:
        print(x)

    print(f"\n{'Example 2'}")
    thisset = {"apple", "banana", "cherry"}
    print("banana" in thisset)

    print(f"\n{'Example 3'}")
    thisset = {"apple", "banana", "cherry"}
    print("banana" not in thisset)

    print(f"\n{'Exercise 1'}")
    print("True or False. You can access set items by referring to the index.")
    print("Ans: False")

    # Subtopic add set items
    print(f"\n{'Example 1'}")
    thisset = {"apple", "banana", "cherry"}
    thisset.add("orange")
    print(thisset)

    print(f"\n{'Example 2'}")
    thisset = {"apple", "banana", "cherry"}
    tropical = {"pineapple", "mango", "papaya"}
    thisset.update(tropical)
    print(thisset)

    print(f"\n{'Example 3'}")
    thisset = {"apple", "banana", "cherry"}
    mylist = ["kiwi", "orange"]
    thisset.update(mylist)
    print(thisset)

    print(f"\n{'Exercise 1'}")
    print("What is a correct syntax for adding items to a set?")
    print("Ans: add()")

    # Subtopic Remove set items
    print(f"\n{'Example 1'}")
    thisset = {"apple", "banana", "cherry"}
    thisset.remove("banana")
    print(thisset)

    print(f"\n{'Example 2'}")
    thisset = {"apple", "banana", "cherry"}
    thisset.discard("banana")
    print(thisset)

    print(f"\n{'Example 3'}")
    thisset = {"apple", "banana", "cherry"}
    x = thisset.pop()
    print(x)
    print(thisset)

    print(f"\n{'Example 4'}")
    thisset = {"apple", "banana", "cherry"}
    thisset.clear()
    print(thisset)

    print(f"\n{'Example 5'}")
    thisset = {"apple", "banana", "cherry"}
    del thisset
    print(thisset)

    print(f"\n{'Exercise 1'}")
    print("What is a correct syntax for removing an item from a set?")
    print("Ans: remove()")

    # Subtopic loop items
    print(f"\n{'Example 1'}")
    thisset = {"apple", "banana", "cherry"}
    for x in thisset:
        print(x)

    print(f"\n{'Exercise 1'}")
    print("What is a correct syntax for looping through the items of a set?")
    print("Ans: \n\tfor x in {'apple', 'banana', 'cherry'}:\n\t\tprint(x))")

    # Subtopic join sets
    print(f"\n{'Example 1'}")
    set1 = {"a", "b", "c"}
    set2 = {1, 2, 3}
    set3 = set1.union(set2)
    print(set3)

    print(f"\n{'Example 2'}")
    set1 = {"a", "b", "c"}
    set2 = {1, 2, 3}
    set3 = set1 | set2
    print(set3)

    print(f"\n{'Example 3'}")
    set1 = {"a", "b", "c"}
    set2 = {1, 2, 3}
    set3 = {"John", "Elena"}
    set4 = {"apple", "bananas", "cherry"}
    myset = set1.union(set2, set3, set4)
    print(myset)

    print(f"\n{'Example 4'}")
    set1 = {"a", "b", "c"}
    set2 = {1, 2, 3}
    set3 = {"John", "Elena"}
    set4 = {"apple", "bananas", "cherry"}
    myset = set1 | set2 | set3 | set4
    print(myset)

    print(f"\n{'Example 5'}")
    x = {"a", "b", "c"}
    y = (1, 2, 3)
    z = x.union(y)
    print(z)

    print(f"\n{'Example 6'}")
    set1 = {"a", "b", "c"}
    set2 = {1, 2, 3}
    set1.update(set2)
    print(set1)

    print(f"\n{'Example 7'}")
    set1 = {"apple", "banana", "cherry"}
    set2 = {"google", "microsoft", "apple"}
    set3 = set1.intersection(set2)
    print(set3)

    print(f"\n{'Example 8'}")
    set1 = {"apple", "banana", "cherry"}
    set2 = {"google", "microsoft", "apple"}
    set3 = set1 & set2
    print(set3)

    print(f"\n{'Example 9'}")
    set1 = {"apple", "banana", "cherry"}
    set2 = {"google", "microsoft", "apple"}
    set1.intersection_update(set2)
    print(set1)

    print(f"\n{'Example 10'}")
    set1 = {"apple", 1,  "banana", 0, "cherry"}
    set2 = {False, "google", 1, "apple", 2, True}
    set3 = set1.intersection(set2)
    print(set3)

    print(f"\n{'Example 11'}")
    set1 = {"apple", "banana", "cherry"}
    set2 = {"google", "microsoft", "apple"}
    set3 = set1.difference(set2)
    print(set3)

    print(f"\n{'Example 12'}")
    set1 = {"apple", "banana", "cherry"}
    set2 = {"google", "microsoft", "apple"}
    set3 = set1 - set2
    print(set3)

    print(f"\n{'Example 13'}")
    set1 = {"apple", "banana", "cherry"}
    set2 = {"google", "microsoft", "apple"}
    set1.difference_update(set2)
    print(set1)

    print(f"\n{'Example 14'}")
    set1 = {"apple", "banana", "cherry"}
    set2 = {"google", "microsoft", "apple"}
    set3 = set1.symmetric_difference(set2)
    print(set3)

    print(f"\n{'Example 15'}")
    set1 = {"apple", "banana", "cherry"}
    set2 = {"google", "microsoft", "apple"}
    set3 = set1 ^ set2
    print(set3)

    print(f"\n{'Example 16'}")
    set1 = {"apple", "banana", "cherry"}
    set2 = {"google", "microsoft", "apple"}
    set1.symmetric_difference_update(set2)
    print(set1)

    print(f"\n{'Exercise 1'}")
    print("What is a correct syntax for joining set1 and set2 into set3?")
    print("Ans: \n\tset3 = set1.union(set2)")
