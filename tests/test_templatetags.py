from django.test import TestCase

from djreports import Report
from djreports.templatetags import djreports_tags


class TestReport(Report):

    def get_data(self):
        return [
            ['Name', 'Age', 'DOB'],
            ['Grant', '24', '11/6/1991'],
            ['Erica', '23', '12/30/1991'],
        ]


class ReportsTagsTests(TestCase):

    def test_report_table_has_headers(self):
        report = TestReport()

        html = djreports_tags.report_table(report)

        self.assertIn('<th>Name</th>', html)
        self.assertIn('<th>Age</th>', html)
        self.assertIn('<th>DOB</th>', html)

    def test_report_table_has_data(self):
        report = TestReport()

        html = djreports_tags.report_table(report)

        self.assertIn('<td>Grant</td>', html)
        self.assertIn('<td>24</td>', html)
        self.assertIn('<td>11/6/1991</td>', html)
        self.assertIn('<td>Erica</td>', html)
        self.assertIn('<td>23</td>', html)
        self.assertIn('<td>12/30/1991</td>', html)
