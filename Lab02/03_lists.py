if __name__ == "__main__":
    # Subtopic python lists
    print(f"\n{'Example 1'}")
    thislist = ["apple", "banana", "cherry"]
    print(thislist)

    print(f"\n{'Example 2'}")
    thislist = ["apple", "banana", "cherry", "apple", "cherry"]
    print(thislist)

    print(f"\n{'Example 3'}")
    thislist = ["apple", "banana", "cherry"]
    print(len(thislist))

    print(f"\n{'Example 4'}")
    list1 = ["apple", "banana", "cherry"]
    list2 = [1, 5, 7, 9, 3]
    list3 = [True, False, False]

    print(f"\n{'Example 5'}")
    list1 = ["abc", 34, True, 40, "male"]

    print(f"\n{'Example 6'}")
    mylist = ["apple", "banana", "cherry"]
    print(type(mylist))

    print(f"\n{'Example 7'}")
    thislist = list(("apple", "banana", "cherry"))
    print(thislist)

    print(f"\n{'Exercise 1'}")
    print("What will be the result of the following syntax:\n",
          "\tmylist = ['apple', 'banana', 'cherry']\n", "\tprint(mylist[1])n")
    print("Ans: banana")

    # subtopic access list items
    print(f"\n{'Example 1'}")
    thislist = ["apple", "banana", "cherry"]
    print(thislist[1])

    print(f"\n{'Example 2'}")
    thislist = ["apple", "banana", "cherry"]
    print(thislist[-1])

    print(f"\n{'Example 2'}")
    thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
    print(thislist[2:5])

    print(f"\n{'Example 3'}")
    thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
    print(thislist[:4])

    print(f"\n{'Example 4'}")
    thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
    print(thislist[2:])

    print(f"\n{'Example 5'}")
    thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
    print(thislist[-4:-1])

    print(f"\n{'Example 6'}")
    thislist = ["apple", "banana", "cherry"]
    if "apple" in thislist:
        print("Yes, 'apple' is in the fruits list")

    print(f"\n{'Exercise 1'}")
    print("What will be the result of the following syntax:\n",
          "\tmylist = ['apple', 'banana', 'cherry']\n", "\tprint(mylist[-1])n")
    print("Ans: cherry")

    # Subtopic change list items
    print(f"\n{'Example 1'}")
    thislist = ["apple", "banana", "cherry"]
    thislist[1] = "blackcurrant"
    print(thislist)

    print(f"\n{'Example 2'}")
    thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
    thislist[1:3] = ["blackcurrant", "watermelon"]
    print(thislist)

    print(f"\n{'Example 3'}")
    thislist = ["apple", "banana", "cherry"]
    thislist[1:2] = ["blackcurrant", "watermelon"]
    print(thislist)

    print(f"\n{'Example 4'}")
    thislist = ["apple", "banana", "cherry"]
    thislist[1:3] = ["watermelon"]
    print(thislist)

    print(f"\n{'Example 5'}")
    thislist = ["apple", "banana", "cherry"]
    thislist.insert(2, "watermelon")
    print(thislist)

    print(f"\n{'Exercise 1'}")
    print("What will be the result of the following syntax:\n",
          "\tmylist = ['apple', 'banana', 'cherry']\n",
          "\tmylist[0] = 'kiwi'\n", "\tprint(mylist[1])n")
    print("Ans: banana")

    # subtopic add list items
    print(f"\n{'Example 1'}")
    thislist = ["apple", "banana", "cherry"]
    thislist.append("orange")
    print(thislist)

    print(f"\n{'Example 2'}")
    thislist = ["apple", "banana", "cherry"]
    thislist.insert(1, "orange")
    print(thislist)

    print(f"\n{'Example 3'}")
    thislist = ["apple", "banana", "cherry"]
    tropical = ["mango", "pineapple", "papaya"]
    thislist.extend(tropical)
    print(thislist)

    print(f"\n{'Example 4'}")
    thislist = ["apple", "banana", "cherry"]
    thistuple = ("kiwi", "orange")
    thislist.extend(thistuple)
    print(thislist)

    print(f"\n{'Exercise 1'}")
    print("What will be the result of the following syntax:\n",
          "\tmylist = ['apple', 'banana', 'cherry']\n",
          "\tmylist.insert(0, 'orange')\n", "\tprint(mylist[1])n")
    print("Ans: apple")

    # Subtopic remove list items
    print(f"\n{'Example 1'}")
    thislist = ["apple", "banana", "cherry"]
    thislist.remove("banana")
    print(thislist)

    print(f"\n{'Example 2'}")
    thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
    thislist.remove("banana")
    print(thislist)

    print(f"\n{'Example 3'}")
    thislist = ["apple", "banana", "cherry"]
    thislist.pop(1)
    print(thislist)

    print(f"\n{'Example 4'}")
    thislist = ["apple", "banana", "cherry"]
    thislist.pop()
    print(thislist)

    print(f"\n{'Example 5'}")
    thislist = ["apple", "banana", "cherry"]
    del thislist[0]
    print(thislist)

    print(f"\n{'Example 6'}")
    thislist = ["apple", "banana", "cherry"]
    del thislist

    print(f"\n{'Example 7'}")
    thislist = ["apple", "banana", "cherry"]
    thislist.clear()
    print(thislist)

    print(f"\n{'Exercise 1'}")
    print("What is a List method for removing list items?")
    print("Ans: pop()")

    # subtopic loop lists
    print(f"\n{'Example 1'}")
    thislist = ["apple", "banana", "cherry"]
    for x in thislist:
        print(x)

    print(f"\n{'Example 2'}")
    thislist = ["apple", "banana", "cherry"]
    for i in range(len(thislist)):
        print(thislist[i])

    print(f"\n{'Example 3'}")
    thislist = ["apple", "banana", "cherry"]
    i = 0
    while i < len(thislist):
        print(thislist[i])
        i = i + 1

    print(f"\n{'Example 4'}")
    thislist = ["apple", "banana", "cherry"]
    [print(x) for x in thislist]

    print(f"\n{'Exercise 1'}")
    print("What is a correct syntax for looping through the items of a list?")
    print("Ans: \n",
          "\tfor x in ['apple', 'banana', 'cherry']:\n\t\t print(x)\n")

    # subtopic list comprehension
    print(f"\n{'Example 1'}")
    fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
    newlist = []
    for x in fruits:
        if "a" in x:
            newlist.append(x)

    print(newlist)

    print(f"\n{'Example 1'}")
    fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
    newlist = [x for x in fruits if "a" in x]
    print(newlist)

    print(f"\n{'Example 1'}")
    newlist = [x for x in fruits if x != "apple"]
    print(newlist)

    print(f"\n{'Example 2'}")
    newlist = [x for x in fruits]
    print(newlist)

    print(f"\n{'Example 3'}")
    newlist = [x for x in range(10)]
    print(newlist)

    print(f"\n{'Example 4'}")
    newlist = [x for x in range(10) if x < 5]
    print(newlist)

    print(f"\n{'Example 5'}")
    newlist = [x.upper() for x in fruits]
    print(newlist)

    print(f"\n{'Example 6'}")
    newlist = ['hello' for x in fruits]
    print(newlist)

    print(f"\n{'Example 7'}")
    newlist = [x if x != "banana" else "orange" for x in fruits]
    print(newlist)

    print(f"\n{'Exercise 1'}")
    print("Consider the following code:",
          "\tfruits = ['apple', 'banana', 'cherry']\n",
          "\tnewlist = [x for x in fruits if x == 'banana']\n",
          "What will be the value of newlist?")
    print("Ans: ['banana']")

    # subtopic sort lists
    print(f"\n{'Example 1'}")
    thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
    thislist.sort()
    print(thislist)

    print(f"\n{'Example 2'}")
    thislist = [100, 50, 65, 82, 23]
    thislist.sort()
    print(thislist)

    print(f"\n{'Example 3'}")
    thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
    thislist.sort(reverse=True)
    print(thislist)

    print(f"\n{'Example 4'}")
    thislist = [100, 50, 65, 82, 23]
    thislist.sort(reverse=True)
    print(thislist)

    print(f"\n{'Example 5'}")

    def myfunc(n):
        return abs(n - 50)

    thislist = [100, 50, 65, 82, 23]
    thislist.sort(key=myfunc)
    print(thislist)

    print(f"\n{'Example 6'}")
    thislist = ["banana", "Orange", "Kiwi", "cherry"]
    thislist.sort()
    print(thislist)

    print(f"\n{'Example 7'}")
    thislist = ["banana", "Orange", "Kiwi", "cherry"]
    thislist.sort(key=str.lower)
    print(thislist)

    print(f"\n{'Example 8'}")
    thislist = ["banana", "Orange", "Kiwi", "cherry"]
    thislist.reverse()
    print(thislist)

    print(f"\n{'Exercise 1'}")
    print("What is a correct syntax for sorting a list?")
    print("Ans: mylist.sort()")

    # subtopic copy lists
    print(f"\n{'Example 1'}")
    thislist = ["apple", "banana", "cherry"]
    mylist = thislist.copy()
    print(mylist)

    print(f"\n{'Example 2'}")
    thislist = ["apple", "banana", "cherry"]
    mylist = list(thislist)
    print(mylist)

    print(f"\n{'Example 3'}")
    thislist = ["apple", "banana", "cherry"]
    mylist = thislist[:]
    print(mylist)

    print(f"\n{'Exercise 1'}")
    print("What is a correct syntax for making a copy of a list?")
    print("Ans: list2 = list1.copy()")

    # subtopic join lists
    print(f"\n{'Example 1'}")
    list1 = ["a", "b", "c"]
    list2 = [1, 2, 3]
    list3 = list1 + list2
    print(list3)

    print(f"\n{'Example 2'}")
    list1 = ["a", "b", "c"]
    list2 = [1, 2, 3]
    for x in list2:
        list1.append(x)

    print(list1)

    print(f"\n{'Example 3'}")
    list1 = ["a", "b", "c"]
    list2 = [1, 2, 3]
    list1.extend(list2)
    print(list1)

    print(f"\n{'Exercise 1'}")
    print("What is a correct syntax for joining list1 and list2 into list3?")
    print("Ans: list3 = list1 + list2")
