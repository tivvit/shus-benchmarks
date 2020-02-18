import subprocess
import os
import time

# todo run dependency clusters

tests = [
    "json-file-ristretto",
    "json-file-lru",
    "json-file-big",
]

cwd = "../shush-speed-test"

for i in range(3):
    for t in tests:
        subprocess.run(["docker-compose", "up", "-d", t], cwd=cwd)
        time.sleep(2)
        subprocess.run(["docker-compose", "run", "wrk", "-c64", "-d5s",
                        "-t8", "-s", "urls.lua", "http://{}/bbUISe".format(t)],
                       cwd=cwd)
        subprocess.run(["docker-compose", "down"], cwd=cwd)
        pth = os.path.join("reports-shush", str(i))
        if not os.path.exists(pth):
            os.mkdir(pth)
        os.rename(cwd + "/result.json", "{}/{}.json".format(pth, t))
