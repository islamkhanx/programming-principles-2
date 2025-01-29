if __name__ == "__main__":
    # subtopic python dictiionaries
    print(f"\n{'Example 1'}")
    thisdict = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }
    print(thisdict)

    print(f"\n{'Example 2'}")
    thisdict = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }
    print(thisdict["brand"])

    print(f"\n{'Example 3'}")
    thisdict = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964,
        "year": 2020
    }
    print(thisdict)

    print(f"\n{'Example 4'}")
    print(len(thisdict))

    print(f"\n{'Example 5'}")
    thisdict = {
        "brand": "Ford",
        "electric": False,
        "year": 1964,
        "colors": ["red", "white", "blue"]
    }

    print(f"\n{'Example 6'}")
    thisdict = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }
    print(type(thisdict))

    thisdict = dict(name="John", age=36, country="Norway")
    print(thisdict)

    print(f"\n{'Exercise 1'}")
    print("Which one of these is a dictionary?")
    print("Ans: \n\tx = {'type' : 'fruit', 'name' : 'banana'}")

    # Subtopic access items
    print(f"\n{'Example 1'}")
    thisdict = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }
    x = thisdict["model"]
    print(x)

    print(f"\n{'Example 2'}")
    x = thisdict.get("model")
    print(x)

    print(f"\n{'Example 3'}")
    x = thisdict.keys()
    print(x)

    print(f"\n{'Example 4'}")
    car = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }
    x = car.keys()
    print(x)  # before the change
    car["color"] = "white"
    print(x)  # after the change

    print(f"\n{'Example 5'}")
    x = thisdict.values()
    print(x)

    print(f"\n{'Example 6'}")
    car = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }
    x = car.values()
    print(x)  # before the change
    car["year"] = 2020
    print(x)  # after the change

    print(f"\n{'Example 7'}")
    car = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }
    x = car.values()
    print(x)  # before the change
    car["color"] = "red"
    print(x)  # after the change

    print(f"\n{'Example 8'}")
    x = thisdict.items()
    print(x)

    print(f"\n{'Example 9'}")
    car = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }
    x = car.items()
    print(x)  # before the change
    car["year"] = 2020
    print(x)  # after the change

    print(f"\n{'Example 10'}")
    car = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }
    x = car.items()
    print(x)  # before the change
    car["color"] = "red"
    print(x)  # after the change

    print(f"\n{'Example 11'}")
    thisdict = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }
    if "model" in thisdict:
        print("Yes, 'model' is one of the keys in the thisdict dictionary")

    print(f"\n{'Exercise 1'}")
    print("True or False.",
          "You can access item values by referring to the key name.")
    print("Ans: True")

    # Subtopic change items
    print(f"\n{'Example 1'}")
    thisdict = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }
    thisdict["year"] = 2018

    print(f"\n{'Example 2'}")
    thisdict = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }
    thisdict.update({"year": 2020})

    print(f"\n{'Exercise 1'}")
    print("Consider the following code:\n",
          "\tx = {'type' : 'fruit', 'name' : 'banana'}\n",
          "What is a correct syntax for changing the type from fruit to berry?"
          )
    print("Ans: x['type'] = 'berry'")

    # Subtopic add items
    print(f"\n{'Example 1'}")
    thisdict = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }
    thisdict["color"] = "red"
    print(thisdict)

    thisdict = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }
    thisdict.update({"color": "red"})
    print(f"\n{'Exercise 1'}")
    print("Which one of these dictionary methods",
          "can be used to add items to a dictionary?"
          )
    print("Ans: update()")

    # Subtopic remove items
    print(f"\n{'Example 1'}")
    thisdict = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }
    thisdict.pop("model")
    print(thisdict)

    print(f"\n{'Example 2'}")
    thisdict = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }
    thisdict.popitem()
    print(thisdict)

    print(f"\n{'Example 3'}")
    thisdict = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }
    del thisdict["model"]
    print(thisdict)

    print(f"\n{'Example 4'}")
    thisdict = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }
    del thisdict
    print(thisdict)

    print(f"\n{'Example 5'}")
    thisdict = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }
    thisdict.clear()
    print(thisdict)

    print(f"\n{'Exercise 1'}")
    print("What is a dictionary method",
          "for removing an item from a dictionary?"
          )
    print("Ans: pop()")

    # Subtopic loop dicitonaries
    print(f"\n{'Example 1'}")
    for x in thisdict:
        print(x)

    print(f"\n{'Example 2'}")
    for x in thisdict:
        print(thisdict[x])

    print(f"\n{'Example 3'}")
    for x in thisdict.values():
        print(x)

    print(f"\n{'Example 4'}")
    for x in thisdict.keys():
        print(x)

    print(f"\n{'Example 5'}")
    for x, y in thisdict.items():
        print(x, y)

    print(f"\n{'Exercise 1'}")
    print("What is a correct syntax for looping",
          "through the values of this dictionary:\n"
          "\tx = {'type' : 'fruit', 'name' : 'apple'}"
          )
    print("Ans: \n\tfor y in x.values():\n\t\tprint(y)")

    # Subtopic copy dicitonaries
    print(f"\n{'Example 1'}")
    thisdict = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }
    mydict = thisdict.copy()
    print(mydict)

    print(f"\n{'Example 2'}")
    thisdict = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }
    mydict = dict(thisdict)
    print(mydict)

    print(f"\n{'Exercise 1'}")
    print("What is a correct syntax for making a copy of this dictionary:",
          "\n\tx = {'type' : 'fruit', 'name' : 'apple'}")
    print("Ans: y = x.copy()")

    # subtopic nested dictionaries
    print(f"\n{'Example 1'}")
    myfamily = {
        "child1": {
            "name": "Emil",
            "year": 2004
        },
        "child2": {
            "name": "Tobias",
            "year": 2007
        },
        "child3": {
            "name": "Linus",
            "year": 2011
        }
    }

    print(f"\n{'Example 2'}")
    child1 = {
        "name": "Emil",
        "year": 2004
    }
    child2 = {
        "name": "Tobias",
        "year": 2007
    }
    child3 = {
        "name": "Linus",
        "year": 2011
    }
    myfamily = {
        "child1": child1,
        "child2": child2,
        "child3": child3
    }
    print(f"\n{'Example 3'}")
    print(myfamily["child2"]["name"])

    print(f"\n{'Example 4'}")
    for x, obj in myfamily.items():
        print(x)
        for y in obj:
            print(y + ':', obj[y])

    print(f"\n{'Exercise 1'}")
    print("Consider this syntax:",
          "\n\ta = {'name' : 'John', 'age' : '20'}\n",
          "\n\tb = {'name' : 'May', 'age' : '23'}\n",
          "\n\tcustomers = {'c1' : a, 'c2' : b}\n",
          "what will be a correct syntax for printing the name 'May'?"
          )
    print("Ans: print(customers['c2']['name']")
