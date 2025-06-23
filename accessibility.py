'''
Script to read the CIM site and run accessibility test
'''
import getopt
import os
import shutil
import sys

from browser import Browser

def get_url(url, chrome=False):
    '''
    Method to test for one url
    '''
    if not url.strip().startswith("http"):
        print("Incorrect url format for: " + str(url))

    Browser(url, "chrome")

    if not chrome:
        Browser(url, "ff")

def get_urls(filename, chrome=False):
    '''
    Method to test for one url
    '''

    fh = open(filename, "r")
    urls = fh.readlines()
    fh.close()

    for url in urls:
        if url.strip().startswith("http"):
            Browser(url, "chrome")
            if not chrome:
                Browser(url, "ff")
        else:
            print("{} is incorrect url".format(url))
    

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
        opts, args = getopt.getopt(sys.argv[1:], "h:u:f:c:", ["help", "url=", 'file=', 'chrome'])
    except getopt.GetoptError as err:
        # print help information and exit:
        usage()
        sys.exit(2)
    url = None
    filename = None
    chrome = True

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
            chrome = False
        else:
            assert False, "unhandled option"

    if filename is not None and url is not None:
        print("Error in options.Please read the usage.")
        usage()
        sys.exit(2)

    urls=[]

    if not os.path.exists('./reports'): 
        os.mkdir('./reports')
    else:
        for filename in os.listdir('./reports'):
            file_path = os.path.join(folder, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print('Failed to delete %s. Reason: %s' % (file_path, e))

    if filename is not None:
        get_urls(filename, chrome)

    if url is not None:
        get_url(url, chrome)

if __name__ == "__main__":
    main()
