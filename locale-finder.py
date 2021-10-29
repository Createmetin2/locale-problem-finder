import os
import sys

localeFileName = "locale_string.txt"
lines = []

try:
	lines = open(localeFileName,"r").readlines()
except:
	print localeFileName+" <-- can't find this file! "
	os.system("PAUSE")
	sys.exit()

cur = 0
lineIndex = 0
for line in lines:
	lineIndex+=1
	if cur == 2:
		cur = 0
		continue
	firstPos = line.find('"')
	if firstPos == -1:
		print "Problem from line: "+str(lineIndex)+" - "+line
		os.system("PAUSE")
		sys.exit()
	else:
		secondPos = line[firstPos+1:].find('";')
		if secondPos == -1:
			print "Problem from line: "+str(lineIndex)+" - "+line
			os.system("PAUSE")
			sys.exit()
	cur+=1

print "Good job your locale_string is clean! "
print "by dracaryS "
os.system("PAUSE")
sys.exit()
