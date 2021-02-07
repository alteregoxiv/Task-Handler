"""
USING JINJA2 TEMPLATE 
"""

from jinja2 import (
    Environment,
    FileSystemLoader,
    select_autoescape
)

env = Environment(
    loader = FileSystemLoader('app/views'),
    autoescape = select_autoescape(['html'])
)


def template(filename, **kwargs):
    return env.get_template(filename).render(kwargs)
