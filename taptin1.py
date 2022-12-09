x = (input())
print("nhap ki tu", x)
def b1(x):
    y = open('D:/123.txt', 'r+')
    y.write(x)
def b2():
    y = open('D:/123.txt', 'r')
    print(y.read())

def b3(x):
    y = open('D:/123.txt', 'a+')
    y.writelines(x)

def b4():
    y = open('D:/123.txt', 'r')
    print(y.read())

def main():
    b1(x)
    b2()
    b3(x)
    b4()
if __name__=="__main__":
    main()