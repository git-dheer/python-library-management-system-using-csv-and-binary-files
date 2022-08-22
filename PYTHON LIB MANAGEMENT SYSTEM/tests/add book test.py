# file name = books.csv
# tables are = | name | id | publisher | author | price | total number awailable before issue | total number after issue |

#opening the file in append mode lets assume the file is aldready created 
import csv

f = open ('books.csv','a' )
w = csv.writer (f)
n = int(input("how many different books do u want to add : "))
for i in range (n) :
    for i in range (1):
        a = input("enter the name of the book : ")
        b = input("enter the book id : ")
        c = input ("enter the name of the book publisher : ")
        d = input ("enter the name of the author : ")
        e = input ("enter the price for the book : ")
        ff = input("enter the total number of this book that is to be added : ")
        l = [a,b,c,d,e,ff]
        w.writerow(l)
f.close ()

