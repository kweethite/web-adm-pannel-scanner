try:
    import requests
except:
    print("Please install requests module\n example: pip install requests")
    exit("blah blah :3 ")

def way1(uri):
    for u in pannel:
        guess = "http://"+uri+"/"+u
        rq = requests.get(guess)
        st = rq.status_code
        if st == 200:
            print("check this url : "+guess+u)

def way2(uri):
    for u in pannel:
        guess = uri+"/"+u
        rq = requests.get(guess)
        st = rq.status_code
        if st == 200:
            print("check this url : "+guess)

with open("url.txt","r") as pn:
    pannel = pn.read()
    pn.close()
url = str(input("Enter taget website :"))

if url.startswith("https://") or url.startswith("http://"):
    way2(url)
else:
    way1(url)



