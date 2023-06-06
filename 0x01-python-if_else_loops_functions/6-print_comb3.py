#!/usr/bin/python3
for a in (
    list(range(10))
    + list(range(12, 20))
    + list(range(23, 30))
    + list(range(34, 40))
):
    print("{:02}".format(a), end=", ")
for b in (
    list(range(45, 50))
    + list(range(56, 60))
    + list(range(67, 70))
    + list(range(78, 80))
):
    print("{}".format(b), end=", ")
print("{}".format(89))
