#!/usr/bin/env python

import urllib
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
        self.simbol = "%"

    def download(self, urlFile):
        """
        Download the file with the url or links sent.
        """
        try:
            print("\n[?] File information: %s saved in %s") % (os.path.basename(urlFile), self.dir)
            urllib.urlretrieve(urlFile, os.path.basename(urlFile), self.progress)
            urllib.urlcleanup() #clears the cache urllib.urlretrieve()
            self.aux = 0
            sys.stdout.write(" - Done.\n")
            self.beep()
        except IOError, er:
            print(er)
        except KeyboardInterrupt:
            print("\n[x] Download canceled by user.")

    def readFile(self, nameFile):
        """
        Read a file with links for dowload.
        """
        try:
            file_ = open(nameFile, "r")
            link = file_.readlines() #returns a list of links
            file_.close()
            for l in link:
                self.download(l)
        except IOError, e:
            print(e)

    def progress(self, numBlock, blockSize, totalSize):
        """
        Progress() function, gives the percentage of the file to download and send it to the function percent().
        """
        p = int(numBlock * blockSize * 100 / totalSize)
        p_ = blockSize * numBlock
        self.percent(p, p_, totalSize)

    def percent(self, percent, percent_, size):
        """
        Screen printed on the progress of the download.
        """
        if percent == self.aux:
            sys.stdout.write("\r\t[~] [%s / %s] Downloading ... %d%s" % (self.sizeFile(percent_), self.sizeFile(size),
                                                                         percent, self.simbol))
            sys.stdout.flush()
            time.sleep(.125)
            self.aux += 1

    def sizeFile(self, bytes):
        bytes = float(bytes)
        if bytes >= 1099511627776:
            teraBytes = bytes / 1099511627776
            size = "%.1fTB" % teraBytes
        elif bytes >= 1073741824:
            gigaBytes = bytes / 1073741824
            size = "%.1fGB" % gigaBytes
        elif bytes >= 1048576:
            megaBytes = bytes / 1048576
            size = "%.1fMB" % megaBytes
        elif bytes >= 1024:
            kiloBytes = bytes / 1024
            size = "%.0fKB" % kiloBytes
        else:
            size = "%.1f Bytes" % bytes
        return size

    def beep(self):
        """
        Successful download simple alert.
        """
        for i in range(0, 2):
            print '\a',

    def main(self):
        """
        Menu of options.
        """
        try:
            opts, args = getopt.getopt(sys.argv[1:], "hdf")
            for o, a in opts:
                if o in ("-h"):
                    self.usage()
                if o in ("-d"):
                    self.download(sys.argv[2])
                if o in ("-f"):
                    self.readFile(sys.argv[2])
        except getopt.error, er:
            print(er)

    def usage(self):
        print("""
        URLpy - Developer by @sosacamilin

        Usage: urlpy [options...] <URL> or <fileName>
        Options:    
        -d     URL file to download.
        -f     file name with links to download.
        """)

if __name__ == "__main__":
    urlpy = URLpy()
    urlpy.main()