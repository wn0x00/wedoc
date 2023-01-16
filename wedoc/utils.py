def _get_column_letter(col_idx):
    """Convert a column number into a column letter (3 -> 'C')

    Right shift the column col_idx by 26 to find column letters in reverse
    order.  These numbers are 1-based, and can be converted to ASCII
    ordinals by adding 64.

    """
    # these indicies corrospond to A -> ZZZ and include all allowed
    # columns
    if not 1 <= col_idx <= 18278:
        raise ValueError("Invalid column index {0}".format(col_idx))
    letters = []
    while col_idx > 0:
        col_idx, remainder = divmod(col_idx, 26)
        # check for exact division and borrow if needed
        if remainder == 0:
            remainder = 26
            col_idx -= 1
        letters.append(chr(remainder + 64))
    return "".join(reversed(letters))


_COL_STRING_CACHE = {}
_STRING_COL_CACHE = {}
for i in range(1, 18279):
    col = _get_column_letter(i)
    _STRING_COL_CACHE[i] = col
    _COL_STRING_CACHE[col] = i


def get_column_letter(
    idx,
):
    """Convert a column index into a column letter
    (3 -> 'C')
    """
    try:
        return _STRING_COL_CACHE[idx]
    except KeyError:
        raise ValueError("Invalid column index {0}".format(idx))


def column_index_from_string(str_col):
    """Convert a column name into a numerical index
    ('A' -> 1)
    """
    # we use a function argument to get indexed name lookup
    try:
        return _COL_STRING_CACHE[str_col.upper()]
    except KeyError:
        raise ValueError("{0} is not a valid column name".format(str_col))
