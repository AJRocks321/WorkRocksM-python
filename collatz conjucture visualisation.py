#collatz conjucture; a way for visualisation
a=1
c=1
b=int(input('give the domain of numbers you want'))
for i in range(1,b):
    p=0
    s=i
    while (s!=1):
        if(s%2==0):
            s=s/2
        else:
            s=3*s+1
        p=p+1
    print(i*a,p*c)
    