book_name = input()
counter = 0
is_found = False

input_line = input()
while input_line != "No More Books":
    if book_name == input_line:
        is_found = True
        break

    counter += 1
    input_line = input()

if is_found:
    print(f"You checked {counter} books and found it.")
else:
    print("The book you search is not here!")
    print(f"You checked {counter} books.")