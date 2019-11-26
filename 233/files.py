from datetime import datetime
from pathlib import Path, PosixPath
from zipfile import ZipFile

TMP = Path('/tmp')
LOG_DIR = TMP / 'logs'
ZIP_FILE = 'logs.zip'


def zip_last_n_files(directory: PosixPath = LOG_DIR,
                     zip_file: str = ZIP_FILE, n: int = 3):
    paths_dt = []
    for log_file in directory.glob('*.log'):
        creation_ts = log_file.stat().st_ctime
        paths_dt.append((log_file, datetime.fromtimestamp(creation_ts)))
    paths_dt.sort(key=lambda x: x[1], reverse=True)

    with ZipFile(zip_file, 'w') as file:
        for path, dt in paths_dt[:n]:
            date_str = dt.strftime("%Y-%m-%d")
            arcname = f"{path.stem}_{date_str}{path.suffix}"
            file.write(path, arcname=arcname)
