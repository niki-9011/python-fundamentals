def encrypted(input):
    message = [chr(ord(x) + 3) for x in input]

    return "".join(message)


message_encrypted_one = encrypted('Programming is cool!')
message_encrypted_two = encrypted('One year has 365 days.')

print(message_encrypted_one)
print(message_encrypted_two)
