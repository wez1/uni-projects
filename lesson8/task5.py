d = {"cat": "kissa","car": "auto"}         #global dictionary variable

def search():
    """search a word from dictionary or define if not found"""
    while True:
        w = input("Search for translation (empty to quit): ").lower().strip()
        if not w: break
    
        if w in d:                          #find as a key first
            print(w, "=", d[w])
            
        elif w in d.values():               #if not found, try with value
            print(w,"=",[key for key, value in d.items() if value == w][0])
                    
        else: define(w)                 #otherwise we can enter new definition

def define(w):
    """defines a new word to dictionary"""
    definition = input("Give definition for '%s' (or leave empty): " % w).lower().strip()
    if definition:
        d[w] = definition

def main():
    """ main program loop"""
    search()

if __name__=='__main__':
    main()
