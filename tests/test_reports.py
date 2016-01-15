from django.test import TestCase

from djreports import Report


class TestReport(Report):
    title = 'Test Report Title'
    subtitle = 'Test Report Subtitle'


class ReportTests(TestCase):

    def test_report_instance_attrs_do_not_change_class_attrs(self):
        report = TestReport(title='Report Title',
                            subtitle='Report Subtitle')

        self.assertEqual(report.title, 'Report Title')
        self.assertEqual(report.subtitle, 'Report Subtitle')
        self.assertEqual(TestReport.title, 'Test Report Title')
        self.assertEqual(TestReport.subtitle, 'Test Report Subtitle')

    def test_report_uses_class_attrs_if_not_overridden(self):
        report = TestReport()

        self.assertEqual(report.title, 'Test Report Title')
        self.assertEqual(report.subtitle, 'Test Report Subtitle')
        self.assertEqual(TestReport.title, 'Test Report Title')
        self.assertEqual(TestReport.subtitle, 'Test Report Subtitle')

    def test_can_pass_in_data(self):
        data = [
            ['Name', 'Age'],
            ['Grant', '24'],
            ['Erica', '24'],
        ]
        report = TestReport(data=data)

        self.assertEqual(report.get_data(), data)

    def test_can_override_get_data(self):
        data = [
            ['Name', 'Age'],
            ['Grant', '24'],
            ['Erica', '24'],
        ]
        class NewTestReport(Report):

            def get_data(self):
                return data

        report = NewTestReport()

        self.assertEqual(report.get_data(), data)

    def test_data_returns_empty_list_if_no_data(self):
        report = TestReport()

        self.assertEqual(report.data, [])

    def test_report_works_with_one_row(self):
        data =[
            ['Name', 'Age'],
        ]
        report = TestReport(data)

        self.assertEqual(report.headers, ['Name', 'Age'])
        self.assertEqual(report.data, [])

    def test_report_works_with_empty_list_data(self):
        report = TestReport([])

        self.assertEqual(report.headers, [])
        self.assertEqual(report.data, [])

    def test_report_works_with_None_data(self):
        report = TestReport(data=None)

        self.assertEqual(report.headers, [])
        self.assertEqual(report.data, [])
