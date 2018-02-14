import urllib.request

def getUrl():
    while True:
        try:
            with urllib.request.urlopen(input("give website: ")) as url:        #https://www.google.com/
                s = url.read()
                return s
        except: print("Give a working URL pl0x!1")

def saveUrl(s):
    with open("tiedosto.txt", 'wb') as f:
        f.write(bytes(s))
        f.close()

def main():
    """ main program loop"""
    saveUrl(getUrl())
    
if __name__=='__main__':
    main()
