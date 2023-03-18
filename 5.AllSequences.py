# Given a positive number N, 2*N elements from 1 to N can be created in a list, such as
# N=3, and list will be 1, 1, 2, 2, 3, 3 with two appearances of 1s, 2s and 3s. Write a
# program to find all sequences between its two appearances with required distance, which
# is exactly equal to value of the element. 


def find_sequences(N, lst):
    sequences = []
    for i in range(1, N+1):
        first_idx = lst.index(i)
        second_idx = lst.index(i, first_idx+1)
        for j in range(first_idx+1, second_idx):
            distance = j - first_idx
            if lst[j] - i == distance:
                valid_sequence = [i]
                for k in range(j+1, second_idx):
                    if lst[k] - valid_sequence[-1] == 1:
                        valid_sequence.append(lst[k])
                if len(valid_sequence) == second_idx - j:
                    sequences.append(valid_sequence)
    return sequences

N = 3
lst = [1, 1, 2, 2, 3, 3]
sequences = find_sequences(N, lst)
print(sequences)
