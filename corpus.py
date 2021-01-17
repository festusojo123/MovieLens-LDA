#creates corpus, uses synthesizedMovieInfo.csv which is altered data from Wikipedia corpus
#uses https://www.kaggle.com/jrobischon/wikipedia-movie-plots


import csv
import pandas as pd

MLtitles = open('titles.txt').read().splitlines()
dictOfOrders = {}
counter = 1
#associates Wikipedia-formatted movie titles with movie IDs
for x in MLtitles:
    dictOfOrders[x] = counter
    counter += 1

f = open('synthesizedMovieInfo.csv','r')
reader = csv.reader(f)
for row in reader:
    newFileContent = ""
    line2 = str(row[3]) + "\n" #genre
    newFileContent += line2
    line3 = str(row[4]) + "\n" #summary from wikipedia   
    newFileContent += line3
    writingFilePath = str(row[5])+'.txt' #file name is movieID
    writingFile = open(writingFilePath,'w')
    #files are written to updatedCorpus.zip
    writingFile.write(newFileContent)
    writingFile.close()     
readingFile.close()
