import csv

from django.http.response import HttpResponse


class CSVReportResponse(HttpResponse):

    def __init__(self, report, file_name='report.csv', *args, **kwargs):
        kwargs['content_type'] = 'text/csv'
        super(CSVReportResponse, self).__init__(*args, **kwargs)
        self['Content-Disposition'] = 'attachment; filename="{}"'.format(file_name)

        writer = csv.writer(self)
        writer.writerow(report.headers)
        for row in report.data:
            writer.writerow(row)
