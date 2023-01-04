#Write a recursive function to reverse a list.

def reverseList(aList):
    if len(aList)== 0:
        return []
    else:
        return [aList[-1]] + reverseList(aList[:-1])

print(reverseList([1,3,7,8]))