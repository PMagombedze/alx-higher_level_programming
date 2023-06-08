#!/usr/bin/python3
if __name__ == "__main__":
    """args"""
    from sys import argv
ac = len(argv)
if ac <= 1:
    print("{} arguments.".format(ac - 1))
else:
    if ac == 2:
        print("{} argument:".format(ac - 1))
    else:
        print("{} arguments:".format(ac - 1))
    for i in range(1, ac):
        print("{}: {}".format(i, argv[i]))
