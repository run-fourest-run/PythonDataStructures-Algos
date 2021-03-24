'''
Sets are unordered collection of unique items. Sets are mutable, but the elements inside of them are immutable.

* Important distinctions is that the cannot contain duplicate keys
* Sets are typically used to perform mathmatical operations such as intersection, union, difference and complement.


Unlike sequence types, set types do not provide any indexing or slicing operations. There are also no keys associated with values.
'''

player_list = ['alex','spencer','don','don']
cod_players = set(player_list)



'''
Methods and operations:
'''


#len(s)
#length
length = len(cod_players)





#s.copy()
#copy
copy = cod_players.copy()

#s.add()
#add
copy.add('ryan')


#s.difference(t)
#difference --> returns all items in s but not in t
difference = cod_players.difference(copy)


#s.intersection(t)
#intersections --> returns a set of all items in both t and s
intersection = cod_players.intersection(copy)


#s.isdisjoint(t)
#is disjoint --> Returns True if S and t have no items in common

isdisjoint = cod_players.isdisjoint(copy)


#s.issubset(t)
# is subset --> Returns True if all items in s are also in t
subset = cod_players.issubset(copy)


#s.issuperset(t)
# is superset --> Returns True if all items in t are also in s

superset = cod_players.issuperset(copy)

#s.union(t)
# union --> returns a set of all items in s or t
union = cod_players.union(copy)



'''Mutable set object methods '''


#s.add(item)
#add
cod_players.add('doug')

#s.clear()
#clear
copy_cod_players = cod_players.copy()
copy_cod_players.clear()


#s.difference_update(t)
#difference update --? removes all items in s that are also in t
cod_players.difference_update(['spencer','alex'])


#s.discard(item)
#discard --> remove item from set
cod_players.discard('doug')


#s.intersection_update(t)
#intersection update --> removes all items from s that are not in the intersection of s and t
cod_players.intersection_update(['alex'])


#s.pop
#pop --> returns and removes
cod_players.pop('don')



#s.symetric_difference_updater
#symeteric difference updater --> removes all items from s that are not in the symettric difference of s and t (no idea what the fuck that means)
cod_players.symmetric_difference_update(['dontknow'])
