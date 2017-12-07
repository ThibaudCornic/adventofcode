#f = open("test7", "r")
f = open("input7", "r")

tuples={}
big_array={}

class Program:
    def __init__(self, name, weight, sub):
        self.name = name
        self.weight = weight
        self.cum_weight = weight

        # Construct the sub nodes
        self.sub = []
        for i in sub:
            self.sub.append(Program(*tuples[i]))

        # Am I balanced?
        if len(self.sub):
            weights = [ x.cum_weight for x in self.sub ]
            if max(weights) == min(weights):
                self.balanced = True
            for i in self.sub:
                self.cum_weight += i.cum_weight
        # A leaf is balanced
        else:
            self.balanced = True

    def find_wrong(self, diff):
        if self.balanced:
            return self.weight + diff

        weights = [ x.cum_weight for x in self.sub ]
        possible_wrong = [ i for i in range(len(self.sub)) if weights.count(self.sub[i].cum_weight) == 1 ]

        if len(self.sub) == 2:
            raise Exception("In {}, two unbalanced: {}".format(self.name, weights))

        if len(possible_wrong) > 1:
            raise Exception("In {}, more than one wrong: {}".format(self.name, possible_wrong))
        
        if not len(possible_wrong):
            raise Exception("In {} but there's no wrong son...".format(self.name))

        wrong = possible_wrong[0]

        if diff == 0:
            diff = self.sub[wrong-1].cum_weight - self.sub[wrong].cum_weight

        return self.sub[wrong].find_wrong(diff)

    def __str__(self):
        return self.print(0, recur=True)

    def print(self, depth, recur=False):
        string = "{}{}: weight {}, cum_weight {}, {} sons, balanced: {}, sons: {}\n".format(depth*'\t', self.name, self.weight, self.cum_weight, len(self.sub), self.balanced, [ s.name for s in self.sub ])
        if recur:
            for i in self.sub:
                string += i.print(depth+1, recur=recur)
        return string


# Construct a dict with all nodes as tuples: (name, weight, list of sub-nodes)
for i in f.readlines():
    words = i.split()
    name = words[0]
    weight = int(words[1].replace(')', '').replace('(',''))
    subs=[]
    if len(words) > 2:
        subs = [ x.replace(',', '') for x in words[3:] ]
    tuples[name] = (name, weight, subs)

possible_roots = list(tuples.keys())
for i in tuples.keys():
    for son in tuples[i][2]:
        possible_roots.remove(son)

# Now that we have the root, construct the tree
root = possible_roots[0]
a = Program(*tuples[root])
#print(a)

# Answer step 2
print(a.find_wrong(0))
