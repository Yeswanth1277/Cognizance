n = int(input('enter the number:'))
a = n
r = 0
while (n>0):
  rem = n % 10
  r = r*10 + rem
  n = n//10
if (a==r):
  print('the given number is a palindrome')
else:
  print('the given number is not a palindrome')