import itertools

thestr = "gghtgedghsdfgtds"

charcounts = [(key,len(list(v))) for key,v in itertools.groupby(sorted(thestr))]

charcounts.sort(key=lambda x: x[1],reverse=True)
if filter(lambda x: x[1]>1,charcounts):
    print "Found duplicates"
else:
    print "No duplicates found"
