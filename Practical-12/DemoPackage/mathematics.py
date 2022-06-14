def sum_function(*args):
    result = 0
    for arg in args:
        result += arg
    return result


def average(*args):
    sum_ = 0
    for arg in args:
        sum_ += arg
    return sum_ / len(args)


def power(value, power_value):
    return value ** power_value
