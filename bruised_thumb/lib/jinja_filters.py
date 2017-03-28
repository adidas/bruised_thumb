import jinja2
from docutils.core import publish_parts

def rst_filter(s):
	return jinja2.Markup(publish_parts(source=s, writer_name='html')['body'])