def text_to_integer(text):
    str_to_num = 1
    for c in reversed(text):
        str_to_num *= 1000
        str_to_num += ord(c)

    return str_to_num


def integer_to_text(number):
    string = ""
    while number != 1:
        string += chr(number % 1000)
        number /= 1000

    return string