str= input("Enter a string: ")
prefix = input("Enter a prefix: ")
suffix = input("Enter a suffix: ")
def check_prefix_suffix(str, prefix, suffix):
    starts_with_prefix = str.startswith(prefix)
    ends_with_suffix = str.endswith(suffix)
    return starts_with_prefix, ends_with_suffix

starts_with_prefix, ends_with_suffix = check_prefix_suffix(str, prefix, suffix)

# Print the results
if starts_with_prefix:
    print("The string  starts with the prefix  ")
else:
    print("The string  does not start with the prefix ")

if ends_with_suffix:
    print("The string  ends with the suffix ")
else:
    print("The string  does not end with the suffix ")

