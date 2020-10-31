# Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order.
# Essentially, rearrange the digits to create the highest possible number.

#   Examples:
#   Input: 42145 Output: 54421
#   Input: 145263 Output: 654321
#   Input: 123456789 Output: 987654321

def descending_order(num):
    ans = [int(i) for i in str(num)]          #Seperate the input num to list(int). Ex: Input:123 -> [1,2,3]
    ans.sort(reverse=True)                    #Sort and reverse the list.
    return int(''.join(str(x) for x in ans))  #Use join with for loop to print the answer.
    
#  The more clever way:
def Descending_Order(num):
    return int("".join(sorted(str(num), reverse=True)))
