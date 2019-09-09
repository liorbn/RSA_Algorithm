str = "abc"
str_to_num = 1
for c in reversed(str):
    str_to_num *= 1000
    str_to_num += ord(c)

print(str_to_num)

while str_to_num != 1:
    print(chr(str_to_num % 1000))
    str_to_num /= 1000

