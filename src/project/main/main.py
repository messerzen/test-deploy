import sys

sys.path.append("C:/git/testing-integriry/modules_zen")
# print(sys.path)

from modules_zen.calculator import *

def mySum(a, b):
    return sum(a, b)

if __name__ == '__main__':
    print(mySum(10,1))

