"<=less >= grater"
score=int(input("score:"))
if(score<35):
    print("poor student")
elif(score>35 and score<70):
    print("Average student")
elif(score >70 and score <100):
    print("Good student")
elif(score==70):
    print("Good Student")
elif(score==100):
    print("Very Good student ")
elif(score==35):
    print("Average student")
else:
    print("invalid input")
