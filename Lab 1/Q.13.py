#This program converts bytes into gigabytes(GB), megabytes(MB),kilobytes(KB).
a = int(input("Enter number of bytes: "))
b = a/1024
c = b/1024
d = c/1024
print("Answers:")
print("Kilobytes: ",b)
print("Megabytes: ",c)
print("Gigabytes: ",d)
