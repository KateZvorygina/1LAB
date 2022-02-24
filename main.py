name = 'KATUSHKA'
print(name)

age = 18
print('Hey, my name is', name, 'and i am', age, 'years old, hehe. I am still young and i am living my best youth.')

namex5 = name*5
print(namex5)

print('what is your name?')

username = input()
if username.isalpha() == False or " " in username:
    print("error! only letters allowed.")
print('What your age?')
userage = int(input())
if userage <= 0:
    print('enter your real age.')
elif userage > 150:
    print('enter your real age.')
print('Hey', username, 'Oooh you are just a baby. You are just', userage, '!')

userage = int(userage)
if userage <= 18:
    massage = 'Xoxo! Okay, i will be waiting for you...'
else:
    message = 'Oh, what are you doing tonight, wanna hang out?'

# print(username[1:])
# print(username[::-1])

a = username[1:]
b = username[::-1]
c = len(username)
d = username[c-3:]
e = username[:5]
print(a, b, d, e)

l = len(username)
sum = int(userage) + l
pr = int(userage) * l
print(sum, l, pr)

u = userage
if u > 9:
    f =(u//10)+(u%10)
    g =(u//10)*(u%10)
else:
    f = u
    g = u
print(f, g)

us = username
h = us.upper()
i = us.lower()
j = us[1:]
k = us[:1]
m = k.upper() + j.lower()
n = k.lower() + j.upper()
print(h, i, m, n)

o = int(input("4*2*3*7*0*82*100*7 = ? \n"))
if o == 0:
    print("Yeaaah, You're right, baby")
else:
    print("Try again, sitting duck")

print('bye,bye')