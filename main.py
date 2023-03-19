import random

upper = "ABCDEFGHIJKLMNOPRSTWXYZ"
lower = upper.lower()
symbols = "!@#$%^&*?"
digits = "123456890"

up, low, num, sys = True, True, True, True

all = ""

if up:
    all += upper
if low:
    all += lower
if sys:
    all += symbols
if num:
    all += digits


length = random.randint(15,25)
record = 15

for x in range(record):
    password = "".join(random.sample(all, length))
    print(password)
