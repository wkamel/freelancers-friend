
class ItemOfferMissingParamException(Exception):
    def __init__(self, msg):
        self.msg = "Field %s missing" % msg

    def __str__(self):
        return repr(self.msg)


class ItemOffer(object):
    """
    Object for storing offers from downloaders
    """
    _fields = ['id', 'title', 'description', 'source', 'url']

    def __init__(self, **kwargs):
        map(lambda param: setattr(self, param, kwargs[param]), kwargs)

        for f in self._fields:
            try:
                getattr(self, f)
                # setattr(self, f, val.strip())
            except:
                raise ItemOfferMissingParamException(f)

    # def __repr__(self):
    #    pass
    #    return u" ItemOffer %s from %s" % (self.title, self.source)
