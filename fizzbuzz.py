Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#fizzbuzz
for i in range(101):
    if i % 3 == 0 and i % 5 == 0:
        print('fizzbuzz')
    elif i % 3 == 0 and i % 5 != 0:
        print('fizz')
    elif i % 3 != 0 and i % 5 == 0:
        print('buzz')
    else:
        print(i)
