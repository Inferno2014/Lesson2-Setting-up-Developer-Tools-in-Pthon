a = int(input('Enter the First Number: '))
b = int(input('Enter the Second Number: '))
c = int(input('Enter the Third Number: '))
if a>b>c or c>b>a:
    print(b,'is the second largest number')
elif b>a>c or c>b>a:
    print(a,'is the second largest number')
elif a>c>b or b>c>a:
    print(c,'is the second largest number')