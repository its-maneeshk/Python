#Integer Palindrome
reverse=0
initial_number=int(input('Enter any number to check Palindrome: '))
while(initial_number!=0):
    last_digit=initial_number%10
    reverse=reverse*10+last_digit
    initial_number=initial_number//10
if (reverse==initial_number):
    print('Given integer is Palindrome.')
else:
    print('Given integer is Not Palindrome.')    


#String Palindrome
initial_string=input("Enter string: ")
reverse_of_string=initial_string[::-1]
if (reverse_of_string==initial_string):
    print('Given string is Palindrome.')
else:
    print('Given string is Not Palindrome.')

