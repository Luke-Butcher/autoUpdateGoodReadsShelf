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
    testData2 = 'Great Expectations'
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
    stringsOfData = []
    for x in wantedData:
        stringsOfData.append(''.join(x))
    
    for x in stringsOfData:
        title, isbn = x.split(',', maxsplit = 1)
        guff, title2 = title.split(':')
        title2 = title2.replace('"' ,'').lstrip()
        if title2 == testData2:
            isbn2 = isbn.split('"')
            for x in isbn2:
                if x.isdigit():
                    if len(x) == 13:
                        return(x)
           
#connect to good reads
#update shelf

main()
