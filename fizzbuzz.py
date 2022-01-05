
def fizzbuzz():
    num= int(input("enter the number"))
    for i in range (1,1+num):
        if (i%2 ==0) and (i%5==0):
            print("fizzbuzz")
        
        elif i%2 == 0:
            print("fizz")
            
        elif i%5 == 0:
            print("buzz")
        else:
            print(i)
fizzbuzz()