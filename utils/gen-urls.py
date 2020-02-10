import random
import string
import json

if __name__ == '__main__':
    l = 6
    N = 10 ** 6
    url_template = "https://{}.com/"
    alpha = string.ascii_letters + string.digits
    print("Alphabet: {}".format(alpha))
    print("Length {}".format(l))
    print("Possible combinations {}".format(len(alpha) ** l))
    shorts = set()
    while len(shorts) < N:
        rand_short = ''.join(random.choices(alpha, k=l))
        if rand_short not in shorts:
            shorts.add(rand_short)
    url_mapping = {i: url_template.format(i) for i in shorts}
    json.dump(url_mapping, open("urls.json", "w"))
