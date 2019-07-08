'''
@author: Kassen Qian kkq
'''
import operator

def averages(items, ratings):
    '''
    This function calculates the average ratings for items. 
    A two-tuple is returned, where the first element is a string and the second element is a float.
    '''
    ret = []
    for i in range(len(items)):
        x = 0
        y = 0
        for j in ratings:
            if ratings[j][i] != 0:
                x+= ratings[j][i]
            else:
                y += 1
        if x == 0:
            ret.append((items[i], 0.0))
        else:
            ret.append((items[i], x/(len(ratings)-y)))
    alpha = sorted(ret)
    alpha.sort(key = operator.itemgetter(1), reverse = True)
    return alpha
    # items is a list of strings ['r1', 'r2', 'r3']
    # ratings is a dictionary {'Me':[2, 3, 4], 'You':[0,1,2]}
#     lstavgs = []
#     for i in range(len(items)): #0
#         avg = getAverage(items[i], items, ratings) #3
#         lstavgs.append(avg) #[2, 2, 3]
#     avgsdic = {}
#     for i in range(len(items)):
#         if items[i] not in avgsdic:
#             avgsdic[items[i]] = 0
#         avgsdic[items[i]] += lstavgs[i]
#     print(avgsdic)
#     lstdic = list(avgsdic.items())
#     finallst = sorted(lstdic, key=lambda x:x[1], reverse=True)
#     return finallst

    # YAY THIS IS FUNCTIONAL

# def getAverage(item, items, ratings):
#     '''
#     This function is a helper function that finds the average rating for each item in items
#     '''
#     sum = 0
#     idx = items.index(item)
#     count = 0
#     for user, rating in ratings.items():
#         if rating[idx] != 0:
#             sum += rating[idx]
#             count += 1
#     if count == 0:
#         avg = 0.0
#     else:
#         avg = float(sum/count)
#     return avg
#     #YEP

def similarities(name, ratings):
    '''
    This function calculates how similar the rater called name is to all other raters.
    A two-tuple is returned, where the first element is a string and the second element is an integer.
    '''
    ret = []
    comparelst = ratings[name]
    for i in ratings:
        if i == name:
            continue
        otherlst = ratings[i]
        x = 0
        for j in range(len(comparelst)):
            x += comparelst[j] * otherlst[j]
        ret.append((i, x))
    alpha = sorted(ret)
    alpha.sort(key = operator.itemgetter(1), reverse = True)
    return alpha
#     name = Liam
#     ratings = {'Jose': [-2, 3, -4, -5], 'Liam': [1, 2, -3, 4], 'Max': [4, -5, 6, 6]}
#     fixedlist = ratings[name]
#     del ratings[name]
#     similaritydic = {}
#     for user, rating in ratings.items():
#         similarity = dotProduct(fixedlist, rating)
#         if user not in similaritydic:
#             similaritydic[user] = 0
#         similaritydic[user] += similarity
#     listsimilarities = list(similaritydic.items())
#     finallist = sorted(sorted(listsimilarities, key=lambda x:x), key=lambda x:x[1], reverse=True)
#     return finallist
    # returns [('Max', 0), ('Jose', -4)]
    # THIS WORKS YAY

# def dotProduct(list1, list2):
#     sum = 0
#     for i in range(len(list1)):
#         sum+=((list1[i])*(list2[i]))
#     return sum
 
def recommendations(name, items, ratings, size):
    '''
    This function calculates the weighted average ratings and makes recommendations 
    based on the parameters and weighted average. A two-tuple is returned, where 
    the first element is a string and the second element is a float.
    '''
    sim = similarities(name, ratings)
    eva = sim[0:size]
    evanames = []
    evanum = []
    newratings = {}
    for i in eva:
        evanames.append(i[0])
        evanum.append(i[1])
    for i in evanames:
        a = evanames.index(i)
        store = []
        for j in ratings[i]:
            weight = j * evanum[a]
            store.append(weight)
        newratings[i] = store
    return averages(items, newratings)
#     similaritieslst = similarities(name, ratings)
#     print(similaritieslst)
#     
#     print("items num: " + str(len(items)))
#     
#     dicweighted = []
#     for tup in similaritieslst[:size]: #IS IT SIZE OR SIZE+1
#         user = tup[0]
#         similarity = tup[1] 
#         userratings = ratings[user]
#         
#         mylst = [i*similarity for i in userratings]
#         dicweighted.append(mylst)
#     
#     print("dicweighted: ")
#     print(dicweighted)  
# #     values = list(zip(*dicweighted)) #unpack dicweighted and then zip it so it iterates the other way
# #     print(values)
#     sumlist = [0]*(len(items))
#     #print(sumlist)
#     count = 0
#     for i in range(len(dicweighted)):
#         for x in range(len(dicweighted[0])):
#             sumlist[x] += dicweighted[i][x]
#             if dicweighted[i][x]!=0:
#                 count+=1
#     
#     finallst = []
#     
#     print("sumlist: ")
#     print(sumlist)
#     
#     
#     for i in range(len(sumlist)):
#         myitem = items[i]
#         myavg = float((sumlist[i])/count)
#         finallst.append((myitem,myavg))
#     x = sorted(sorted(finallst, key=lambda x:x[0]), key=lambda x:x[1], reverse=True)
#     return x
            
#     for user, weightedrating in dicweighted:
#         for i in range(len(weightedrating)):
#     avglst = []
#     for i in range(len(values)):
#         removezero = [x for x in values[i] if x!=0]
#         if removezero==[]:
#             avglst.append(0)
#         else:
#             avg = float((sum(removezero))/len(removezero))
#             avglst.append(avg)
#     sortedavglst = sorted(avglst)
#     return sortedavglst
# def weightedAverage(dicweighted):
#     lstdicweightedvals = list(dicweighted.values())
#     print(lstdicweightedvals)
#     sum = 0
#     count = 0
#     lstcount = []
#     summedlst = []
#     for i in range(len(lstdicweightedvals)): #for each group
#         for x in range(len(lstdicweightedvals[0])): #for each number in group
#             if i!=x:
#                 number = lstdicweightedvals[i][x]
#                 Sum= []

if __name__ == '__main__':
    pass
#     name = 'Liam'
#     items = ['Cat', 'Dog', 'Zebra']
#     ratings = {'Liam': [10, 2, 5], 'Man-Lin': [2, 5, 0], 'Max': [7, 9, 1], 'Jose': [1, 2, 3]}
#     size = 2
#     print(recommendations(name, items, ratings, size))
    #print(weightedAverage({'Max': [0, 0, 0, 0], 'Jose': [8, -12, 16, 20]}))
#     print(recommendations(name, items, ratings, size))
    #print(similarities(name, ratings))
    #print(averages(['Cat', 'Dog'], {'Liam': [0, 0], 'Man-Lin': [0, 3], 'Max': [0, 6]}))