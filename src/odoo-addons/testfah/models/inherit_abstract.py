from datetime import datetime

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class StockPicking(models.Model):
    _name = 'stock.picking'
    _inherit = ['stock.picking', 'at.transport.mixin']

    """ Add readonly states to everything except draft for all the fields in the report """
    name = fields.Char(readonly=True, states={'draft': [('readonly', False)]})

    vehicle_id = fields.Char(states={'done': [('readonly', True)], 'cancel': [('readonly', True)]})

    title22 = _("Title22fafafah")    

    res_partner_fafafah = fields.Many2one('res.partner', string='Partnerfafafah', translate=True)