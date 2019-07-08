'''
@author: Kassen Qian kkq
'''
import RecommenderEngine
def makerecs(name, items, ratings, size, top):
    '''
    This function calculates the top recommendations and returns a two-tuple consisting of two lists. 
    The first list is the top items rated by the rater called name (string).
    The second list is the top items not seen/rated by name (string)
    '''
    watched = []
    recs = []
    a = RecommenderEngine.recommendations(name, items, ratings, size)
    for i in a:
        q = i[0]
        w = items.index(q)
        if ratings[name][w] == 0:
            recs.append(i)
        else:
            watched.append(i)
    return (watched[:top], recs[:top])
    

if __name__ == '__main__':
    pass



