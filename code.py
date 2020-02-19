import jsontrips
import json
"""
The skeleton file. You should implement your code here. Make sure that the code you write here runs properly
when called by the test2.py file in the root directory.`
"""


def similarity_path_dist(type1, type2):
    """2ai) Take two types in the TRIPS ontology as inputs, and return the similarity between them (a number).
              Implement the path distance algorithm in this function."""
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
    while index < len(l1) and index < len(l2) and l1[index] == l2[index]:
        index = index + 1

    return len(l1) + len(l2) - 2*index


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
    while index < len(l1) and index < len(l2) and l1[index] == l2[index]:
        index = index + 1

    return 2 * (index) / (len(l1) + len(l2))


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
    with open('part2/lexicon.json') as f:
        data = json.load(f)
    type = data[word2]["lf_parent"][0]
    type_list = data[word1]["lf_parent"]
    t_min = type_list[0]
    for t in type_list:
        t_min = most_similar_type(t, t_min, type)

    return t_min

