import random
lottozahlen=list(range(50))
random.shuffle(lottozahlen)
for i in range(6):
    user_input=input("geben sie die loto zahlen an ")
    user_input=int(user_input)
    if user_input<1:
        print("rong awnser")
        break
    elif user_input>49:
        print("rong awnser")
        break
    elif user_input==lottozahlen:
        print("jackpott")
        break
    else:
        continue







