def selection(arr):
    n=len(arr)
    for i in range(n-1):
        for j in range(i+1,n):
            if arr[i]>arr[j]:
                arr[i],arr[j]=arr[j],arr[i]
    return arr
arr=[20,9,8,7]
print(selection(arr))            
        