#East african voting
citizenship = input("Enter the citizenship: ")
age = int(input("Enter the age: "))

if age >=18 and citizenship in ["kenyan", "ugandan", "tanzanian"]:
    print("The person is eligible to vote.")
else:
    print("Try next year.")
