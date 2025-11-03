# Created on 
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