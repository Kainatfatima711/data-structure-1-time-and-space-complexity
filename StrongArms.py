number = int(input("Enter your number: "))

digits = len(str(number))

result_number = 0

temp = number

while temp > 0 :

    digit = temp % 10
    result_number = result_number + digit ** digits
    temp = temp // 10

#Display the result
if number == result_number:
    print(number , "is an Armstrong number")
else:
    print(number , "is not an Armstrong number")