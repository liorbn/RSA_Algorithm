import rsa

n, e = rsa.get_public_keys()

c = rsa.encrypt(1223, n, e)
m = rsa.decrypt(c)


def text_to_integer(text):
    str_to_num = 1
    for c in reversed(text):
        str_to_num *= 1000
        str_to_num += ord(c)

    return str_to_num

#
def integer_to_text(number):
    string = ""
    while number != 1:
        string += chr(number % 1000)
        number /= 1000

    return string


number = text_to_integer("This is a test for string")
print(number)

encrypted_number = rsa.encrypt(number, n, e)
print(encrypted_number)

decrypted_number = rsa.decrypt(encrypted_number)
print(decrypted_number)

string = integer_to_text(decrypted_number)
print(string)

