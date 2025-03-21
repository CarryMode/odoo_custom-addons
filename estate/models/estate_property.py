from odoo import models, fields
from datetime import date
from dateutil.relativedelta import relativedelta

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = 'Estate Property Module'

    name = fields.Char('Estate Property', required = True)
    description = fields.Text('Description of estate')
    postcode = fields.Char()
    date_availability = fields.Date(default = lambda self: date.today() + relativedelta(months=3), copy = False)
    expected_price = fields.Float(required = True)
    selling_price = fields.Float(readonly = True, copy = False)
    bedrooms = fields.Integer(default = 2)
    garage = fields.Boolean(default = True)
    garden = fields.Boolean()
    garden_area = fields.Integer()
    active = fields.Boolean()
    garden_orientation = fields.Selection([
        ('north','North'),
        ('south','South'),
        ('east','East'),
        ('west','West'),
    ])
    state = fields.Selection([
        ('new','New'),
        ('offer received','Offer Recieved'),
        ('offer accepted','Offer Accepted'),
        ('sold','Sold'),
        ('cancelled','Cancelled'),
    ],
    requider = True,
    copy = False,
    default = 'new')







  