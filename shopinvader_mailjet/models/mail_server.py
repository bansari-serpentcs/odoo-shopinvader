# -*- coding: utf-8 -*-
# Copyright 2017 Akretion (http://www.akretion.com).
# @author Sébastien BEAU <sebastien.beau@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class IrMailServer(models.Model):
    """Enhance the object to add feature."""

    _inherit = 'ir.mail_server'

    server_type = fields.Selection([
        ('mailjet', 'Mailjet'),
        ('smtp', 'Smtp')],
        default='smtp',
        required=True)

    @api.onchange('server_type')
    def onchange_type(self):
        """The onchange used to set smtp_host based on server type."""
        self.ensure_one()
        if self.server_type == 'mailjet':
            self.smtp_host = 'mailjet'
