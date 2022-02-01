# with open("a_file.txt") as file:
#     file.read()

try:
    file = open("a_file.txt")
    a_dict = {"key":"value"}
    print(a_dict["fdsjgh"])
except FileNotFoundError:
    file = open("a_file.txt","w")
    file.write("Something")
except KeyError as error_message:
    print(f"The key {error_message} does not exist")
else:
    content = file.read()
    print(content)
finally:
    raise TypeError("This is an error I made up")