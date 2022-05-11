docs = list()
rawDocs = list()
res = ""
for i in range(0,5):
    filename = "doc" + str(i+1) + ".txt"
    with open(filename) as file:
        for line in file:
            tmp = re.sub(r"\!|\(|\)|\,|\n|\'|\?|\.|\"|\”|\“|\:|\;", "", line)
            tmp = re.sub("\—", " ", tmp)
            tmp = str.lower(tmp)
            rawDocs.append(tmp)
    for s in rawDocs:
        res += s + " "
    docs.append(res[:-1])