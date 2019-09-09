import rsa
import rsa_utils as util

print("Hi, this is an RSA Algorithm, please enter level of encryption, a number in base 2 like: 128,256,512... ")
encryption_level = input()

rsa.init(encryption_level)
n, e = rsa.get_public_keys()


def run():
    not_exit = True
    while not_exit:
        print("\n")
        print_menu()
        selection = input("Enter selection: ")
        print("\n")
        if selection == 1:
            integer = input("Enter integer:")
            encrypted_number = rsa.encrypt(integer, n, e)
            if encrypted_number is None:
                print("message to encrypt must be smaller the public key n, please split message")
                continue
            print("integer after encryption: {}".format(encrypted_number))
            decrypted_number = rsa.decrypt(encrypted_number)
            print("integer after decryption: {}".format(decrypted_number))

        elif selection == 2:
            string = raw_input("Enter string: ")
            string_integer = util.text_to_integer(string)
            encrypted_string_integer = rsa.encrypt(string_integer, n, e)
            if encrypted_string_integer is None:
                print("message to encrypt must be smaller the public key n, please split message")
                continue
            print("string after encryption: {}".format(encrypted_string_integer))
            decrypted_string_integer = rsa.decrypt(encrypted_string_integer)
            decrypted_string = util.integer_to_text(decrypted_string_integer)
            print("string after decryption: {}".format(decrypted_string))

        elif selection == 3:
            print("Public key n = {}".format(n))
            print("Public key e = {}".format(e))

        elif selection == 4:
            not_exit = False

        else:
            print("Selection not defined")


def print_menu():
    print("1. Show Encrypt/Decrypt integer")
    print("2. Show Encrypt/Decrypt string")
    print("3. Show public keys - n,e")
    print("4. Exit")


run()


