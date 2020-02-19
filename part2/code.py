import jsontrips

"""
The skeleton file. You should implement your code here. Make sure that the code you write here runs properly
when called by the test2.py file in the root directory.`
"""


def similarity_path_dist(type1, type2):
    """2ai) Take two types in the TRIPS ontology as inputs, and return the similarity between them (a number).
              Implement the path distance algorithm in this function."""
    # IMPLEMENT FUNCTION HERE
    p_1 = [type1]
    current1 = type1
    edge = 0

    while 'parent' in jsontrips.ontology()[current1].keys() and jsontrips.ontology()[current1]['parent'] != "":
        p_1.append(jsontrips.ontology()[current1]['parent'])
        current1 = jsontrips.ontology()[current1]['parent']

    current2 = type2
    while 'parent' in jsontrips.ontology()[current2].keys() and jsontrips.ontology()[current2]['parent'] not in p_1:
        edge += 1
        current2 = jsontrips.ontology()[current2]['parent']

    return p_1.index(jsontrips.ontology()[current2]['parent']) + 1 + edge


def similarity_wu_palmer(type1, type2):
    """2aii) Take two types in the TRIPS ontology as inputs, and return the similarity between them (a number).
            Implement the wu palmer algorithm in this function."""
    # IMPLEMENT FUNCTION HERE

    l1 = []
    l2 = []
    cur1 = type1
    cur2 = type2
    while 'parent' in jsontrips.ontology()[cur1].keys() and jsontrips.ontology()[cur1]['parent'] != "":
        l1.append(cur1)
        cur1 = jsontrips.ontology()[cur1]['parent']

    while 'parent' in jsontrips.ontology()[cur2].keys() and jsontrips.ontology()[cur2]['parent'] != "":
        l2.append(cur2)
        cur2 = jsontrips.ontology()[cur2]['parent']

    l1.reverse()
    l2.reverse()
    index = 0
    # print (l1)
    # print (l2)
    while index < len(l1) and index < len(l2) and l1[index] == l2[index]:
        index = index + 1
    # print (index)

    return 2 * (index) / (len(l1) + len(l2))
    # p_1 = [type1]
    # depth1 = 1
    # current1 = type1
    # while 'parent' in jsontrips.ontology()[current1].keys() and jsontrips.ontology()[current1]['parent'] != "":
    #     p_1.append(jsontrips.ontology()[current1]['parent'])
    #     current1 = jsontrips.ontology()[current1]['parent']
    #     depth1 += 1
    #
    # depth2 = 1
    # current2 = type2
    # while 'parent' in jsontrips.ontology()[current2].keys() and jsontrips.ontology()[current2]['parent'] != "":
    #     depth2 += 1
    #     current2 = jsontrips.ontology()[current2]['parent']
    #
    # edge = 0
    # current3 = type2
    # while 'parent' in jsontrips.ontology()[current3].keys() and jsontrips.ontology()[current3]['parent'] not in p_1:
    #     current3 = jsontrips.ontology()[current3]['parent']
    #     edge += 1
    #
    # depth3 = depth2 - edge - 1
    #
    # return 2*depth3/(depth1 + depth2)


def most_similar_type(type1, type2, type_ref):
    """2b) Take two TRIPS types, type1 and type2, and return the type which is most similar to the reference type."""
    # IMPLEMENT FUNCTION HERE
    s_1 = similarity_path_dist(type1, type_ref)
    s_2 = similarity_path_dist(type2, type_ref)
    if s_1 < s_2:
        return type1
    else:
        return type2


def disambiguate_conjunction(word1, word2):
    """2c) Take two words, word1 and word2, and return the disambiguated type for word1 (assume that the two words
          are being used in a conjunction, e.g. "orange and lemon" vs "orange and yellow")."""
    # IMPLEMENT FUNCTION HERE

    pass