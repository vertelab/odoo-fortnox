{
    'name': "Account Period Financial Report",
    'summary': "Adds a financial report wizard for accounting periods.",
    'version': '18.0.1.0.0',
    'license': 'AGPL-3',
    'depends': ['account_period', 'account_financial_report'],
    'author': "Vertel AB",
    "website": "https://vertel.se/apps/odoo-fortnox/account_period_financial_report",
    'category': 'Accounting',
    'description': '''
Account Period Financial Report
===============================

    Glue module between account_period and account_financial_report. 
        This module will make it so that account_period fiscal years are used instead of the core one.

    Features:

        - Guided Wizards: Step-by-step dialogs for data entry.
    ''',
    'auto_install': True,    
}
