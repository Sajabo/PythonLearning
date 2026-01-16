# Write a function that takes a list value as an argument and returns a string with all the items separated by a comma and a space, with 'and' before the last item.
# For example, passing the list ['apples', 'bananas', 'tofu', 'cats'] would return 'apples, bananas, tofu, and cats'. 
# But your function should be able to handle any list value passed to it. 

def comma_code(items):
    if not items:
        return ""
    if len(items) == 1:
        return items[0]
    if len(items) == 2:
        return " and ".join(items)
    
    # first_part will get every element except the last one using slicing. In this case, slicing is items[start:stop] so for
    # the function, items[0:last item]. The stop is non-inclusive so it stops at the last item. [0:-2] would be from start to second to last.
    first_part = items[:-1]
    first_str = ', '.join(first_part)
    last_item = items[-1]
    result = first_str + ", and " + last_item
    return result
    

things = ['apples', 'ball', 'red', 'orange']
print(comma_code(things))

