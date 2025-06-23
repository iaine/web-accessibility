'''
Script to run accessibility test on defined urls
'''
import getopt
import sys

from automate import Automate

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
    urlfilename = None
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
            urlfilename = a
        elif o in ("-c", "--chrome"):
            chrome = False
        else:
            assert False, "unhandled option"

    if urlfilename is not None and url is not None:
        print("Error in options.Please read the usage.")
        usage()
        sys.exit(2)

    urls=[]

    automated = Automate()

    automated.update_folders()

    if urlfilename is not None:
        automated.get_urls(urlfilename, chrome)

    if url is not None:
        automated.get_url(url, chrome)

if __name__ == "__main__":
    main()
