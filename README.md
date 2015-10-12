# interval_searcher
A wrapper class for various interval searching algorithms. Can take arbitrary number of lists of intervals and they may be overlaping (interval tree is constructed in this case)
##Usage
[1] import intervals

Each list must be of tuples of start and stop values, anything else in the tuple is saved in interval class as INFO

[2] A 	= [(1,5, "A1"), (4,10, "A2"),  (13,15, "A3"), (32, 34, "A4"), (61,68, "A5")]

[3] B 	= [(1,6, "B1"), (7,15, "B2"),  (16,17, "B3" ), (62,69, "B4") ]

[4] C 	= [(2,6, "C1"), (18,20, "C2"),  (21,23, "C3"), (25, 29), (31, 35)]

[5] D 	= [(2,7, "D1"), (12, 17, "D2"), (61,65, "D3")]

[6] ST 	= intervals.comparison((A,B,C, D) )

[7] OVERLAPS_0_1 	  = ST.find_overlaps(0,1)

[8] OVERLAPS_0_1_2	= ST.find_overlaps(0,1,2)

[9] UNIQUE_2 	      = ST.get_isolated(2)

We can also compute all possible overlaps (i.e. venn diagram or more formally a powerset)

[10] V = ST.compute_venn(0,1, 2,3, display=False )

[11] UNIQUE_2 = V.get_comparison(2)

[12] ALL_NOT_MUTUAL_EXCLUSIVE_OVERLAPS 	= V.get_comparison(0,1,3)

Turning display to true plots a venn diagram of the overlaping intervals althrough is only supported for two or three comparisons.

Please see example_usage.py for a quick tutorial

![Alt text](https://github.com/azofeifa/interval_searcher/blob/master/FIG_2.png)

![Alt text](https://github.com/azofeifa/interval_searcher/blob/master/FIG.png)


