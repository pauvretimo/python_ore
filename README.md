# python_ore

This is a simple implementation of an Order Revealing Encryption mainly inspired bypython
[kpatsakis/OrderRevealingEncryptio](https://github.com/kpatsakis/OrderRevealingEncryption) 
and [this lesson](https://icerm.brown.edu/materials/Slides/tw19-1-es/Order-Revealing_Encryption_-_Definitions,_Constructions,_and_Challenges_]_David_Wu,_University_of_Virginia.pdf)

# Small test

```python
from Crypto.Random.random import randint

def int_comp(u, v):
    if u == v:
        return 0
    elif u > v:
        return 1
    else:
        return -1

passwd = 'test'
ore = ORE(passwd, 20)
num1 = randint(2**4, 2**16)
num2 = randint(2**4, 2**16)

a = ore.encode(num1)
b = ore.encode(num2)

c1 = ore.decode(a)
c2 = ore.decode(b)

print(num1)
print()
print(num2)
print()
print(ore.compare(a, b) == int_comp(num1, num2))
```
