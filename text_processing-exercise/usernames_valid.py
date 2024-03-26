def valid_usernames(names):
    for name in names.split(', '):
        if 3 <= len(name) <= 16:
            if name.isalnum() or '-' in name or '_' in name:
                print(name)


test_input_one = valid_usernames("sh, too_long_username, !lleg@l ch@rs, jeffbutt")
test_input_two = valid_usernames("Jeff, john45, ab, cd, peter-ivanov, @smith")

print(test_input_one)
print(test_input_two)
