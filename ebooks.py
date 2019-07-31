import pyodbc

#Variables to connect to DB
server = 'localhost,1433'
database = 'Ebooks'
username = 'SA'
password = 'Passw0rd2018'

docker_ebooks = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)

cursor = docker_ebooks.cursor()

#Printing all the books
# all_books = cursor.execute("SELECT * FROM Books;")
# Counter = 1
# while True:
#     row_record = all_books.fetchone()
#     if row_record is None:
#         break
#     print(Counter, "Title: ",row_record.Title, "; Author: ", row_record.Author, "; Publish date: ", row_record.PublishDate)
#     Counter +=1

#Function to search for title
def search_book(title):
    cursor.execute("SELECT * FROM Books WHERE Title LIKE '" +title+"%'")
    row = cursor.fetchone()
    return row

