movie = input()

standard_tickets = 0
kids_tickets = 0
student_tickets = 0
total_tickets = 0
seats_taken = 0

while movie != "Finish":
    free_places = int(input())
    type_ticket = input()

    while type_ticket != "End":
        if type_ticket == 'standard':
            standard_tickets += 1
        elif type_ticket == 'kid':
            kids_tickets += 1
        elif type_ticket == 'student':
            student_tickets += 1
        seats_taken += 1
        if free_places <= seats_taken:
            break
        type_ticket = input()
    print(f"{movie} - {(seats_taken / free_places * 100):.2f}% full.")
    seats_taken = 0
    movie = input()
    total_tickets = standard_tickets + kids_tickets + student_tickets

print(f"Total tickets: {total_tickets}")
print(f"{(student_tickets / total_tickets * 100) :.2f}% student tickets.")
print(f"{(standard_tickets / total_tickets * 100) :.2f}% standard tickets.")
print(f"{(kids_tickets / total_tickets * 100) :.2f}% kids tickets.")

