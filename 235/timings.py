import re
from pathlib import Path
from urllib.request import urlretrieve

tmp = Path('/tmp')
timings_log = tmp / 'pytest_timings.out'
if not timings_log.exists():
    urlretrieve(
        'https://bites-data.s3.us-east-2.amazonaws.com/pytest_timings.out',
        timings_log
    )


def get_bite_with_fastest_avg_test(timings: list) -> str:
    bite_avg = []
    for line in timings:
        match = re.search(r'^(\d+)\s=+\s(\d+)\spassed.+(\d+\.\d+)\sseconds', line.strip())
        if not match:
            continue
        bite_no = match.groups()[0]
        passed_count = int(match.groups()[1])
        runtime = float(match.groups()[2])
        avg_runtime = runtime / passed_count
        bite_avg.append((bite_no, avg_runtime))
    return sorted(bite_avg, key=lambda x: x[1])[0][0]
