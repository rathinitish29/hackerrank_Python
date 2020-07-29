#If n is odd, print Weird
#If n  is even and in the inclusive range of 2 to 5, print Not Weird
#If n  is even and in the inclusive range of 6 to20 , print Weird
#If n is even and greater than20 , print Not Weird

#1
n = int(input('Enter no :'))
if n%2 !=0 :
    print('Weird')
elif n%2 == 0 and 2<= n <=5 :
    print('Not Weird')
elif n%2 == 0 and 6<= n <=20 :
    print('Weird')
elif n%2 == 0 and n>20 :
    print('Not Weird')


#2

n = int(input())
if n%2==1 :
    print("Weird")
elif n%2==0 and 2<=n<=5 :
    print("Not Weird")
elif n%2==0 and 6<=n<=20 :
    print("Weird")
elif n%2==0 and n>20 :
    print("Not Weird")
