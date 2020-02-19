import yaml

wrk_raw = """
build:
  context: "../speed-tests"
  dockerfile: wrk/Dockerfile
volumes:
  - ".:/results"
command: -c64 -d5s -t8 -s urls.lua http://json-file-ristretto/
"""
wrk = yaml.load(wrk_raw, Loader=yaml.Loader)

image = "tivvit/shush:0.0.1"
volumes = ["../utils/urls.json:/app/urls.json"]

backends = ["json-file"]
cache = ["no", "big", "fast", "free", "lru", "ristretto"]

dc = {"version": "3", "services": {}}

dc["services"]["wrk"] = wrk

for b in backends:
    for c in cache:
        name = "{}-{}".format(b, c)
        dc["services"][name] = {
            "image": image,
            "volumes": volumes + ["./{}.yml:/app/conf.yml".format(name)]
        }

with open("docker-compose.yml", "w") as w:
    yaml.dump(dc, w)
