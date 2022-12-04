a=int(input("Enter lower number: "))
b=int(input("Enter higher number: "))
countC,countP=0,0
if a<=b:
    for i in range(a,b+1):
        if i >1:
            for j in range(2,i):
                if  i%j ==0:
                    countC == countC+1
                    print(i,"is composite")
                    break
            else:
                countP=countP+1
                print(i,"is prime")
        elif i==1:
            print(i,"is neither prime nor composite")
    print("Count:",countP,"prime and",countC,"composite numbers in range")



