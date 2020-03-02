# -*- coding: utf-8 -*-
from odoo import models, fields, _


class ResCompany(models.Model):
    """
        Representation of a company
    """
    _inherit = 'res.company'

    code = fields.Char(
        help='Company unique code',
        string='Code',
        # required=True
    )