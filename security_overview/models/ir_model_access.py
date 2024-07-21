# Copyright 2024 Jérémy Didderen
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class IrModelAccess(models.Model):
    _inherit = "ir.model.access"

    ir_module_ids = fields.Many2many(
        comodel_name="ir.module.module", compute="_compute_ir_module_ids"
    )

    def _compute_ir_module_ids(self):
        for access_right in self:
            xml_ids = access_right._get_external_ids()
            if xml_ids:
                module_names = list(
                    set(xml_id.split(".")[0] for xml_id in xml_ids[access_right.id])
                )
                access_right.ir_module_ids = self.env["ir.module.module"].search(
                    [("name", "in", module_names)]
                )
            else:
                access_right.ir_module_ids = False
