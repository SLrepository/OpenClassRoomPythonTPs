year = int(input("saisissez une année : "))

if not(year % 400) or (not(year % 4) and (year % 100)):
    print("l'annee est bissextile #2")
else:
    print("l'annee n'est pas bissextile #2")

