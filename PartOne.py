def cameltosnake(input):
    output = ""
    for char in input:
        if char.isupper():
            output+= "_" + char.lower()
        else:
            output += char
    return output.lstrip('_')

input = input("Enter camel case: ")
result = cameltosnake(input)
print("snake case conversion:", result)

