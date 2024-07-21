# Copyright 2024 Jérémy Didderen
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import logging

from odoo import models

_logger = logging.getLogger(__name__)


class ResUsers(models.Model):
    _inherit = "res.users"

    def action_open_security_overview(self):
        self.ensure_one()
        access_dict = self.groups_id._get_access_rights_per_model()
        wizards = self.env["security.overview.wizard"].create(
            list(access_dict.values())
        )
        action = self.env["ir.actions.actions"]._for_xml_id(
            "security_overview.security_overview_wizard_action"
        )
        action["domain"] = [("id", "in", wizards.ids)]
        action["display_name"] = f"Security Overview for {self.name}"
        return action
