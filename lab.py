import os
fileNameIndex={} #storing all file names
dirIndex={} #storing all directory names
textIndex={} #to store content of all text files
def crawler():
        #this loop traverse throught all the files, directories and sub-directories in the provided directory to os.walk()
	for dirname, dirs, files in os.walk("E:/csv"):
		# print path to all filenames.
		for file in files:
			path=os.path.join(dirname, file)
			#All text files are read and their content is saved in textIndex{}
			if (os.path.splitext(file)[1]=='.txt'): 
				with open(path,'r') as f:
					for line in f:
						for word in line.split():
							if word not in textIndex:
								textIndex[word]=[]
							if path not in textIndex[word]:
								textIndex[word].append(path)
				
			wordList=os.path.splitext(file)[0]
			wordList=wordList.split(' ')
			for word in wordList:
				if word not in fileNameIndex:
					fileNameIndex[word]=[]
				fileNameIndex[word].append(path)

		#stroing directiory 
		for subdir in dirs:
			wordList=subdir.split(' ')
			for word in wordList:
				if word not in dirIndex:
					dirIndex[word]=[]
				dirIndex[word].append(path)
print("Crawled")
crawler()
print(dirIndex)
inp=1
while(inp!=0):
	print("Input a keyword to search for!")
	word=raw_input("Enter the word: ")
		

	if word in textIndex:
		temp=textIndex[word]
		print("In readable files: ")
		for path in temp:
			print (path)
	if word in fileNameIndex:
		temp=fileNameIndex[word]
		print("In files names: ")
		for path in temp:
			print (path)
	if word in dirIndex:
		temp=dirIndex[word]
		print("In Directory names: ")
		for path in temp:
			print (path)
