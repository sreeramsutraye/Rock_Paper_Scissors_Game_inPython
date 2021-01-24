import random
a = ['Heads','Tails']
x = input("Heads or Tails")
y = random.choice(a)
if x.title() == y.title():
    print('You win')
else:
    print('You Lose')
