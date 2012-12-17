#encoding=utf-8

from pyquery import PyQuery as pq
import getopt
import sys
import urllib

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


def main():
	src = "http://dict.youdao.com/search?q="
	words = getopt.getopt(sys.argv[1:], "")
	for word in words:
		if len(word) == 0:
			continue
		w = urllib.quote(word[0])
		if w == word[0]:
			w = w.lower()
		D = pq(url=src+w)
		if w != word[0] :
			toEnglish(D)
		else:
			toChinese(D)

if __name__ == "__main__":
	main()
