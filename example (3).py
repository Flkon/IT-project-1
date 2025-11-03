# Created on iPad.

classify_person = int(input("how old are you"))
if classify_person <= 12:
    print("child")
elif classify_person <= 17:
    print("teenager")
elif classify_person <= 64:
    print("adult")
else:
    print("senior")
    
    
    
a = int(input("what time is it"))
if a in range (4, 12):
    print("morning")
elif a in range (11, 17):
	print("afternoon")
elif a in range(16, 21):
	print("evening")
elif a in range(20, 24):
    print("night")
elif a in range(0, 5):
	print("night")
    
D =int(input("write a number here to check if its divisible by 5"))
if D/5 :
    print("divisible by 5")
else:
    print("not divisible by 5").