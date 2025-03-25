import datetime
now = datetime.datetime.today()   


print("\t\tWelcome to the age calculator.\n")

print("=============================================================\n")

print("\t          Let's calculate your age \n\n")

name = str(input("Enter your name: "))
birth_year = int(input("Enter your birth year:- "))
birth_month = int(input("Enter your birth month:- "))
birth_day = int(input("Enter your birth day:- "))
print("\n")
current_year = int(input("Enter the current year:- "))
current_month = int(input("Enter the current month:- "))
current_day = int(input("Enter the current day:- "))

Age_year = current_year - birth_year
Age_month = current_month - birth_month
Age_day = current_day - birth_day

# for fixing the negative values
if Age_day < 0:
    Age_month -= 1
    Age_day += 30  # Approximate, assuming month length is 30 days

if Age_month < 0:
    Age_year -= 1
    Age_month += 12


print("\n\t Calculation of your age is processing....\n")
print(f"\n\t {name}, your age is {Age_year} year, {Age_month} months, {Age_day} days years old.\n")
print("\n\t Calculation of your age is completed....\n")

print(str(input("\n\nGive your feedback:- ")))
print("\n\n\t\tThank you for using the age calculator.\n")
