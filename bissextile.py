year = input("Bissextile ou pas ?")
year = int(year)
bis  = False

if year % 4 == 0 and year % 100 != 0 or (year % 400 == 0):
    bis = True
else:
    bis = False

if bis:
    print("oui")
else:
    print("non")
