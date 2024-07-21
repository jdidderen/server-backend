# Copyright 2024 Jérémy Didderen
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class SecurityOverviewWizard(models.TransientModel):
    _name = "security.overview.wizard"
    _description = (
        "Wizard to have an overview of the security rights for an user or a group"
    )

    access_right_ids = fields.Many2many(comodel_name="ir.model.access")
    module_ids = fields.Many2many(
        comodel_name="ir.module.module",
        compute="_compute_module_ids",
        store=True,
        string="Modules",
    )
    model_id = fields.Many2one(comodel_name="ir.model")
    model_name = fields.Char(
        related="model_id.name", store=True, translate=True, string="Model"
    )
    model = fields.Char(related="model_id.model", store=True)
    info = fields.Text(related="model_id.info", store=True)
    can_read = fields.Boolean(compute="_compute_rights", store=True)
    can_create = fields.Boolean(compute="_compute_rights", store=True)
    can_write = fields.Boolean(compute="_compute_rights", store=True)
    can_unlink = fields.Boolean(compute="_compute_rights", store=True)
    group_ids = fields.Many2many(comodel_name="res.groups")

    @api.depends("access_right_ids")
    def _compute_module_ids(self):
        for wizard in self:
            wizard.module_ids = wizard.access_right_ids.mapped("ir_module_ids")

    @api.depends("access_right_ids")
    def _compute_rights(self):
        for wizard in self:
            wizard.can_read = any(wizard.access_right_ids.mapped("perm_read"))
            wizard.can_create = any(wizard.access_right_ids.mapped("perm_create"))
            wizard.can_write = any(wizard.access_right_ids.mapped("perm_write"))
            wizard.can_unlink = any(wizard.access_right_ids.mapped("perm_unlink"))
