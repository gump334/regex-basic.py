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

#print("Is 415-555-4242 a phone number?")
#print(isPhoneNumber("415-555-4242"))
#print("is Moshi moshi a phone number?")
#print(isPhoneNumber("Moshi mosh"))
#test