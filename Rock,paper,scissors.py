import random
q=input("Choose rock,paper or scissors ")
rock='''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
'''
paper='''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors='''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
if q=="rock":
    print(rock)
elif q=="paper":
    print(paper)
else:
    print(scissors)

x=random.randint(0,2)
if x==0:
    print(f"computer chose rock: {rock}")
elif x==1:
    print(f"computer chose paper: {paper}")
elif x==2:
    print(f"computer chose scissors: {scissors}")

if q=="rock":
    if x==0:
        print("tie")
    elif x==1:
        print("you lost")
    elif x==2:
        print("you won")
elif q=="paper":
    if x==0:
        print("you won")
    elif x==1:
        print("tie")
    elif x==2:
        print("you lost")
else:
    if x==0:
        print("you lost")
    elif x==1:
        print("you won")
    elif x==2:
        print("tie")

a=input("press enter to close")
