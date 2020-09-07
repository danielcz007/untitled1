
import os

#os.mkdir("testdir")
# print(os.listdir("./"))
# print(os.getcwd())
#os.removedirs("testdir")
print(os.listdir("./"))
print(os.getcwd())
print(os.path.exists("testdir"))
if not os.path.exists("testdir"):
    os.mkdir("testdir")
if not os.path.exists("testdir/test.txt"):
    f = open("testdir/test.txt","w")
    f.write("hello '标准库'")
    f.close()
