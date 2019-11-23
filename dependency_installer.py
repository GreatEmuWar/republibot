from pip._internal import main as pipmain

def installer():

    infile = open('dependencies.txt','r+')
    packages = infile.readlines()

    for i in range(0,len(packages)):

        packages[i] = packages[i].rstrip('\n')

    for n in range(0,len(packages)):

        try:

            pipmain(['install',packages[n]])

        except ImportError:

            print("Import error: packages could not be properly imported.")

        finally:

            print("All dependencies have been resolved.")

def __main__():

    installer()

__main__()            