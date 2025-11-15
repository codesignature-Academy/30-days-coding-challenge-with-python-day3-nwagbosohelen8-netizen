jamb_score = int(input("Enter JAMB Score: "))
department = input("Enter Department: ")

if department == "medicine":
    cutoff = 300
elif department == "law":
    cutoff = 250
elif department == "engineering":
    cutoff = 210
elif department == "nursing":
    cutoff = 260
elif department == "computer science":
    cutoff = 180
elif department == "biochemistry":
    cutoff = 200  
elif department == "fishery":
    cutoff = 150
elif department == "accounting":
    cutoff = 220
elif department == "economics":
    cutoff = 180
elif department == "microbiology":
    cutoff = 190
else:
    print("Invalid department entered.")

if jamb_score >= cutoff:
    print(f"Congratulations, you are admitted into {department} department.")
else:
    print("Sorry, you were not admitted.")