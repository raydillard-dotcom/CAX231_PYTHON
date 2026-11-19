#The existing employee list
employees = [
    "Maya Lin",
    "Marcus Vance",
    "Elena Rostova",
    "David Kim",
    "Sarah Jenkins",
    "Carlos Mendez",
    "Priya Patel",
    "Liam O'Connor",
    "Hannah Abbott",
    "Jamal Washington",
    "Chloe Dubois",
    "Kenji Takahashi",
    "Rachel Goldberg",
    "Tariq Al-Mansoor",
    "Sofia Rossi",
    "Nathan Brooks",
    "Amara Okafor",
    "Lucas Lindqvist",
    "Jessica Alvarez",
    "Owen Gallagher"
]

#The new employee to check and add
new_employee = "Raymond Dillard-Frazier"

#Check if the employee is missing.
if new_employee not in employees:
    employees.append(new_employee)

#Print the updated list
print(employees)