id=input('Input student ID: ')
fn=input('Input first name: ')
ln=input('Input last name: ')
m=input('Input "I am a newbie in Whitecliffe college: ')
ms=m.split()
if "Whitecliffe" in ms and "college" in ms :
    code=id[:2]+ln[:3]
    print(code)
elif "whitecliffe" in ms and "college" in ms:
    code = id[:2] + ln[:3]
    print(code)
elif "Whitecliffe" in ms and "College" in ms :
    code=id[:2]+ln[:3]
    print(code)
elif "whitecliffe" in ms and "College" in ms :
    code=id[:2]+ln[:3]
    print(code)