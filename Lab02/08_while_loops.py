if __name__ == "__main__":
    # subtopic python dictiionaries
    print(f"\n{'Example 1'}")
    i = 1
    while i < 6:
        print(i)
        i += 1

    print(f"\n{'Example 2'}")
    i = 1
    while i < 6:
        print(i)
        if i == 3:
            break
        i += 1

    print(f"\n{'Example 3'}")
    i = 0
    while i < 6:
        i += 1
        if i == 3:
            continue
        print(i)

    print(f"\n{'Example 4'}")
    i = 1
    while i < 6:
        print(i)
        i += 1
    else:
        print("i is no longer less than 6")

    print(f"\n{'Exercise 1'}")
    print("Which statement is a correct syntax to break out of a loop?")
    print("Ans: break")

    