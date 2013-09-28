import itertools

thestr = "gghtgedghsdfgtds"

#Find out whether there are any duplicatged characters in a string:
charcounts = [(key,len(list(v))) for key,v in itertools.groupby(sorted(thestr))]
charcounts.sort(key=lambda x: x[1],reverse=True)
if filter(lambda x: x[1]>1,charcounts):
    print "Found duplicates"
else:
    print "No duplicates found"

#Strip out every consecutive repeating character
thestr = "gghtge   dghssssdfgtdddddd1ds"
print "".join([key for key,v in itertools.groupby(thestr)])

