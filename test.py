n = int(input())
for i in range(1,n+1,1):
    if i%2 != 0:
        if i%3==0 or i%5==0:
            if i%3==0:
                print("Solo")
            if i%5==0:
                print("Learn")
            if i%3==0 and i%5==0:
                print("SoloLearn")
        else:
            print(i)
   
   
