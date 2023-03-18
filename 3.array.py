# Given an array with positive integer elements, such as arr = {1, 3, 2, 1, 2, 1}, write a
# program to partition it to two subsets (arrays) with equal sum of all elements, like ls1={1,
# 1, 1, 2} and ls2 = {2, 3}, having sum 5 in each array. Notice that the solution may NOT
# be unique, such as ls1={3, 1, 1} and ls2 = {2, 2, 1} are other two subsets to meet
# requirements as well.

def partition(arr, ls1, ls2, target, idx):
    if sum(ls1) == target and sum(ls2) == target:
        return (ls1, ls2)
    if len(ls1) > len(arr)/2 or len(ls2) > len(arr)/2:
        return None
    if sum(ls1) > target or sum(ls2) > target:
        return None
    for i in range(idx, len(arr)):
        if sum(ls1) + arr[i] <= target:
            ls1.append(arr[i])
            res = partition(arr, ls1, ls2, target, i+1)
            if res:
                return res
            ls1.pop()
        if sum(ls2) + arr[i] <= target:
            ls2.append(arr[i])
            res = partition(arr, ls1, ls2, target, i+1)
            if res:
                return res
            ls2.pop()
    return None


arr = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))

total_sum = sum(arr)
if total_sum % 2 == 0:
    result = partition(arr, [], [], total_sum/2, 0)
    if result:
        print("Valid partition found!")
        print("Subset 1:", result[0])
        print("Subset 2:", result[1])
    else:
        print("No valid partition found.")
else:
    print("No valid partition found.")

