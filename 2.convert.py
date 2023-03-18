# Given a linked list with int type node ONLY from 0 to 9, like
# lst0 = Head->1->2->2->1->None, and then other three lists can be generated after
# combinations of any two CONSECUTIVE nodes, such as lst1 = Head->12->2->1
# ->None, lst2 = Head->1->22->1->None, and lst3 = Head->1->2->21->None. Please
# generate a function/method to convert those 4 lists to char type node linked list based on
# corresponding English letter 1 to 'A', 2 to 'B', ... ... 26 to 'Z'. If the number is bigger than
# 26, replace it with '#' character. So outputs will be Head->A->B->B->A->None from
# Head->1->2->2->1->None, Head->L->B->A->None from Head->12->2->1
# ->None, Head->A->V->A->None from Head->1->22->1->None, and Head->A->B
# ->U->None from Head->1->2->21->None.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def convertToIntList(digits):
    head = ListNode()
    curr = head
    for digit in digits:
        if digit.isdigit():
            curr.next = ListNode(int(digit))
            curr = curr.next
        else:
            curr.next = ListNode(int(digit) * 10 + int(digits[digits.index(digit) + 1]))
            curr = curr.next
    return head.next

def convertToCharList(head):
    curr = head
    output = "Head->"
    while curr:
        if 1 <= curr.val <= 26:
            output += chr(curr.val + 64) + "->"
        else:
            output += "#" + "->"
        curr = curr.next
    output += "None"
    print(output)


digits = input("Enter digits separated by space: ").split()
intList = convertToIntList(digits)
convertToCharList(intList)
