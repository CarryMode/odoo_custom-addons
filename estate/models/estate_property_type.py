from odoo import models, fields


class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = 'Estate Property Type Module'

    name = fields.Char('Name', required = True)