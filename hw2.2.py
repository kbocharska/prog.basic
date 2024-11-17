def to_dec(value, base):
    counter = 1
    decimal = 0
    values = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}
    for digit in value:
        if digit in values:
            digit = values[digit]
        decimal += int(digit) * base ** (len(value) - counter)
        counter += 1
    return decimal

def from_dec(value, base):
    product = ""
    values = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
    value = int(value)
    while value != 0:
        digit = value % base
        if digit in values:
            digit = values[digit]
        product = str(digit) + product
        value //= base
    return product


def system_check(value):
    if not "x" in value:
        return False
    i = value.index("x")
    if len(value) - i - 1 > 2 or len(value) - i - 1 < 1:
        return False
    elif len(value) - i - 1 == 1:
        if value[-1] == "1" or value[-1] == "0" or not value[-1].isdecimal():
            return False
    else:
        if not value[-1].isdecimal() or not value[-2].isdecimal():
            return False
        else:
            if int(value[i+1:]) > 16:
                return False
    return True

def validation(value):
    if not system_check(value):
        return False
    i = value.index("x")
    base = int(value[i+1:])
    value = value[:i]
    if base <= 10:
        if not value.isdecimal():
            return False
        for digit in value:
            if not int(digit) < base:
                return False
    else:
        letters = ["A", "B", "C", "D", "E", "F"]
        available_letters = []
        for item in letters:
            if letters.index(item) < base-10:
             available_letters.append(item)
        for digit in value:
            if not digit in available_letters and not digit.isdecimal():
                return False
    return True

def sys_validation(value):
    if not value.isdecimal():
        return False
    else:
        value = int(value)
        if value < 2 or value > 16:
            return False
    return True




while True:
    number_raw = input("enter your number ")
    while not validation(number_raw):
        number_raw = input("try again ")

    ind = number_raw.index("x")
    input_system = int(number_raw[ind + 1:])

    output_system = input("enter desired output system ")
    while not sys_validation(output_system):
        output_system = input("try again ")
    output_system = int(output_system)

    if input_system == output_system:
        print(f"the result is {number_raw}")
        continue

    number = number_raw[:ind]
    if input_system != 10:
        number = to_dec(number, input_system)
    if output_system != 10:
        number = from_dec(number, output_system)
    number = str(number) + "x" + str(output_system)

    print(f"{number_raw} in base {output_system} is {number}")

    decision = input("do you want to stop? (y or n) ")
    if decision == "y":
        break