import os

ONE_KB = 1024


def get_files(dirname, size_in_kb):
    """Return files in dirname that are >= size_in_kb"""
    with os.scandir(dirname) as it:
        return [e for e in it if e.is_file and (e.stat().st_size / ONE_KB) >= size_in_kb]
