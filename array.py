
n = int(input("Enter number of elements: "))
arr = []
print("Enter elements:")
for i in range(n):

    num = int(input())
    arr.append(num)
    
print("Reversed array:")
for i in range(n-1, -1, -1):
    print(arr[i], end=" ")