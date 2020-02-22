import yaml
import copy

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

config = {
    "server": {
        "address": "0.0.0.0:80"
    },
    "log": {
        "level": "info"
    }
}

backend_conf = {
    "json-file": {
        "path": "urls.json"
    }
}

cache_conf = {
    "big-cache": {
        "life-window-sec": 600,
        "clean-window-sec": 10,
        "max-entry-size-bytes": 256,
        "verbose": True,
        "hard-max-cache-size-mb": 1024,
    },
    "fast-cache": {
        "size-bytes": 1073741824,
    },
    "free-cache": {
        "expire-sec": 600,
        "size-kb": 1048576,
    },
    "lru-cache": {
        "max-elems": 10000000,
        "expire-sec": 600,
    },
    "ristretto-cache": {
        "counters": 100000000,  # 10 * elements
        "max-cost": 10000000,  # elements"
    },

}

for b in backends:
    for c in cache:
        name = "{}-{}".format(b, c)
        conf_name = "{}.yml".format(name)
        dc["services"][name] = {
            "image": image,
            "volumes": volumes + ["./{}:/app/conf.yml".format(conf_name)]
        }
        conf = copy.deepcopy(config)
        conf["backend"] = {
            b: backend_conf[b]
        }
        if c != "no":
            c_name = "{}-cache".format(c)
            conf["cache"] = {
                c_name: cache_conf[c_name]
            }
        with open(conf_name, "w") as w:
            yaml.dump(conf, w)

with open("docker-compose.yml", "w") as w:
    yaml.dump(dc, w)
