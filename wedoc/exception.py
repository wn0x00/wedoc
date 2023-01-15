class WeworkError(Exception):

    errcode = ""
    errmsg = ""


class IpLimitError(WeworkError):
    """'errcode': 60020, 'errmsg': 'not allow to access from your ip"""

    pass
