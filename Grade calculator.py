midterm1 = int(input("Please enter your first midterm exam grade:"))
midterm2 = int(input("Please enter your second midterm exam grade:"))
final = int(input("Lutfen final sınavı notunuzu giriniz:"))

result = (midterm1/100*30)+(midterm2/100*30)+(final/100*40)

if(result >= 90):
    print("Your grade {} AA".format(result))
elif(result >= 85):
    print("Your grade {} BA".format(result))
elif(result >= 80):
    print("Your grade {} BB".format(result))
elif(result >= 75):
    print("Your grade {} CB".format(result))
elif(result >= 70):
    print("Your grade {} CC".format(result))
elif(result >= 65):
    print("Your grade {} DC".format(result))
elif(result >= 60):
    print("Your grade {} DD".format(result))
elif(result >= 50):
    print("Your grade {} FD".format(result))
else:
    print("Your grade {} FF".format(result))
