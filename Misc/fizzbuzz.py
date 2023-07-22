def solution_0(limit):
    for number in range(1, limit):
        if number % 3 == 0 and number % 5 == 0:
            print("fizzbuzz")
        elif number % 3 == 0:
            print("fizz")
        elif number % 5 == 0:
            print("buzz")
        else:
            print(number)

def solution_1(limit):
    for number in range(1, limit):
        string = ""
        if number % 3 == 0:
            string += "fizz"
        if number % 5 == 0:
            string += "buzz"
        if number % 7 == 0:
            string += "bazz"
        if string == "":
            print(number)
        else:
            print(string)

def solution_2(limit):
    three_counter, five_counter, seven_counter = 0, 0, 0
    for number in range(1, limit):
        three_counter += 1
        five_counter += 1
        seven_counter += 1
        string = ""

        if three_counter >= 3:
            three_counter = 0
            string += "fizz"
        if five_counter >= 5:
            five_counter = 0
            string += "buzz"
        if seven_counter >= 7:
            seven_counter = 0
            string += "bazz"
        print(number if string == "" else string)

def resetting_counter(target):
    number = 0
    while True:
        number += 1
        if number >= target:
            number = 0
            yield True
        else: yield False

def solution_3(limit):
    three_counter = resetting_counter(3)
    five_counter = resetting_counter(5)
    seven_counter = resetting_counter(7)
    for number in range(1, limit):
        string = ""

        if next(three_counter):
            string += "fizz"
        if next(five_counter):
            string += "buzz"
        if next(seven_counter):
            string += "bazz"
        print(number if string == "" else string)

def fizz_map(number):
    match number**4 % 15:
        case 1:
            return number
        case 6:
            return "fizz"
        case 10:
            return "buzz"
        case 0:
            return "fizzbuzz"

def solution_4(limit):
    for number in range(1, limit):
        print(fizz_map(number))

def solution_5(limit):
    results = {
        "1": None,
        "6": "fizz",
        "10": "buzz",
        "0": "fizzbuzz"
    }
    for number in range(1, limit):
        if result := results[str(number**4 % 15)]:
            print(result)
        else: print(number)

def solution_6(limit):
    rules = [
        (3, "fizz"),
        (5, "buzz"),
        (7, "bazz"),
    ]
    for number in range(1, limit):
        string = ""
        for target, result in rules:
            if number % target == 0:
                string += result
        print(number if string == "" else string)
        
def solution_7(limit):
    rules = [
        lambda x: "fizz" if x % 3 == 0 else "",
        lambda x: "buzz" if x % 5 == 0 else "",
        lambda x: "bazz" if x % 7 == 0 else "",
    ]
    for number in range(1, limit):
        string = ""
        for rule in rules:
            string += rule(number)
        print(number if string == "" else string)

solution_7(10000)
