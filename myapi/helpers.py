import os
from pathlib import Path


def get_last_n_files_in_dir(dir_path, n, recurse=False, *args, **kwargs):
    method_str = "rglob" if recurse else "glob"
    p = Path(dir_path)
    fluid_glob = getattr(p, method_str)

    l = [(i, i.stat().st_mtime) for i in fluid_glob("*.*")]
    l.sort(key=lambda x: x[0], **kwargs)
    l_ = l[:n]

    return [i[0] for i in l_]


def delete_last_n_files_in_dir(dir_path, *args, **kwargs):
    fpaths = get_last_n_files_in_dir(dir_path, *args, **kwargs)
    for p in fpaths:
        os.remove(p)