from odoo import models, fields
from datetime import date
from dateutil.relativedelta import relativedelta

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = 'Estate Property Module'

    name = fields.Char('Title', required = True)
    description = fields.Text('Description of estate')
    postcode = fields.Char()
    date_availability = fields.Date(default = lambda self: date.today() + relativedelta(months=3), copy = False)
    expected_price = fields.Float(required = True)
    selling_price = fields.Float(readonly = True, copy = False)
    bedrooms = fields.Integer(default = 2)
    garage = fields.Boolean(default = True)
    garden = fields.Boolean()
    garden_area = fields.Integer()
    active = fields.Boolean(default = True)
    living_area = fields.Integer()
    facades = fields.Integer()
    available_from = fields.Date()
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
    required = True,
    copy = False,
    default = 'new')







  