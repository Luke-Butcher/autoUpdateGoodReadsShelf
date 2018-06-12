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
    splitSRS = searchResultString.split('"kind"')
    results = []
    for book in splitSRS:
        results.append(book)
        
    wantedData = []
    for book in results:
        bookData = []
        bookSplit = book.splitlines()
        for line in bookSplit:
            if '"title":' in line or '"identifier"' in line:
                bookData.append(line.strip())
        if len(bookData) >=1:
            wantedData.append(bookData)
    print(wantedData)


    # for x in wantedData:
    #     title, ISBN, other = x.split(',')
    #     print(ISBN)
        

    
         
    
    
    
    #THIS ALL WORKS returns the isbn for all the results
    # splitSRS = searchResultString.split(',')
    # ISBN13s = []
    # for word in splitSRS:
    #     if 'identifier' in word:
    #          for ISBN in word.split('"') :
    #             if ISBN.isdigit():
    #                 if len(ISBN) == 13:
    #                     ISBN13s.append(ISBN)
    # print(ISBN13s)
    


    

#connect to good reads
#update shelf

main()
