import node

OLD 	= False
NEW 	= True
if NEW:
	A 	= [(5,10), (10,15), (16,18), (25,30), (31,32)]
	B 	= [(1,3), (10,12), (16,18), (18,22), (21,22), (60,70) ]
	T 	= node.tree(B)
	for b in A:
		print b ,T.searchInterval(b)
if OLD:
	#============================================
	#Simple list of overlaping intervals, these 
	#intervals can be arbitrarily long and overlapping

	#============================================
	#to make you interval tree strucutre you need 
	#to have a list of tuples. The first element
	#in the tuple is the start location the second
	#element is the stop location, and the 
	#third element is optional but can be anything
	LST 		= [(1,4,"Interval_A"), (3,8, "Interval_B"), (10,20,"Interval_C"), (15,25, "Interaval_D") ]
	#============================================
	#now all you need is to instantiate your
	#instance of node.tree, takes in your list, LST
	T 			= node.tree(LST)
	#============================================
	#now you can do ask whether or not an incoming
	#point (single value) overlaps any elements
	#in your list. This will return all intervals
	#that overlap your point, you call by
	#T.searchPoint(x), if there is no interval
	#that overlaps your query you will get an empty list

	test_pt_1 	= 3.4 	#should overlap 2
	test_pt_2 	= 9 	#should overlap 0
	test_pt_3 	= 13 	#should overlap 1
	test_pt_4 	= 17.8 	#should overlap 2
	test_pt_5 	= 26 	#should overlap 0
	FINDS_1 	= T.searchPoint(test_pt_1) #returns a list of tuples (start, stop, INFO)
	print FINDS_1 #should look like this -> [(1, 4, 'Interval_A'), (3, 8, 'Interval_B')]
	assert len(FINDS_1)==2, "DID NOT PASS"
	FINDS_2 	= T.searchPoint(test_pt_2)
	assert len(FINDS_2)==0, "DID NOT PASS"
	FINDS_3 	= T.searchPoint(test_pt_3)
	assert len(FINDS_3)==1, "DID NOT PASS"
	FINDS_4 	= T.searchPoint(test_pt_4)
	assert len(FINDS_4)==2, "DID NOT PASS"
	FINDS_5 	= T.searchPoint(test_pt_5)
	assert len(FINDS_5)==0, "DID NOT PASS"

	#============================================
	#you can do the same thing with intervals
	#you need to call T.searchInterval(tple)
	#where tple is a tuples of start and stop
	#if there is no interval that overlaps your
	#query you will get an empty list

	test_int_1 	= (3,5) #should overlap 2
	test_int_2 	= (12,18) #should overlap 2
	test_int_3 	= (11,13) 	#should overlap 1
	test_int_4 	= (26,30) 	#should overlap 0
	test_int_5 	= (24,30) 	#should overlap 1
	FINDS_1 	= T.searchInterval(test_int_1) #returns a list of tuples (start, stop, INFO)
	print FINDS_1 #should look like this -> [(1, 4, 'Interval_A'), (3, 8, 'Interval_B')]
	assert len(FINDS_1)==2, "DID NOT PASS"
	FINDS_2 	= T.searchInterval(test_int_2)
	assert len(FINDS_2)==2, "DID NOT PASS"
	FINDS_3 	= T.searchInterval(test_int_3)
	assert len(FINDS_3)==1, "DID NOT PASS"
	FINDS_4 	= T.searchInterval(test_int_4)
	assert len(FINDS_4)==0, "DID NOT PASS"
	FINDS_5 	= T.searchInterval(test_int_5)
	assert len(FINDS_5)==1, "DID NOT PASS"




