##
String = input('insert any string')
if String.isalpha():
    print('the string contains only letters')
if String.upper() == String and String.isdigit() is False:
    print('the string contains only UPPERCASE LETTERS')
elif String.lower() == String and String.isdigit() is False:
    print('THE STRING CONTAINS ONLY lowercase letters')

if String.isdigit():
    print('the string only contains digits')

if String.isalnum():
    print('the string only contains letters or digits')

if String[0].islower():
    print('the string starts with a lowercase letter')

if String[len(String)-1] == '.':
    print('the string ends with a full stop >:(')
