import os
import json


def get_json(fn, script=__file__):
    f = open(get_local_path(fn, script))
    return json.load(f)


def get_folder(script):
    return os.path.dirname(os.path.realpath(script))


def dump_json(data, fn, script=__file__):
    with open(get_local_path(fn, script), 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def get_local_path(fn, script):
    return get_folder(script) + os.sep + fn
