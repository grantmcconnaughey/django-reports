from django.test import TestCase

from djreports import Report

from .models import Company, Employee


class TestReport(Report):
    title = 'Test Report Title'
    subtitle = 'Test Report Subtitle'


class CompanyTestReport(Report):
    title = 'Company Report'
    fields = ['name', 'website']

    def get_data(self):
        return Company.objects.all()


class EmployeeTestReport(Report):
    title = 'Company Report'
    fields = ['first_name', 'last_name', 'company']

    def get_data(self):
        return Employee.objects.all()


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


class ModelReportTests(TestCase):

    def test_model_report_headers_capitalize(self):
        Company.objects.create(name='GitHub', website='http://github.com')

        report = CompanyTestReport()

        self.assertEqual(report.headers, ['Name', 'Website'])

    def test_model_report_headers_remove_underscores(self):
        company = Company.objects.create(name='GitHub', website='http://github.com')
        employee = Employee.objects.create(first_name='Louis', last_name='CK', company=company)

        report = EmployeeTestReport()

        self.assertEqual(report.headers, ['First name', 'Last name', 'Company'])

    def test_model_report_data(self):
        Company.objects.create(name='GitHub', website='http://github.com')

        report = CompanyTestReport()

        self.assertEqual(report.data, [['GitHub', 'http://github.com']])

    def test_model_report_data_with_foreign_keys(self):
        company = Company.objects.create(name='GitHub', website='http://github.com')
        employee = Employee.objects.create(first_name='Louis', last_name='CK', company=company)

        report = EmployeeTestReport()

        self.assertEqual(report.data, [['Louis', 'CK', 'GitHub']])

    def test_model_report_data_with_null_foreign_keys(self):
        employee = Employee.objects.create(first_name='Louis', last_name='CK')

        report = EmployeeTestReport()

        self.assertEqual(report.data, [['Louis', 'CK', '']])

    # def test_model_report_data_with_many_to_many_field
    # def test_model_report_data_with_date_field
    # def test_model_report_data_with_boolean_field
