"""
Model for database tasks table
"""

from pydal import Field
from .connect import db


db.define_table('tasks',
               Field('title', required=True, notnull=True),
               Field('description', type='text'),
               Field('deadline', type='datetime', required=True, notnull=True),
               Field('done', type='boolean', required=True, notnull=True, default=False),
               Field('owner', type='reference users', required=True, notnull=True, ondelete='CASCADE')
               )

db.executesql('CREATE INDEX IF NOT EXISTS idx_tasks__owner ON tasks (owner);')

db.commit()
