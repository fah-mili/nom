from odoo import api, fields, models, tools, _
from odoo.exceptions import ValidationError
import logging
import datetime
import io
import pytz
from base64 import b64encode
from lxml import etree
import os

class ATTransportMixin(models.AbstractModel):
    _name = 'at.transport.mixin'
    _description = 'AT Transport Mixin'

    vehicle_id = fields.Char(string='Vehicle License Plate FAH')