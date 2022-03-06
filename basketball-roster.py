# Basketball Roster App

print("Welcome to the Basketball Roster Program\n")

roster = {}

roster["Point Guard"] = input("Who is your point guard: ").title()
roster["Shooting Guard"] = input("Who is your shooting guard: ").title()
roster["Small Forward"] = input("Who is your small forward: ").title()
roster["Power Forward"] = input("Who is your power forward: ").title()
roster["Center"] = input("Who is your center: ").title()

print(f"\n\tYour starting 5 for the upcoming Basketball Season")
for key,value in roster.items():
  print(f"\t\t{key}:\t\t{value}".expandtabs(4))

