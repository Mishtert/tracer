class CaseInsensitiveDict(dict):
    def __init__(self, *args, **kwargs):
        self._keystore = {}
        d = dict(*args, **kwargs)
        for k in list(d.keys()):
            self._keystore[self._get_lower(k)] = k
        return super(CaseInsensitiveDict,self).__init__(*args,**kwargs)

    def __setitem__(self, k, v):
        self._keystore[self._get_lower(k)] = k
        return super(CaseInsensitiveDict, self).__setitem__(k, v)

    def __getitem__(self, k):
        return super(CaseInsensitiveDict,
                self).__getitem__(self._keystore[self._get_lower(k)])
    @staticmethod
    def _get_lower(k):
        if isinstance(k,str):
            return k.lower()
        else:
            return k