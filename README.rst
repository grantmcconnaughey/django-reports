=============================
django-reports
=============================

.. image:: https://badge.fury.io/py/django-reports.png
    :target: https://badge.fury.io/py/django-reports

.. image:: https://travis-ci.org/grantmcconnaughey/django-reports.png?branch=master
    :target: https://travis-ci.org/grantmcconnaughey/django-reports
    
.. image:: https://coveralls.io/repos/grantmcconnaughey/django-reports/badge.svg?branch=master&service=github
  :target: https://coveralls.io/github/grantmcconnaughey/django-reports?branch=master

A Django app to easily create and render reports.

Documentation
-------------

The full documentation is at https://django-reports.readthedocs.org.

Quickstart
----------

Install django-reports::

    pip install django-reports

Then use it in a project::

    from djreports import Report

    class MyReport(Report):

        title = 'My Report'
        description = 'A list of important things'

        def get_data(self):
            return Thing.objects.filter(type='important')

    report = MyReport()

And render the report in your template::

    {% load djreport_tags %}

    {% report_table report %}

Features
--------

* Create report objects out of Python lists or Django QuerySets.
* Render them to an HTML table or CSV

Running Tests
--------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install -r requirements-test.txt
    (myenv) $ python runtests.py

Credits
---------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-pypackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
