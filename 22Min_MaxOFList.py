lst=eval(input("enter the list of integers only "))
def find_min_max(lst):
    if len(lst) == 0:
        return None, None  # Return None if the list is empty
    min_val = min(lst)
    max_val = max(lst)
    return min_val, max_val

num1,num2=find_min_max(lst)
print("the minimum value is ",num1)
print("the maximum value is ",num2)
