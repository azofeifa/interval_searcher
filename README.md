# interval_searcher
Constructs a simple interval tree from a list of python tuples of start and stop locations, does not support adding or deleting intervals from the tree.
##Usage
To make you interval tree strucutre you need to have a list of tuples. The first element in the tuple is the start location the second element is the stop location, and the third element is optional but can be anything.
LST=[(1,5, "A"), (3,10, "B")...]
import node
T=node.tree(LST)
Once tree() is instantiated with your list, you can call searchPoint or searchInterval
to ask whether or not an incoming
point (single value) or interval (tuple of start, stop) overlaps any elements
in your list. This will return all intervals
that overlap your point and an empty list if none overlap, 
x = 3
T.searchPoint(x), if there is no interval
x = (3,7)
T.searchInterval(x)
