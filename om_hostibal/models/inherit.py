from odoo import api, fields, models


class NewInherit(models.Model):
    _inherit = 'sale.order'

    NewField = fields.Char(string="New we")
