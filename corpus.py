#creates corpus, uses synthesizedMovieInfo.csv which is altered data from Wikipedia corpus
#https://www.kaggle.com/jrobischon/wikipedia-movie-plots


import csv
# import pandas as pd

# MLtitles = open('titles.txt').read().splitlines()
# dictOfOrders = {}
# counter = 1
# for x in MLtitles:
#     dictOfOrders[x] = counter
#     counter += 1
# print(dictOfOrders['Alice in Wonderland']) 



f = open('synthesizedMovieInfo.csv','r')
reader = csv.reader(f)
for row in reader:
    newFileContent = ""
    # line1 = str(row[2]) + "\n"
    # print(line1)
    # newFileContent += line1
    line2 = str(row[3]) + "\n"
    newFileContent += line2
    line3 = str(row[4]) + "\n"    
    newFileContent += line3
    # line4 = "movieID: " + str(row[5]) + "\n" 
    # newFileContent += line4  
    writingFilePath = str(row[5])+'.txt'
    writingFile = open(writingFilePath,'w')
    writingFile.write(newFileContent)
    writingFile.close()     
readingFile.close()



# starter_df = pd.read_csv('new.csv')



# starter_df["movieID"] = starter_df["Title"].map(lambda x : dictOfOrders[x])

# starter_df.to_csv('synthesizedMovieInfo.csv')

# with open('new.csv', 'w') as csv_file:  
#     writer = csv.writer(csv_file)
#     for key, value in dictOfOrders.items():
#         if key == 
#        writer.writerow([key, value])

# import pandas as pd
# csv_input = pd.read_csv('new.csv')
# csv_input['movieID'] = dictOfOrders['Title']
# csv_input.to_csv('output.csv', index=False)

#step 3 - or just use counter and MovieID

# counter = 0
# for x in MLtitles:
#     x = str(counter) + " - " + x
#     print(x)
#     counter += 1


# # read the csv data into a dataframe 
# # change "," to the data separator in your csv file 
# df = pd.read_csv("wiki_movie_plots_deduped.csv", sep=",")
# # filter the data: keep only the rows that contain one of the keywords 
# # in the position or the Job description columns
# df = df[df["Title"].isin(MLtitles)] 
# # write the data back to a csv file 
# df.to_csv("new_data.csv",sep=",", index=False) 

# data = pd.read_csv("new_data.csv", sep=",")
# deselectlist =[ '', 'Release Year', 'Origin/Ethnicity' , 'Director', 'Cast' , 'Wiki Page']
# selectlist =[x for x in data.columns if x not in deselectlist]
# datatowrite = data[selectlist]

# datatowrite.to_csv('new.csv')


#step 2 make csv 

# def writeSynthesizedFile():
#     newFileContent = ""
#     readingFile = open("plots.txt",'r')
#     for line in readingFile:
#         strippedLine = line.strip('\n')
#         for x in MLtitles:
#             if x in strippedLine:
#             newLine = multipleReplace(strippedLine,replaceDict)
#             newFileContent += newLine + "\n"
#     readingFile.close()
#     writingFilePath = 'outputBankStatements/output-file10-'+str(count)+'.txt'
#     writingFile = open(writingFilePath,'w')
#     writingFile.write(newFileContent)
#     writingFile.close()
#     return newFileContent


# if __name__ == '__main__':
#     printList = writeSynthesizedFile()
#     print(printList)
