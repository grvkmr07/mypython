try:
    d = open("abcd.txt")
except:
    print("Doesnot Exist")
else:
    print("Yes, it exists")
finally:
    print("Out of file operation")
