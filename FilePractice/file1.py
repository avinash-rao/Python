try:
   f = open("testfile0.txt", mode='a', encoding = 'utf-8')
   # perform file operations
   f.write("This sentence is appended by file1\n")
finally:
   f.close()