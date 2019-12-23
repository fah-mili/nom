# -*- coding: utf-8 -*-
from odoo import http

# class Testfah(http.Controller):
#     @http.route('/testfah/testfah/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/testfah/testfah/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('testfah.listing', {
#             'root': '/testfah/testfah',
#             'objects': http.request.env['testfah.testfah'].search([]),
#         })

#     @http.route('/testfah/testfah/objects/<model("testfah.testfah"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('testfah.object', {
#             'object': obj
#         })