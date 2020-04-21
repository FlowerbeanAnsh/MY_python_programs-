import string
p=string.punctuation
t=input("enter something:")
new=" "
for i in t:
    if i not in p:
        new+=i
print(new)
