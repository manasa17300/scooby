import random
count=0
while(count<=100):
    roll=input("press r to roll a dice")
    if  roll=='r': 
        r=random.randint(1,6)
        count=count+r
        print("your random number is ",r)
        print("you are in position",count)
        print(r)
    if  count==100:
        print("you win")
        break
    elif  count==8:
          count=37
          print("move towards 37",count)
          print("continue playing")
    elif  count==11:
          count=2
          print("snake bit oops",count)
    elif  count==13:
          count=34
          print("move towards 34",count)
    elif  count==25:
          count=4
          print("oops snake bit",count)
    elif  count==38:
          count=9
          print("oh no",count)
    elif  count==40:
          count=68
          print("move towards 68",count)
    elif  count==52:
          count=81
          print("woahh move towards 81",count)
    elif  count==65:
          count=46
          print("ouchhh",count)
    elif  count==76:
          count=97
          print("yayyy move towards 97",count)
    elif  count==89:
          count=70
          print("go back to 70",count)
    elif  count==93:
          count=64
          print("oh no go back to 64",count)      
    elif  count==99:
          print("you're almost there",count)
    if    count>100:
          count=count-r
          print("your number is greater than 100 try again")
          


                                                    
