import operator

def maxSubSeqPal(s):
    if len(s) == 0:
        return 0
    if len(s) == 1:
        return 1
    lastPos = 0
    t = ""
    lettere = set(s)
    app = []; res = []
    dPos = {}; dDist = {}
    for el in lettere:
        while s.find(el, lastPos) != -1:
            app.append(s.index(el, lastPos))
            lastPos = s.index(el, lastPos) + 1
        dPos[el] = app
        lastPos = 0; app = []
    for key, values in dPos.items():
        if len(values) > 1:
            dDist[key] = values[len(values)-1] - values[0] + 1
    dDist = sorted(dDist.items(), key = operator.itemgetter(1))
    dDist = dDist[::-1]
    for i in range(len(dDist)):
        res.append(0)
    for i in range(len(dDist)):
        if res[i] > dDist[i][1]:
            break
        t = s[dPos[dDist[i][0]][0]+1:dPos[dDist[i][0]][len(dPos[dDist[i][0]])-1]]
        if len(t) == 0:
            res[i] += 2
        if len(t) == 1:
            res[i] += 3
        if len(t) > 1:
            res[i] += 2 + maxSubSeqPal(t)
    if len(res) == 0:
        return 0
    return max(res)

print(maxSubSeqPal("DATAMININGSAPIENZA"))