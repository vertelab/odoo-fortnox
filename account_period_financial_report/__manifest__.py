{
    'name': "Account Period Financial Report",
    'version': '18.0',
    'license': 'AGPL-3',
    'depends': ['account_period', 'account_financial_report'],
    'author': "Vertel AB",
    "website": "https://vertel.se/apps/odoo-fortnox/account_period_financial_report",
    'category': 'Accounting',
    'description': """
    Glue module between account_period and account_financial_report. 
    This module will make it so that account_period fiscal years are used instead of the core one.
    """,
    'auto_install': True,    
}
