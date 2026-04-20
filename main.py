def i(arr):
    n=len(arr)
    for i in range(1,n):
        n=len
        curr=arr[i]
        j=i-1
        while j>=0 and arr[j]>curr:
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=curr
    return arr
arr=[12,11,13,5,6]
print(i(arr))            
        
            