import random

liste1=["a","b","c","d","e","f","g"]
liste2=list(range(9))


random_nummber1=random.choice(liste1)
random_nummber2=random.choice(liste2)


print(random_nummber1)
print(random_nummber2)
while True:
    user_input1 = input("gebe eine reihe an von a bis f an")
    user_input2 = input("gebe eine Zeile von 1 bis 10an")
    user_input2=int(user_input2)
    if random_nummber2==user_input2 and user_input1==random_nummber1:
        print("its a hit")
        break
    else:
        print("no hit")
        continue




