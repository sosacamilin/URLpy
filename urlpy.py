import urllib
import sys
import os
import getopt


class Url():
	"""Class to download files individually or in a text file."""
	def __init__(self):
		self.aux = 0


	def usage(self):
		print("""
Camilo Sosa Morales <codex.deb@gmail.com>
Usage: python url.py [options...] <url> or <file>

Options:
-u     url file to download.
-f     file with links to download.
		""")


	def download(self, urlFile):
		"""download the file with the url or links sent."""
		try:
			print("- Downloading... %s" % os.path.basename(urlFile))
			urllib.urlretrieve(urlFile, os.path.basename(urlFile), self.progress)
			urllib.urlcleanup() #clears the cache urllib.urlretrieve()
			self.aux = 0
			print("\n- Download complete.\n")
		except IOError, e:
			print(e)


	def progress(self, numBlock, blockSize, totalSize):
		"""progress() function, gives the percentage of the file to download and send it to the function percent()."""
		p = int(numBlock * blockSize * 100 / totalSize)
		self.percent(p)


	def percent(self, percent):
		"""screen printed on the progress of the download."""
		if percent == self.aux:
			sys.stdout.write("|")
			sys.stdout.flush()
			self.aux += 1


	def readFile(self, nameFile):
		"""read a file with links for dowload"""
		try:
			f = open(nameFile, "r")
			flist = f.readlines() #returns a list of links
			f.close()
			for l in flist:
				self.download(l)
		except IOError, e:
			print(e)


	def main(self):
		try:
			opts, args = getopt.getopt(sys.argv[1:], "hd:f:")
			for o, a in opts:
				if o in ("-h"):
					self.usage()
				if o in ("-d"):
					self.download(sys.argv[2])
				if o in ("-f"):
					self.readFile(sys.argv[2])
		except getopt.error, e:
			print(e)


if __name__ == '__main__':
	u = Url()
	u.main()		