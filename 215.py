ROW_NUM = 10

#yes, there is itertools.permutations but that's boring isn't it?
def calc_permutations(vlist, rest_list):
    if len(rest_list) == 0:
        add_list_to_permutations(vlist)   
        return
    new_rest = list(rest_list)
    new_vlist = list(vlist)
    if all_the_same(new_rest):
        new_vlist.extend(new_rest)
        new_rest = ()
        calc_permutations(new_vlist, new_rest)
    else:
        #2
        new_new_rest1 = list(new_rest)
        new_new_rest1.remove(2)
        new_new_vlist1 = list (new_vlist)
        new_new_vlist1.append(2)
        calc_permutations(new_new_vlist1, new_new_rest1)
        #3
        new_new_rest2 = list(new_rest)
        new_new_rest2.remove(3)
        new_new_vlist2 = list (new_vlist)
        new_new_vlist2.append(3)
        calc_permutations(new_new_vlist2, new_new_rest2)


def all_the_same (l):
    first = l[0]
    same = True
    for i in range(1, len(l)):
        if l[i] != first:
            same = False
    return same


def add_list_to_permutations(arg_list):
	p_list = list(arg_list)
	sum = 0
	value = ""
	p_list.pop()
	for number in p_list:
		sum = sum + number
		value = value + str(sum) + '-'
	value = value[:len(value)-1]
	permutations.add(value)


def generate_follower_map():
	permutation_list = list(permutations)
	followers = {}
	all_permutations = permutations
	for current in all_permutations:
		numbers = current.split('-')
		for permutation in permutation_list:
			contains = False
			for number in numbers:
				number_str = '-' + number + '-'
				if number_str in permutation:
					contains = True
				elif permutation.startswith(number + '-'):
					contains = True
				elif permutation.endswith('-' + number):
					contains = True			
			if not contains:
				follower_set = followers.get(current)
				if follower_set is None:
					follower_set = set()
				follower_set.add(permutation)
				followers[current] = follower_set
	return followers


def build_row(current_rows, followers):
	for i in range(1,ROW_NUM):
		next_rows = {}
		for row, value in current_rows.iteritems():
			follow_rows = followers[row]
			for f_row in follow_rows:
				if f_row not in next_rows:
					next_rows[f_row] = value
				else:
					next_rows[f_row] = next_rows[f_row] + value
		current_rows = next_rows
	return sum(current_rows.values())


permutations = set()
#16 x 2
perm_0=[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]
#13 x 2, 2 x 3
perm_1=[2,2,2,2,2,2,2,2,2,2,2,2,2,3,3]
#10 x 2, 4 x 3
perm_2=[2,2,2,2,2,2,2,2,2,2,3,3,3,3]
 #7 x 2, 6 x 3
perm_3=[2,2,2,2,2,2,2,3,3,3,3,3,3]
 #4 x 2, 8 x 3
perm_4=[2,2,2,2,3,3,3,3,3,3,3,3]
 #1 x 2, 10 x 3
perm_5=[2,3,3,3,3,3,3,3,3,3,3]
calc_permutations([],perm_0)
calc_permutations([],perm_1)
calc_permutations([],perm_2)
calc_permutations([],perm_3)
calc_permutations([],perm_4)
calc_permutations([],perm_5)
print "permutations generated"
followers = generate_follower_map()
#print followers
print "follower map generated"

initial_row_map = {}
for permutation in followers.keys():
	initial_row_map[permutation] = 1

count = build_row(initial_row_map, followers)
print count