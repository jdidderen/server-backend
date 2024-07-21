# Copyright 2024 Jérémy Didderen
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Security Overview",
    "summary": "Security Overview",
    "version": "17.0.1.0.0",
    "category": "Tools",
    "author": "Jérémy Didderen," "Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/server-backend",
    "license": "AGPL-3",
    "depends": ["base"],
    "installable": True,
    "data": [
        "security/ir.model.access.csv",
        "views/res_groups_views.xml",
        "views/res_users_views.xml",
        "wizard/security_overview_wizard_views.xml",
    ],
}
