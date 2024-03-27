def replace_repeating(input):
    output = ''

    for char in input:
        if not output:
            output += char
        if char != output[-1]:
            output += char

    return output


# replace = replace_repeating('aaaaabbbbbcdddeeeedssaa')
replace = replace_repeating('qqqwerqwecccwd')
print(replace)

