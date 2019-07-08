'''
@author: Kassen Qian kkq
'''


def getdata():
    '''
    This function reads data from a file and returns the data in the form of a two-tuple.
    The first element of the two-tuple is a list of strings, the second element is a 
    dictionary.
    
    student1367,Star Trek Beyond,3

    '''
    items = []
    ratings = {}
    f = open("data/movies.txt")
    for line in f:
        a = line.split(",")
        if a[1] not in items:
            items.append(a[1])
        if a[0] not in ratings:
            ratings[a[0]] = []
    items.sort()
    for i in ratings:
        for l in range(len(items)):
            ratings[i].append(0)
    f = open("data/movies.txt")
    for line in f:
        a = line.split(",")
        place = items.index(a[1])
        ratings[a[0]][place] = int(a[2])
    return (items, ratings)
#     f = open('data/movies.txt', encoding="utf-8")
#     items = []
#     ratings = {}
#     for line in f:
#         linelist = line.split(",") #['student1367', 'Star Trek Beyond', '3']
#         student = linelist[0]
#         movie = linelist[1]
#         rating = linelist[2]
#         items.append(movie)
#     
#     items = sorted(items)
# 
#     for line in f:
#         linelist = line.split(",") #['student1367', 'Star Trek Beyond', '3']
#         student = linelist[0]
#         movie = linelist[1]
#         rating = linelist[2]
#         idx = items.index(movie)
#         if student not in ratings:
#             ratings[student] = [0]*(len(items))
#         ratings[student][idx] = rating
#         
#         
#     f.close()
#     
#     return (items, ratings)
#         
