
# ============================
# name_main1.py
# ============================

# understanding __name__ = __main__

# https://stackoverflow.com/questions/419163/what-does-if-name-main-do

# Note: If you put code before the function definitions it will execute before main.


def functionA():
    print("Function A printed")
def functionB():
    print("Function B printed")
def functionC():
    print("Function C printed")
def functionD():
    print("Function D printed")

# These two functions will be printed by import_name_main.py
# because they will run without __name__= __main__

functionA()
functionB()

# These two functions will not print when being imported by import_name_main.py
# because they only run if __name__==__main__

if __name__ == '__main__':
    functionC()
    functionD()

# Note that all the functions will print if being ran from here
# because __name__=__main__


