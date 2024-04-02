# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.

from . import wizard
from . import models
from odoo import api, fields, SUPERUSER_ID, _


def uninstall_hook(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    sh_activity_rule = env.ref(
        'mail.mail_activity_rule_user', raise_if_not_found=False).write({'domain_force': "['|',('user_id', '=', user.id), ('create_uid', '=', user.id)]"})
