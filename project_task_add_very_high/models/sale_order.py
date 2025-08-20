# Copyright 2016-2020 Onestein (<https://www.onestein.eu>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    priority = fields.Selection(
        selection=[("1", "Very High"), ("3", "Most Important")],
        # ondelete={"priority": "set default"},
        default="1",
    )
