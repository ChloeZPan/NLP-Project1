import jsontrips

"""
The skeleton file. You should implement your code here. Make sure that the code you write here runs properly
when called by the test1.py file in the root directory.`
"""


def check_subsumption(type1, type2):
    """1) Take two types in the TRIPS ontology as inputs. If one type is a subtype of the other, return the tuple
            (True, type), where type is the type that is a subtype. Otherwise, return the tuple (False, None)."""
    # IMPLEMENT FUNCTION HERE
    # def parent_lookup(goal, p):
    #     if 'parent' in jsontrips.ontology()[p].keys():
    #         if goal in jsontrips.ontology()[p]['parent']:
    #             return True
    #         else:
    #             parent_lookup(goal, jsontrips.ontology()[p]['parent'])
    #     else:
    #         return False
    def parent_lookup(goal, p):
        current = p
        while 'parent' in jsontrips.ontology()[current].keys() and jsontrips.ontology()[current]['parent'] != "":
            if goal in jsontrips.ontology()[current]['parent']:
                return True
            current = jsontrips.ontology()[current]['parent']
        return False

    if 'parent' in jsontrips.ontology()[type1].keys() and parent_lookup(type1, type2):
        return True, type2
    elif 'parent' in jsontrips.ontology()[type2].keys() and parent_lookup(type2, type1):
        return True, type1
    else:
        return False, None

