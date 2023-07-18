# add your code here
list = range(1,101,1)
for i in list:
    #print(i)
    if i % 3 == 0 and i % 5 == 0:
        i = 'FizzBuzz'
    #print(i)
    elif i % 3 == 0:
        i = 'Fizz'
    elif i % 5 == 0:
        i = 'Buzz'
    print(i)
