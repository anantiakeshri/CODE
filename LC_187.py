# 187. Find Repeated DNA Sequence

s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
# Output: ["AAAAACCCCC","CCCCCAAAAA"]

def findRepeatedSequence(s):
    seen, res = set(), set()

    for l in range(len(s) - 9):
        cur = s[l: l + 10]
        if cur in seen:
            res.add(cur)
        seen.add(cur)
    return list(res)

print(findRepeatedSequence(s))