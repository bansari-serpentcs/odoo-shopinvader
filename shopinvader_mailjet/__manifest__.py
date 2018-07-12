# -*- coding: utf-8 -*-
# Copyright 2017 Akretion (http://www.akretion.com).
# @author Sébastien BEAU <sebastien.beau@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Shopinvader MailJet',
    'version': '10.0.1.0.0',
    'author': "Akretion, "
              "Serpent Consulting Services Pvt. Ltd.",
    'website': 'https://www.akretion.com',
    'license': 'AGPL-3',
    'category': 'mail',
    'summary': 'Send shopinvader email using mailjet API',
    'external_dependencies': {
        'python': ['mailjet_rest'],
        'bin': [],
    },
    'depends': [
        'shopinvader',
        # 'account_invoice_sale_link',
    ],
    'data': [
        'views/email_template_view.xml',
        'views/mail_server_view.xml',
        'views/mail_mail_view.xml',
    ],
    'installable': True,
}
