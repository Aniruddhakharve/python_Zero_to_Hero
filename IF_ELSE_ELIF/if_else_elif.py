import sys

type = sys.argv[1]

if type == "t2.micro":
    print ("you will be charged 2 dollars")
elif type == "t2.medium":
    print ("you will be crged 5 dollars")
elif type == "t2.large":
    print ("you will charge 25 dollars")
else :
    print("you have entered the wrong ec2 instance type")

# list = ["hii" ,  "how" , "are" ,  "you" ]
# print (list[3])