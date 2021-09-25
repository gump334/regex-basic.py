import re

def isPhoneNumber(text):
    if len(text) != 12:
        return False # not phone number-size
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False # no area code
    if text[3] != "-":
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != "-":
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True

message = "Call me at 415-555-1011 tomorrow. 415-555-9999 is my office."
foundNumber = False
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print("Phone number foune: " + chunk)
        foundNumber = True
if not foundNumber:
    print("could not find any phone numbers. ")  
print("Done")

# Simplified with regex
phoneNumberRegex = re.compile(r'\(\d\d\d\) \d\d\d-\d\d\d\d')
mo = phoneNumberRegex.search("My number is (334) 450-0000")
print(phoneNumberRegex.findall("call me 444-254-5454 tomorrow or at 334-450-8000"))
print(mo.group()) #grabbing sections of your search pattern


batRegex = re.compile(r"Bat(man|mobile|copter|bat)")
mo = batRegex.search("Batmobile lost a wheel then Batman need to get to the Batcopter")
print(mo.group())