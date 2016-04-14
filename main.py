# ================== Variables =================
words = []

uniqueWord = 0
N = 0
uniqueCount = 0
l = 0

# ================== Functions =================

def readParameters():
	global uniqueWord
	global N
	global l
	uniqueWord = input( "Write unique word: " )
	N = int(input( "Write count of words: " ))
	l = len( uniqueWord )

def readText( path ):
	global words
	file = open( path, "r" )
	fullText = file.read()
	words = fullText.split()

def delta( s ):
	global uniqueWord
	global l
	count = 0
	for i in range( 0, min( len( s ), l ) ):
		if ( s[i] == uniqueWord[i] ):
			count += 1
	return len( s ) - count

def makeUnique():
	global words
	global uniqueCount
	words.sort()
	posToSwap = 0
	uniqueCount = 1
	for i in range( 0, len( words ) - 1 ):
		if ( words[i] != words[i+1] ):
			posToSwap += 1
			if ( posToSwap != (i + 1) ):
				words[posToSwap] = words[i + 1]
			uniqueCount += 1
	words = words[:uniqueCount]

def getResult():
	global words
	words.sort( key = delta )

def writeAnswer():
	global words
	global uniqueCount
	global N
	for i in range ( 0, min( N, uniqueCount ) ):
		print( words[i] )

def endUp():
	global words
	words = []

# ================== Main ======================

def main():
	import datetime
	count = 1;
	readParameters()
	timeOut = open( "timePy.txt", "w" )
	for i in range( 0, 4 ):
		path = "strings" + str( count ) + "000000.txt"
		readText( path )
		beginTime = datetime.datetime.now()
		makeUnique()
		getResult()
		endTime = datetime.datetime.now()
		# writeAnswer()
		delta = endTime - beginTime
		timeOut.write( str( count ) + "000000 " + str(int(delta.total_seconds() * 1000) ) + '\n' )
		count *= 2
	timeOut.close()

# ================== Program ===================

main()