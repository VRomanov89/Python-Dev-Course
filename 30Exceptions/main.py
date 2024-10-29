try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["test"])
except FileNotFoundError:
    open("a_file.txt", "w")
except KeyError:
    print("We have a Key Error?!")