#years = input("Enter a number of years and I'll tell you how many minutes that is... ")
#years = int(years)
#days = years * 365
#hours = days * 24
#minutes = hours * 60
#print(years, "years is ", minutes, "minutes")

#I predict the code will complete a series of math problems and then produce the number
#of minutes there are in a number of years

seconds = input("Enter a number of seconds and I'll tell you how many years that is... ")
seconds = int(seconds)
minutes = seconds / 60
hours = minutes / 60
days = hours / 24
years = days / 365
print(seconds, "seconds", years, "years")
