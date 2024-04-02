# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.
{
    'name': "Activities Management Basic | All In One Schedule Activities | Activity Dashboard | Advance Schedule Activity | Dynamic Action For Multiple Activities | Activity Management Dashboard | Activities Dashboard",
    'author': 'Softhealer Technologies',
    'website': 'https://www.softhealer.com',
    "support": "support@softhealer.com",
    'category': 'Discuss',
    'version': '16.0.5',
    "summary": "Activity Scheduler Employee Activity Supervisor Activity filter Activity Multi Activity Schedule Mass Activity Tag activity history Activity monitoring Activity multi users assign schedule activity schedule activities Multi Company Activity Mail Odoo Activity Management Activity Dashboard Activity Monitoring Activity Views User Activity Log, User Activity Audit,  Session Management, Record Log, Activity Traces, Login Notification, User Activity Record, Record History, Login History, Login location, Login IP Advance Schedule Activity multi users assign schedule activity to multi users Schedule Activity Dashboard for schedule activity history of schedule activity reports for schedule activity menu and view for schedule activities for Multi Company Activity odoo",
    "description": """Do you want to show the well-organized structure of activities? Do you want to show completed, uncompleted activities easily to your employees? Do you want to show an activity dashboard to the employee? Do you want to show the scheduled activity to the manager, supervisor & employee? This module helps the manager can see everyone's activity, the supervisor can see the assigned user and their own activity, the user can see only their own activity. You can see activities like all activities, planned activities, completed activities, or overdue activities. Manager, Supervisor & Employee have their own dashboard. Activity notification will help to send a notification before and after the activity due date. You can notify your salesperson/customer before or after the activity is done. Hurray!""",
    'depends': [
        'mail',
    ],
    'data': [
        'security/activity_security.xml',
        'security/ir.model.access.csv',
        'views/sh_menu.xml',
        'views/activity_config_setting.xml',
        'wizard/sh_feedback.xml',
        'wizard/sh_mark_as_done.xml',
        'views/sh_activity_views.xml',
        'views/sh_activity_dashboard.xml',
        'views/res_users.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'sh_activities_management_basic/static/src/scss/crm_dashboard.scss',
            'sh_activities_management_basic/static/src/js/activity_dashboard.js',
            'sh_activities_management_basic/static/src/xml/**/*',
        ],
    },
    'images': ['static/description/background.png', ],
    'uninstall_hook': 'uninstall_hook',
    "installable": True,
    "auto_install": False,
    "application": True,
    "license": "OPL-1",
    "price": 50,
    "currency": "EUR"
}
