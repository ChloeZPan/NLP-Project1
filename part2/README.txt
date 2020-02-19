Project1 Part2
---------------

Name: Zeyi Pan
Student ID: 
Email: 

(1) Execute
Windows Terminal Commend: python test2.py

(2) Algorithm

---------------------------
Algorithm similarity_path_dist
input: string type1, type2
output: integer similarity

l1 <- list[]
l2 <- list[]
cur1 <- type1
cur2 <- type2
while 'parent' is cur1's key and cur1's parent is not "" then
	add cur1 to l1
	cur1 <- cur1's parent
while 'parent' is cur2's key and cur2's parent is not "" then
	add cur2 to l2
	cur2 <- cur2's parent

l1 <- reverse l1
l2 <- reverse l2
index <- 0
while index < len(l1) and index < len(l2) and l1[index] == l2[index]:
	index <- index + 1

return len(l1) + len(l2) - 2*index

-----------------------
Algorithm similarity_wu_palmer
input: string type1, type2
output: integer similarity

l1 <- list[]
l2 <- list[]
cur1 <- type1
cur2 <- type2
while 'parent' is cur1's key and cur1's parent is not "" then
	add cur1 to l1
	cur1 <- cur1's parent
while 'parent' is cur2's key and cur2's parent is not "" then
	add cur2 to l2
	cur2 <- cur2's parent

l1 <- reverse l1
l2 <- reverse l2
index <- 0
while index < len(l1) and index < len(l2) and l1[index] == l2[index]:
	index <- index + 1
return 2 * (index) / (len(l1) + len(l2))

-----------------------
Algorithm most_similar_type
input: string type1, type2, type_ref
output: string type

s_1 <- similarity between type1 and type_ref
s_2 <- similarity between type2 and type_ref

if s_1 < s_2 then
	return type1
else
	return type2

------------------------
Algorithm disambiguate_conjunction
input: string word1, word2
output: string type

data <- read lexicon.json as dictionary
type <- the type of word2
type_list <- types of word1
t_min <- the fisrt element of type_list

for every item t in type_list
	t_min <- the most similar type to type_ref between t and t_min

return t_min
