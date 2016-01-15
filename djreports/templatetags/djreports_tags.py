from django import template
from django.template.loader import render_to_string


register = template.Library()


@register.simple_tag()
def report_table(report):
    return render_to_string('djreports/report_table.html', {'report': report})

# report_bootstrap2_table
# report_bootstrap3_table
