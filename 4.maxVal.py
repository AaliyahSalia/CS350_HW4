# Assuming that all int type values are saved in an array, like a = {3, 9, 10, 1, 30, 40}, find
# a function to get maximum value from a[u] – a[v] + a[w] –a[x], where indices must be
# u>v>w>x. (40-1+10-3) will be the result based on given array.

def max_difference(a):
    max_val = float('-inf')
    n = len(a)
    for u in range(n):
        for v in range(u):
            for w in range(v):
                for x in range(w):
                    diff = a[u] - a[v] + a[w] - a[x]
                    if diff > max_val:
                        max_val = diff
    return max_val

a = list(map(int, input("Enter the array elements separated by spaces: ").split()))

max_val = max_difference(a)

print("Maximum value of a[u] - a[v] + a[w] - a[x]:")
print(max_val)
