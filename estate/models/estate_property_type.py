from odoo import models, fields
from datetime import date
from dateutil.relativedelta import relativedelta

class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = 'Estate Property Type Module'

    name = fields.Char('Title', required = True)
    description = fields.Text('Description of estate type')
    postcode = fields.Char()
    date_availability = fields.Date(default = lambda self: date.today() + relativedelta(months=3), copy = False)
    available_from = fields.Date()
    expected_price = fields.Float(required = True)
    selling_price = fields.Float(readonly = True, copy = False)
