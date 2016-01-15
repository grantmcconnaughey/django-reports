
class Report(object):

    title = ''
    subtitle = ''
    description = ''

    def __init__(self, title='', subtitle='', **params):
        if title:
            self.title = title
        if subtitle:
            self.subtitle = subtitle
        self.params = params

    def get_data(self):
        raise NotImplementedError

    @property
    def headers(self):
        pass
