'''
Script to read the CIM site and run accessibility test
'''
import os
import getopt, sys
from browser import Browser

def get_url(url, chrome=False):
    '''
    Method to test for one url
    '''
    Browser(url, "ff")

    if chrome:
        Browser(url, "chrome")

def get_urls(filename, chrome=False):
    '''
    Method to test for one url
    '''
    fh = open(file, "r")
    data = fh.readlines()
    for line in data:
        getline = line.split(',')
        urls.append(getline[1])
    fh.close()

    for url in urls:
        Browser(url, "ff")
        if chrome:
            Browser(url, "chrome")
    

def usage():
    '''
    Help function
    '''
    usage = """Accessibility test tool. 
    Takes a series of urls or a single url to test accessibility.
    It uses the axe library to test. 
    
    Do not run this too often: it is a heuristic to help test, not a replacement and 
    results may change between runs."""

    print(usage)


def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hufc:", ["help", "url=", 'file='])
    except getopt.GetoptError as err:
        # print help information and exit:
        print(err)  # will print something like "option -a not recognized"
        usage()
        sys.exit(2)
    url = None
    filename = None
    chrome = False
    for o, a in opts:
        if o == "-v":
            verbose = True
        elif o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-u", "--url"):
            output = a
        elif o in ("-f", "--file"):
            filename = a
        elif o in ("-c", "--chrome"):
            chrome = True
        else:
            assert False, "unhandled option"

    if file is not None and url is not None:
        print("Error in options.Please read the usage.")
        usage()
        sys.exit(2)

    urls=[]

    if not os.path.exists('./reports'): os.mkdir('./reports')

    if file is not None:
        get_urls(file, chrome)

    if url is not None:
        get_url(url, chrome)

if __name__ == "__main__":
    main()
