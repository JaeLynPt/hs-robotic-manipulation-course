def fb(n):
    x = 1
    while x < n:
        if(x%5 == 0 and x%3 ==0):
            print("fizzbuzz")
        elif(x%5 == 0):
            print("buzz")
        elif(x%3 == 0):
            print("fizz")
        else:
            print(x)
        x+=1
    return x
fb(15)