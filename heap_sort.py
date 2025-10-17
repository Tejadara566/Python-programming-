def heapify(a,n,i):
    largest=i; l=2*i+1; r=2*i+2
    if l<n and a[l]>a[largest]: largest=l
    if r<n and a[r]>a[largest]: largest=r
    if largest!=i:
        a[i],a[largest]=a[largest],a[i]
        heapify(a,n,largest)
def heapsort(a):
    n=len(a)
    for i in range(n//2-1,-1,-1): heapify(a,n,i)
    for i in range(n-1,0,-1):
        a[0],a[i]=a[i],a[0]
        heapify(a,i,0)
    return a
print(heapsort([12,11,13,5,6,7]))