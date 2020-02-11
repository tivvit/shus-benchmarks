import yaml


def configure(fn):
    return yaml.load(open(fn, "r"))


def configure_backend(conf):
    if "backend" not in conf:
        return
    if conf["backend"]["type"] == "json_file":
        from backend.json_file import JsonFile
        return JsonFile(conf["backend"]["path"])
    else:
        return


def configure_cache(conf, backend):
    if "cache" not in conf:
        return backend
    if conf["cache"] == "preload":
        from cache.preload import Preload
        return Preload(backend)
    else:
        return backend
