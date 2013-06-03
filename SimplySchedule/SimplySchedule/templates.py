
from django.template import Template, Context
import datetime

raw_template = """<p>Thanks for placing an order from {{ company }}. It's scheduled to
ship on {{ ship_date|date:"F j, Y" }}.</p>

{% if ordered_warranty %}
<p>Your warranty information will be included in the packaging.</p>
{% else %}
<p>You didn't order a warranty, so you're on your own when
the products inevitably stop working.</p>
{% endif %}

<p>Sincerely,<br />{{ company }}</p>"""

upload_template = """Upload your csv file:<form></form>
 """

t = Template(raw_template)

c = Context({'person_name': 'John Smith',
	'company': 'Outdoor Equipment',
	'ship_date': datetime.date(2009, 4, 2),
    'ordered_warranty': False})

t.render(c)


Tom = { 'name': 'tom', 'session1':'A', 'session2':'B', 'session3':'C'}
attendee_template = """<ul>
{% for attendee in attendee_list %}
    <li>{{ attendee.name }} is attending sessions {{ attendee.session1 }}, \
{{ attendee.session2}} and {{ attendee.session3}}</li>
{ %empty }
Nobody is going to any workshops
{% endfor %}
</ul>"""

attendee_t = Template(attendee_template)
attendee_context = Context({'attendee': Tom})
attendee_t.render(attendee_context)

request_view_template = """<table> 
{% for key,value in vars %}
	<tr><td> {{ key }} </td><td> {{ value }} </td></tr>
{% endfor %}
</table>"""

