trial = input("What free trial do you want to be reminded about? ")
date = input("When does your free trial end? E.g. 06/21/21:  ")
print("")
sender = input("Enter your email: ")
pw = input("Enter password to email: ")
with open("trial.txt", "w") as f:
    f.write(trial)
    
with open("date.txt", "w") as f:
    f.write(date)












