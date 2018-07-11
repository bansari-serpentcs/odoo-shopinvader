# -*- coding: utf-8 -*-
# Copyright 2017 Akretion (http://www.akretion.com).
# @author Sébastien BEAU <sebastien.beau@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Shopinvader Google Shopping',
    'version': '10.0.1.0.0',
    'author': "Akretion, "
              "Serpent Consulting Services Pvt. Ltd.",
    'website': 'http://www.akretion.com',
    'license': 'AGPL-3',
    'category': 'E-commerce',
    'summary': 'Export your product in google shopping',
    'depends': [
        'shopinvader',
    ],
    'data': [
        'views/google_category_view.xml',
        'views/product_view.xml',
        'wizard/import_google_category_view.xml',
        'data/ir_cron.xml',
        'data/ir_parameter.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
}
