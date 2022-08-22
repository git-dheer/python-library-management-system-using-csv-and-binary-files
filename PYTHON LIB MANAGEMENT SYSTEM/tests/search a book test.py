# file name = books.csv
# tables are = | name | id | publisher | author | price | total number awailable before issue | total number after issue |

import csv
f = open("books.csv","r")
r = csv.reader(f)
# basically we search a book by the book name
nts = input("enter the book id to search : ")
for rows in r:
    if rows[0] == nts :
        pass