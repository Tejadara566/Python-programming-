def shell(a):
    n=len(a);gap=n//2
    while gap>0:
        for i in range(gap,n):
            temp=a[i];j=i
            while j>=gap and a[j-gap]>temp:
                a[j]=a[j-gap];j-=gap
            a[j]=temp
        gap//=2
    return a
print(shell([12,34,54,2,3]))