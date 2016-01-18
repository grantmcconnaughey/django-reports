from django.db.models.query import QuerySet


class Report(object):

    title = ''
    subtitle = ''
    description = ''
    fields = []

    def __init__(self, data=None, title='', subtitle='', **params):
        self._data = data
        if title:
            self.title = title
        if subtitle:
            self.subtitle = subtitle
        self.params = params

    @property
    def headers(self):
        return self.get_headers()

    def get_headers(self):
        data = self.get_data()
        if data and isinstance(data, (list, tuple)):
            return data[0]
        elif data and isinstance(data, QuerySet):
            return [field.capitalize().replace('_', ' ') for field in self.fields]
        else:
            return []

    def _format_field(self, field_value):
        return '' if field_value is None else str(field_value)

    @property
    def data(self):
        data = self.get_data()
        if data and isinstance(data, (list, tuple)):
            # List/tuple reports
            return data[1:]
        elif data and isinstance(data, QuerySet):
            # Django Model reports
            instances = list(data)
            return [[self._format_field(getattr(instance, field))
                     for field in self.fields
                     if hasattr(instance, field)]
                    for instance in instances]
        else:
            return []

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
