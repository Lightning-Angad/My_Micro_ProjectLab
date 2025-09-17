import os
import time
pointA = pointB = pointC = pointD = pointE = pointF = pointG = 0
print("----------Welcome to the Miniature Quiz Contest----------")
time.sleep(0.5)
name=input("Enter your super name: ")
time.sleep(0.5)
print("Rules:\n1. Choose only the alphabet (whether capital or small) as denoted.\n2. Wrong inputs may decrease your progess.\n3. This quiz is of 7 questions. So, PLAY FAIR !\n")
time.sleep(2)
num=input("Press S to Start or E to Exit: ")
time.sleep(0.5)
if (num=="S" or num=="s"):
    print("[Question-1]\nWhat is the nickname of the Indian freedom fighter 'Subash Chandra Bose' ?")
    print("Option-A: Mahatma\nOption-B: Netaji\nOption-C: Raja\nOption-D: Tiger")
    ans1=input("Enter: ")
    if (ans1=="B" or ans1=="b"):
        print("Correct")
        pointA=1
        time.sleep(2)
    else:
        print("Incorrect")
        pointA=0
        time.sleep(2)
    print("------------------------------------")
    print("[Question-2]\nHow many bones are present in an adult human body ?")
    print("Option-A: 206\nOption-B: 300\nOption-C: 217\nOption-D: 201")
    ans2=input("Enter: ")
    if (ans2=="A" or ans2=="a"):
        print("Correct")
        pointB=1
        time.sleep(2)
    else:
        print("Incorrect")
        pointB=0
        time.sleep(2)
    print("------------------------------------")
    print("[Question-3]\nWhat is the name of our galaxy ?")
    print("Option-A: S-200 Galaxy\nOption-B: Bermuda Galaxy\nOption-C: Y4-8S00 Galaxy\nOption-D: Milky-Way Galaxy")
    ans3=input("Enter: ")
    if (ans3=="D" or ans3=="d"):
        print("Correct")
        pointD=1
        time.sleep(2)
    else:
        print("Incorrect")
        pointD=0
        time.sleep(2)
    print("------------------------------------")
    print("[Question-4]\nWho proposed 'The Theory of Special Relativity' ?")
    print("Option-A: Galileo Galilei\nOption-B: Issac Newton\nOption-C: Albert Einstein\nOption-D: Jagadish Ch. Bose")
    ans4=input("Enter: ")
    if (ans4=="C" or ans4=="c"):
        print("Correct")
        pointC=1
        time.sleep(2)
    else:
        print("Incorrect")
        pointC=0
        time.sleep(2)
    print("------------------------------------")
    print("[Question-5]\nWhat is the total circumference of our planet Earth ?")
    print("Option-A: 100,000km\nOption-B: 40,000km\nOption-C: 50,000km\nOption-D: 95,000km")
    ans1=input("Enter: ")
    if (ans1=="B" or ans1=="b"):
        print("Correct")
        pointE=1
        time.sleep(2)
    else:
        print("Incorrect")
        pointE=0
        time.sleep(2)
    print("------------------------------------")
    print("[Question-6]\nWhat is the chemical name of 'Common Salt' ?")
    print("Option-A: Sodium Hypochloride\nOption-B: Ethanol\nOption-C: Sulphur Dioxide\nOption-D: Sodium Chloride")
    ans1=input("Enter: ")
    if (ans1=="D" or ans1=="d"):
        print("Correct")
        pointF=1
        time.sleep(2)
    else:
        print("Incorrect")
        pointF=0
        time.sleep(2)
    print("------------------------------------")
    print("[Question-7]\nWhich one of these is an example of operating system ?")
    print("Option-A: Kali Linux\nOption-B: BGMI\nOption-C: Instagram\nOption-D: Power BI")
    ans1=input("Enter: ")
    if (ans1=="A" or ans1=="a"):
        print("Correct")
        pointG=1
        time.sleep(2)
    else:
        print("Incorrect")
        pointG=0
        time.sleep(2)
    print("------------------------------------")
elif (num=="E" or num=="e"):
    exit (0)
else:
    print("Invalid Input")
    exit (0)
score=pointA+pointB+pointC+pointD+pointE+pointF+pointG
print(name,"Your Total Score is: ", score)
print("Hope. You liked this game !!")