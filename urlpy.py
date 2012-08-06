#!/usr/bin/env python

import urllib
import urllib2
import sys
import os
import getopt
import time

class URLpy():
    """
    Class to download files individually or in a text file.
    """
    def __init__(self):
        self.aux = 0
        self.dir = os.getcwd()
        self.simbol = '%'


    def usage(self):
        print '''
Camilo Sosa Morales. a.k.a c0dex__ codex.deb@gmail.com
Facebook: fb.com/kamiadry
---------------------
Usage: python url.py [options...] <URL> or <fileName>

Options:    
-u     URL file to download.
-f     file name with links to download.
        '''


    def download(self, urlFile):
        """
        Download the file with the url or links sent.
        """
        try:
            r = urllib2.urlopen(urlFile)
            print '\n[?] File information: %s - %.2f MB' % (os.path.basename(urlFile),
                float(r.info()['Content-Length']) / 1048576)
            urllib.urlretrieve(urlFile, os.path.basename(urlFile), self.progress)
            urllib.urlcleanup() #clears the cache urllib.urlretrieve()
            self.aux = 0
            sys.stdout.write(' - Done.\n')
        except IOError, e:
            print e
        except KeyboardInterrupt:
            print '\n[x] Download canceled by user.'


    def progress(self, numBlock, blockSize, totalSize):
        """
        Progress() function, gives the percentage of the file to download and send it to the function percent().
        """
        p = int(numBlock * blockSize * 100 / totalSize)
        self.percent(p)


    def percent(self, percent):
        """
        Screen printed on the progress of the download.
        """
        if percent == self.aux:
            sys.stdout.write('\r\t[~] Downloading ... %d%s' % (percent, self.simbol))
            sys.stdout.flush()
            time.sleep(.125)
            self.aux += 1


    def readFile(self, nameFile):
        """
        Read a file with links for dowload.
        """
        try:
            f = open(nameFile, 'r')
            flist = f.readlines() #returns a list of links
            f.close()
            for l in flist:
                self.download(a, l)
        except IOError, e:
            print(e)


    def main(self):
        """
        Menu of options.
        """
        try:
            opts, args = getopt.getopt(sys.argv[1:], 'hd:f:')
            for o, a in opts:
                if o in ('-h'):
                    self.usage()
                if o in ('-d'):
                    self.download(sys.argv[2])
                if o in ('-f'):
                    self.readFile(sys.argv[2:])
        except getopt.error, e:
            print(e)


if __name__ == '__main__':
    urlpy = URLpy()
    urlpy.main()        
