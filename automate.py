"""
Helper functions
"""
import os
import shutil
import time

from browser import Browser

class Automate():

    def get_url(self, url, chrome=False):
        '''
        Method to test for one url
        '''
        if not url.strip().startswith("http"):
            print("Incorrect url format for: " + str(url))

        Browser(url, "chrome")

        if not chrome:
            Browser(url, "ff")

    def get_urls(self, filename, chrome=False):
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

    def update_folders(self):
        """
        Method to keep the previous report and then to store the data
        """
        if not os.path.exists('./reports'): 
            os.mkdir('./reports')
        else:
            folder = './reports/' + str(int(time.time()))
            os.mkdir(folder)
            for filename in os.listdir('./reports'):
                file_path = os.path.join(folder, filename)
                try:
                    if not os.path.isdir('./reports/' + filename):
                        shutil.copy('./reports/' + filename, file_path)
                    else:
                        if filename != './reports/' + filename:
                            shutil.rmtree(filename)
                except Exception as e:
                    print('Failed to delete %s. Reason: %s' % (file_path, e))

