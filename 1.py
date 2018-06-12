import os
import urllib.request
import urllib.parse



#N:\\test1
titles = []
validExtension = ('.txt', '.docx', '.pptx')
def main():
    startFolder = input('Enter your input:')
    getTitles(startFolder)
    getISBN(titles)

#get the titles
def getTitles(startFolder):
   for root, dirs, files in os.walk(startFolder):
        for name in files:
            if name.endswith(validExtension):
                title, extension = name.split('.')
                titles.append(title)

#get the isbn
def getISBN(titles): 
    print(titles)

    testData='GreatExpectations'
    url = 'https://www.googleapis.com/books/v1/volumes?q='+testData+'+intitle'
    
    searchResult= urllib.request.urlopen(url)

    searchResultString=(searchResult.read().decode('utf-8'))  
    
    print(searchResultString)
    

#connect to good reads
#update shelf

main()
