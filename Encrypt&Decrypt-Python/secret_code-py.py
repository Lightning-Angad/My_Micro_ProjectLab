#Assignment-D: Encryption & Decryption
name = input("Enter your name (no spaces): ")
print ("Enter [1] for Encryption\nEnter [2] for Decryption\nEnter [0] for Exit")
s = int(input("Enter your choice: "))
match s:
  case 0:
    exit ()
  case 1:
    if (len(name)<=3):
        rev = name[::-1]
        print("The encrypted text is: ", rev.lower())
    else:
        x=name.replace(name[0], "%", 1)
        y=x.replace(name[len(name)-1], "?", 1)
        rev = y[::-1]
        z="*!@" + rev.lower() + "*!@"
        print("The encrypted text is: ", z)
  case 2:
    if (len(name) <= 3):
        rev = name[::-1]
        print("The decrypted text is: ", rev.capitalize())
    else:
        first = input ("Enter first key: ")
        last = input ("Enter last key: ")
        m=name.strip("*!@")
        rev = m[::-1]
        x=rev.replace("%", first, 1)
        y=x.replace("?", last, 1)
        print("The decrypted text is: ", y.title())
  case _:
       print ("Wrong Input")