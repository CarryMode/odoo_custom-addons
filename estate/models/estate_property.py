from odoo import models, fields

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = 'Test module for studying'

    name = fields.Char('Estate Name', required = True)
    description = fields.Text('Description of estate')
    postcode = fields.Char()
    date_availability = fields.Date()
    expected_price = fields.Float(required = True)
    selling_price = fields.Float()
    bedrooms = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection([
        ('North', 'north'),
        ('South', 'south'),
        ('East', 'east'),
        ('West', 'west'),
    ])






  