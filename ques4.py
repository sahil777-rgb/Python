p1 = "make a lot of money"
p2 = "money making"
p3 = "subscibe to this"
p4 = "clik on this link"

message = input("ENTER YOUR COMMENT: ")
if ((p1 in message)  or (p2 in message) or (p3 in message) or (p4 in message) ):
    print("THIS IS A SPAM ! ")
else:
    print("THIS IS NOT A A SPAM ")    

