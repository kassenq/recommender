'''
@author: Kassen Qian kkq
'''


def getdata():
    '''
    This function reads data from a file and returns the data in the form of a two-tuple.
    The first element of the two-tuple is a list of strings, the second element is a 
    dictionary.
    '''
    items = []
    ratings = {}
    f = open("data/books.txt")
    for line in f:
        a = line.split(",")
        ratings[a[0]] = []
        for i in range(len(a)):
            if i == 0:
                continue
            if i%2 == 1:
                if a[i] not in items:
                    items.append(a[i])
            else:
                ratings[a[0]].append(int(a[i]))
    return (items, ratings)
#     f = open('data/books.txt', encoding="utf-8")
#     items = []
#     ratings = {}
#     for line in f:
#         linelist = line.split(",") #['student1367', 'Star Trek Beyond', '3', 'book2', '5']
#         student = linelist[0]
#         for str in linelist:
#             if (linelist.index(str) % 2) == 1:
#                 if str not in items:
#                     items.append(str)
#     
#     items = sorted(items)
#                         
#     for line in f:
#         linelist = line.split(",") #['student1367', 'Star Trek Beyond', '3', 'book2', '5']
#         student = linelist[0]
#         
#         if student not in ratings:
#             ratings[student] = [0]*len(items)
#         
#         for i in range(1, len(linelist), 2):
#             bookname = linelist[i]
#             rating = linelist[i+1]
#             idx = items.index(bookname)
#             ratings[student][idx] = rating
#         
#     f.close()
#     return (items, ratings)