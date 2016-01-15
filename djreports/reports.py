
class Report(object):

    title = ''
    subtitle = ''
    description = ''

    def __init__(self, data=None, title='', subtitle='', **params):
        self._data = data
        if title:
            self.title = title
        if subtitle:
            self.subtitle = subtitle
        self.params = params

    @property
    def headers(self):
        data = self.get_data()
        return data[0] if data else []

    @property
    def data(self):
        data = self.get_data()
        return data[1:] if data else []

    def get_data(self):
        """
        Override this method to return the data the report needs.
        This data can be in the following formats:
            * A list of lists, where the outer outer list contains rows and the
              inner list contains the data in each "cell" of the row. The first
              list should be the report headers while the rest of the lists are
              the report data.
        """
        return self._data
