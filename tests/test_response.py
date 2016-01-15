from django.test import TestCase

from djreports import Report
from djreports.response import CSVReportResponse


class CSVReportResponseTests(TestCase):

    def test_response_has_200_status_code(self):
        report = Report([['Hello', 'World'], ['Hello', 'World']])

        response = CSVReportResponse(report)

        self.assertEqual(response.status_code, 200)

    def test_response_has_csv_content_type(self):
        report = Report([['Hello', 'World'], ['Hello', 'World']])

        response = CSVReportResponse(report)

        self.assertEqual(response._headers['content-type'],
                         ('Content-Type', 'text/csv'))

    def test_response_uses_default_file_name(self):
        report = Report([['Hello', 'World'], ['Hello', 'World']])

        response = CSVReportResponse(report)

        self.assertEqual(response._headers['content-disposition'],
                         ('Content-Disposition', 'attachment; filename="report.csv"'))

    def test_response_has_csv_file_content(self):
        report = Report([['Col1', 'Col2'], ['Cell1', 'Cell2']])

        response = CSVReportResponse(report)

        self.assertEqual(response.content, 'Col1,Col2\r\nCell1,Cell2\r\n')
