#encoding=utf-8

from pyquery import PyQuery as pq
import getopt
import sys
import urllib
src = "http://dict.youdao.com/search?q="

def toChinese(D):
	res = D("#phrsListTab .trans-container li")
	lis = []
	for r in res:
		lis.append(r.text)
		print r.text


def toEnglish(D):
	res = D("#phrsListTab .wordGroup a")
	lis = []
	for r in res:
		lis.append(r.text)
		print r.text


# API
def translate(word):
	w = urllib.quote(word)
	if w == word:
		w = w.lower()
	D = pq(url=src+w)
	if w != word :
		toEnglish(D)
	else:
		toChinese(D)

def main():
	words = getopt.getopt(sys.argv[1:], "")
	for word in words:
		if len(word) == 0:
			continue
		translate(word[0])

if __name__ == "__main__":
	main()
