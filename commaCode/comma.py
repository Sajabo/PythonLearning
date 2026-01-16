# Write a functrion that takes a list value as an argument and returns a string with all the items separated by a comma and a space, with 'and' before the last item.
# For example, passing the list ['apples', 'bananas', 'tofu', 'cats'] would return 'apples, bananas, tofu, and cats'. 
# But your function should be able to handle any list value passed to it. 

def comma_code(items):
    if not items:
        return ""
    for i in len(items):
        items[i.append(",")]
    print(items)
