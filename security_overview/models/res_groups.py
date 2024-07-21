# Copyright 2024 Jérémy Didderen
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import logging

from odoo import models
from odoo.models import Command

_logger = logging.getLogger(__name__)


class ResGroups(models.Model):
    _inherit = "res.groups"

    def action_open_security_overview(self):
        self.ensure_one()
        access_dict = self._get_access_rights_per_model()
        wizards = self.env["security.overview.wizard"].create(
            list(access_dict.values())
        )
        action = self.env["ir.actions.actions"]._for_xml_id(
            "security_overview.security_overview_wizard_action"
        )
        action["domain"] = [("id", "in", wizards.ids)]
        action["display_name"] = f"Security Overview for {self.name}"
        return action

    def _get_access_rights_per_model(self):
        access_dict = {}
        access_rights = self.model_access.filtered(lambda m: not m.model_id.transient)
        for access_right in access_rights:
            if access_right.model_id.id not in access_dict:
                access_dict[access_right.model_id.id] = {
                    "model_id": access_right.model_id.id,
                    "group_ids": [Command.link(access_right.group_id.id)],
                    "access_right_ids": [Command.link(access_right.id)],
                }
            else:
                access_dict[access_right.model_id.id]["group_ids"].append(
                    Command.link(access_right.group_id.id)
                )
                access_dict[access_right.model_id.id]["access_right_ids"].append(
                    Command.link(access_right.id)
                )
        return access_dict
