try:
    import requests
except:
    print("Please install requests module\n example: pip install requests")
    exit("blah blah :3 ")
try:
    import pyfiglet

except:
    print("Please install pyfiglet module\n example: pip install pyfilglet")
    exit("blah blah :3")
tt = pyfiglet.figlet_format("w adm login scanner")
print(tt)

pannel = open("url.txt","r")

class color():
    def __init__(self,gl,blu,read,yel,):
        self.gl = gl
        self.blu = blu
        self.read = read
        self.yel = yel
cl = color('\033[1;32;50m','\033[1;34;50m','\033[1;31;50m','\033[1;33;50m')

print(cl.read,'Educational Purpose Only')
print(cl.blu,'Author by စပစာ')
print(cl.yel,'youtube cn :https://www.youtube.com/blah balh :3')
print(cl.gl,'facebook :https://web.facebook.com/thite.thite.1069')
print(cl.read,'######################################################################')



def way1(uri):

    for u in pannel:
        guess = "http://"+uri+"/"+u
        try:
           rq = requests.get(guess)
           st = rq.status_code
           if st == 200:
               print("check this url : " + guess + u)
           else:
               print("no :" + u)
        except:
            print("network error on invalid url ")
            break


def way2(uri):
    for u in pannel:
        guess = uri+"/"+u
        try:
            rq = requests.get(guess)
            st = rq.status_code
            if st == 200:
                print("check this url : "+guess)
            else:
                print("no :"+u)
        except:
            print("network error or invalid url")
            break
url = str(input("Enter taget website :"))

if url.startswith("https://") or url.startswith("http://"):
    way2(url)
else:
    way1(url)



