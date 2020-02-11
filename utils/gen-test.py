import json

from numpy.random import choice
from collections import Counter

d = list(json.load(open("urls.json", "r")).keys())
s = 10 ** 7
p = []
f = 0
url_template = "/{}\n"
samples = len(d)
step = 10 / samples
for i in range(samples):
    f += step
    p.append(f)
p = [i ** -1 for i in p]
sm = sum(p)
p = [i / sm for i in p]
c = choice(d, size=s, p=p)
print("Sample:\n{}".format(c[:100]))
print("Most common samples:\n{}".format(Counter(c).most_common(50)))

with open("test.txt", "w") as f:
    for i in c:
        f.write(url_template.format(i))
