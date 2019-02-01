f = open("testfile0.txt", 'w')

f.write("This is testfile0\n")
f.write("Testing the skills\n \nHave a nice day!\n")

f.close()

f = open("testfile0.txt", 'r')

print("-------     f.read()    -------")
print(f.read())
f.seek(0)

print("-------     f.readline()    -------")
print(f.readline())
f.seek(0)

print("-------     f.readlines()    -------")
print(f.readlines())

f.close()

