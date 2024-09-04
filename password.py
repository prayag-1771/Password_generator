import random
import string 
def gpswd(lenn,num=True,sc=True):
    letters=string.ascii_letters
    digits=string.digits
    special=string.punctuation
    characters=letters
    if num:
        characters+=digits

    if sc:
        characters+=special


    groo=""
    criteria=False
    num_num=False
    Special_special=False
    while not criteria or len(groo)<lenn:
        new=random.choice(characters)
        groo+=new

        if new in digits:
            num_num=True
        elif new in special:
            Special_special=True
        
        criteria= True
        if num:
            criteria=num_num
        elif sc:
            criteria=criteria and Special_special
    return groo

showlen=int(input("Enter the length of password:"))
gettnum=input("Want numbers in your password?... Then press 1:")
gettspecial=input("Want special characters in your password?... Then press 2:")
if gettnum==str(1):
    gettnum=True
else:
    gettnum=False
if gettspecial==str(2):
    gettspecial=True
else: 
    gettspecial=False
groo=gpswd(showlen,gettnum,gettspecial)
print(groo,"Here is it!")