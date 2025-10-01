
def ex_1_1():
    card1, card2, card3, card4, card5 = 4, 2, 7, 1, 11
    result=card1 + card2 + card3 + card4 + card5
    return result


def ex_1_2():
    card1, card2, card3, card4, card5 = 4, 2, 7, 1, 11
    total = card1 + card2 + card3 + card4 + card5
    return "busted" if total > 21 else "safe"

def ex_1_3():
    card1, card2, card3 = 4, 2, 7
    total = card1 + card2 + card3
    if total < 21:
        return "safe"
    elif total > 21:
        return "busted"
    else:
        return "Black Jack"
    
    raise NotImplementedError("Exercise 1.3 not implemented")


def ex_1_4():
    """
    Exercise 1.4 (2p)
    Create dealer1, dealer2, dealer3 = 1, 6, 7.
    Add the variables togheter, use the result to
    decide what the dealer should do:
      - sum < 17        -> "pick"
      - 17 <= sum < 21  -> "stop"
      - sum == 21       -> "black jack"
      - sum > 21        -> "busted"
      Return the answers
    """
    dealer1, dealer2, dealer3 = 1, 6, 7
    total = dealer1 + dealer2 + dealer3
    if total < 17:
        return "pick"
    elif 17 <= total < 21:
        return "stop"
    elif total == 21:
        return "black jack"
    else:
        return "busted"
    raise NotImplementedError("Exercise 1.4 not implemented")


def ex_2_1():
    """
    Exercise 2.1 (1p)
    Create a variable my_fruit and set it to "plum".
    Use match/case (Python 3.10+) to build a text about the fruit's color:
      - banana -> "The banana is yellow."
      - apple  -> "The apple is green."
      - kiwi   -> "The kiwi is green."
      - plum   -> "The plum is purple."
    """
    my_fruit = "plum"
    match my_fruit:
        case "banana":
            return "The banana is yellow"
        case "apple":
            return "The apple is green"
        case "kiwi":
            return "The kiwi is green"
        case "plum":
            return "The plum is purple"
    raise NotImplementedError("Exercise 2.1 not implemented")


def ex_2_2():
    """
    Exercise 2.2 (1p)
    Extend match/case with a default (case _).
    Set my_fruit = "pear" and return:
      "That is an unknown fruit."
    """
    my_fruit = "pear"
    match my_fruit:
        case "banana":
            return "The banana is yellow"
        case "apple":
            return "The apple is green"
        case "kiwi":
            return "The kiwi is green"
        case "plum":
            return "The plum is purple"
        case _:
            return "That is an unknown fruit"
    raise NotImplementedError("Exercise 2.2 not implemented")


def ex_3_1():
    """
    Exercise 3.1 (1p)
    Use a for-loop to increase 481 by 6 ten times.
    Return the result.
    """
    number = 481
    for _ in range(10):
        number += 6
    return number
    raise NotImplementedError("Exercise 3.1 not implemented")


def ex_3_2():
    """
    Exercise 3.2 (1p)
    Use a for-loop to decrease 551 by 8 ten times.
    Return the result.
    """
    number = 551
    for _ in range(10):
        number -= 8
    return number
    raise NotImplementedError("Exercise 3.2 not implemented")


def ex_3_3():
    """
    Exercise 3.3 (3p)
    Use a for-loop to build a string with all even numbers in the range
    22..45, separated by commas. No extra comma at the end.
    """
    numbers = []
    for i in range(22, 46):
        if i % 2 == 0:
            numbers.append(str(i))
    return ",".join(numbers)
    raise NotImplementedError("Exercise 3.3 not implemented")


def ex_4_1():
    """
    Exercise 4.1 (1p)
    Use a while-loop to increase 10 by 6 until the value is at least 481.
    Return the number of steps.
    """
    value = 10
    steps = 0
    while value < 481:
        value += 6
        steps += 1
    return steps
    raise NotImplementedError("Exercise 4.1 not implemented")


def ex_4_2():
    """
    Exercise 4.2 (1p)
    Use a while-loop to subtract 8 from 551 until the value is <= 0.
    Return the number of steps.
    """
    value = 551
    steps = 0
    while value > 0:
        value -= 8
        steps += 1
    return steps
    raise NotImplementedError("Exercise 4.2 not implemented")


def ex_4_3():
    """
    Exercise 4.3 (3p)
    Use a while-loop to create a comma-separated string of all numbers
    between 28..63 that are divisible by 5 or 7.
    """
    numbers = []
    i = 28
    while i <= 63:
        if i % 5 == 0 or i % 7 == 0:
            numbers.append(str(i))
        i += 1
    return ",".join(numbers)
    raise NotImplementedError("Exercise 4.3 not implemented")

def _run_and_print(fn, label):
    try:
        result = fn()
        print(f"{label}: {result}")
    except NotImplementedError:
        print(f"{label}: (not implemented)")


def main():
    print("Running Lab exercises...\n")
    _run_and_print(ex_1_1, "1.1")
    _run_and_print(ex_1_2, "1.2")
    _run_and_print(ex_1_3, "1.3")
    _run_and_print(ex_1_4, "1.4")
    _run_and_print(ex_2_1, "2.1")
    _run_and_print(ex_2_2, "2.2")
    _run_and_print(ex_3_1, "3.1")
    _run_and_print(ex_3_2, "3.2")
    _run_and_print(ex_3_3, "3.3")
    _run_and_print(ex_4_1, "4.1")
    _run_and_print(ex_4_2, "4.2")
    _run_and_print(ex_4_3, "4.3")


if __name__ == "__main__":
    main()