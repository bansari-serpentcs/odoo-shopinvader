# -*- coding: utf-8 -*-
# Copyright 2017 Akretion (http://www.akretion.com).
# @author Sébastien BEAU <sebastien.beau@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class CrmLead(models.Model):
    """Enhance the object to add features."""

    _inherit = 'crm.lead'

    shopinvader_backend_id = fields.Many2one(
        'shopinvader.backend',
        'Shopinvader Backend')
