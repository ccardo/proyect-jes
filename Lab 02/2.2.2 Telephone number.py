##
# This program takes any 10-digit number, and
# prints it out in the standard US format: (xxx) xxx-xxxx
InputNumber = input("insert any 10-digit number: ")
if len(InputNumber) == 10:

    # splits the number up into the area code, and the
    # digits which come before and after the hyphen
    areaCode = InputNumber[:3]
    preHyphen = InputNumber[3:6]
    postHyphen = InputNumber[6:]

    # converts the digits into a formatted phone number
    phoneNumber = '(' + areaCode + ')' + ' ' + preHyphen + '-' + postHyphen
    print("phone number: ", phoneNumber)

else:
    print("only insert a 10-digit number")
