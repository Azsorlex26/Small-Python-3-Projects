def AND(one, two):
    return one and two

def OR(one, two):
    return one or two

def NOT(input):
    return not input

def NAND(one, two):
    return NOT(AND(one, two))

def NOR(one, two):
    return NOT(OR(one, two))

def XOR(one, two):
    return AND(OR(one, two), NAND(one, two))

def XNOR(one, two):
    return NOT(XOR(one, two))

def test_function(function):
    print(function)
    for x in range(0, 2):
        x = x == 1

        for y in range(0, 2):
            y = y == 1

            print('x:', x, '\ty:', y, '\tx y:', function(x, y))

    print()

test_function(AND)
test_function(OR)
print(NOT)
print(False, NOT(False))
print(True, NOT(True), '\n')
test_function(NAND)
test_function(NOR)
test_function(XOR)
test_function(XNOR)
