class WedocApiBase:
    """接口基类"""

    def __init__(self, client=None) -> None:
        self._clent = client

    @property
    def base_url(self):
        return self._clent.access_token

    @property
    def corpid(self):
        return self._clent.corpid

    @property
    def corpsecret(self):
        return self._clent.corpsecret

    @property
    def access_token(self):
        return self._clent.access_token

    def request(self, *args, **kwargs):
        return self._clent.request(*args, **kwargs)
