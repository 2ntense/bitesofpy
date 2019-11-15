from enum import Enum
from datetime import datetime
from collections import Counter


class DateFormat(Enum):
    DDMMYY = 0  # dd/mm/yy
    MMDDYY = 1  # mm/dd/yy
    YYMMDD = 2  # yy/mm/dd
    NONPARSABLE = -999

    @classmethod
    def get_d_parse_formats(cls, val=None):
        """ Arg:
        val(int | None) enum member value
        Returns:
        1. for val=None a list of explicit format strings 
            for all supported date formats in this enum
        2. for val=n an explicit format string for a given enum member value
        """
        d_parse_formats = ["%d/%m/%y", "%m/%d/%y", "%y/%m/%d"]
        if val is None:
            return d_parse_formats
        if 0 <= val <= len(d_parse_formats):
            return d_parse_formats[val]
        raise ValueError


class InfDateFmtError(Exception):
    """custom exception when it is not possible to infer a date format
    e.g. too many NONPARSABLE or a tie """
    pass


def _maybe_DateFormats(date_str):
    """ Args:
    date_str (str) string representing a date in unknown format
    Returns:
    a list of enum members, where each member represents
    a possible date format for the input date_str
    """
    d_parse_formats = DateFormat.get_d_parse_formats()
    maybe_formats = []
    for idx, d_parse_fmt in enumerate(d_parse_formats):
        try:
            _parsed_date = datetime.strptime(date_str, d_parse_fmt)  # pylint: disable=W0612
            maybe_formats.append(DateFormat(idx))
        except ValueError:
            pass
    if len(maybe_formats) == 0:
        maybe_formats.append(DateFormat.NONPARSABLE)
    return maybe_formats


def get_dates(dates):
    """ Args:
    dates (list) list of date strings
    where each list item represents a date in unknown format
    Returns:
    list of date strings, where each list item represents
    a date in yyyy-mm-dd format. Date format of input date strings is
    inferred based on the most prevalent format in the dates list.
    Alowed/supported date formats are defined in a DF enum class.
    """
    c = Counter()

    for d in dates:
        mdf = _maybe_DateFormats(d)
        for df in mdf:
            if df == DateFormat.DDMMYY:
                c[DateFormat.DDMMYY] += 1
            elif df == DateFormat.MMDDYY:
                c[DateFormat.MMDDYY] += 1
            elif df == DateFormat.YYMMDD:
                c[DateFormat.YYMMDD] += 1
            else:
                c[DateFormat.NONPARSABLE] += 1

    mc = c.most_common(2)
    if mc[0][1] == mc[1][1]:
        raise InfDateFmtError()

    most_prevalent = mc[0][0]
    if most_prevalent == DateFormat.NONPARSABLE:
        raise InfDateFmtError()

    df = DateFormat.get_d_parse_formats(val=most_prevalent.value)

    date_list = list()
    for d in dates:
        try:
            date_list.append(datetime.strptime(d, df).strftime("%Y-%m-%d"))
        except ValueError:
            date_list.append("Invalid")

    return date_list


dates = [
    "04/25/79",
    "08/09/70",
    "08/04/10",
    "95/31/10",
    "06/13/34",
    "04/03/22",
    "67/12/17",
    "34/10/12",
    "04/05/94",
    "07/12/41",
    "88/11/05",
    "96/26/08",
]

print(get_dates(dates))
