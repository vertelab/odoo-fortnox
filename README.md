# odoo-fortnox — gren 19.0

> **Denna gren är avsiktligt tom.** Modulerna är INTE portade till Odoo 19.
> Grenen finns så att dev-miljöer (`hansolo19`) kan klona den utan att falla,
> men den påstår ingenting om att koden är portad.

## Baseline

| | |
|---|---|
| Källa | `20.0` |
| Moduler | **47** |
| Grenar i repot | `12.0`, `12.0-SFM-Multicompanyfix`, `12.0-af`, `12.0-test`, `12to14-port`, `13.0`, `14.0`, `14.0-multi-userattestering`, `14.0_before_removed_merged`, `16.0`, `17.0`, `18.0`, `20.0`, `Dev-12.0-Fenix-Sprint-02`, `Dev-12.0-SFM-partner_paid_invoice`, `account_move_attachment`, `fortnox-latest-auth0`, `fortnox-membership-upgrade`, `master`, `master10` |

## Moduler

- `account_admin_rights`
- `account_analytic_default_all_move_lines`
- `account_analytic_line_project`
- `account_analytic_move_ids`
- `account_analytic_name`
- `account_analytic_tag_responsability_project_no`
- `account_analytics_extra_criteria`
- `account_contact_selection`
- `account_customer_filter`
- `account_enablebanking`
- `account_exchange_difference_analytic_tag`
- `account_exchange_difference_draft`
- `account_fortnox`
- `account_inexchange`
- `account_journal_card_type`
- `account_journal_entry_mail_alias`
- `account_journal_select_payable_receivable_account`
- `account_journal_selection`
- `account_journal_upload`
- `account_mis_report_filter`
- `account_move_contact`
- `account_move_disable_create`
- `account_move_line_communication_payment_order`
- `account_move_line_group_by`
- `account_move_red_narration`
- `account_move_report_vat`
- `account_move_tier_validation_control`
- `account_move_tier_validation_implement`
- `account_move_tier_validation_report`
- `account_payment_order_date`
- `account_payment_order_filter`
- `account_payment_order_filter_currency`
- `account_payment_order_regulatory_reporting`
- `account_payment_order_sepa_seb`
- `account_period`
- `account_period_contract`
- `account_period_financial_report`
- `account_reconciliation_override`
- `account_remove_unique_bank_account_constraint`
- `account_remove_unique_bank_number`
- `bank_payment_order_customization`
- `currency_exchange_rate`
- `odoo_invoice_analysis`
- `payment_order_file_name`
- `split_invoice_by_attachments`
- `tier_all_validations_required`
- `tier_validation_reminder`

## Blockerare

**7 externa beroenden saknas** i Odoo 19-kärnan och OCA 19.0:

| Beroende | Behövs av |
|---|---|
| `account_invoice_ubl` | `account_inexchange` |
| `account_move_tier_validation` | `account_analytic_tag_responsability_project_no`, `account_move_tier_validation_implement`, `tier_all_validations_required` |
| `account_payment_partner` | `account_move_disable_create` |
| `account_statement_import` | `account_journal_card_type` |
| `base_tier_validation` | `account_move_tier_validation_implement`, `tier_all_validations_required`, `tier_validation_reminder` |
| `base_tier_validation_report` | `account_move_tier_validation_implement`, `account_move_tier_validation_report` |
| `membership` | `account_fortnox` |

### Prioritering

Ett beroende som blockerar många moduler ger mest nytta att lösa först:

- `account_move_tier_validation` — frisläpper **3** modul(er)
- `base_tier_validation` — frisläpper **3** modul(er)
- `base_tier_validation_report` — frisläpper **2** modul(er)
- `account_invoice_ubl` — frisläpper **1** modul(er)
- `account_payment_partner` — frisläpper **1** modul(er)

## Nästa steg

Portering sker på `*-pfile`-maskin med versionsagnostisk kod
(`.p.py` / `.p.xml`). Se `/skill:odoo-pfiles`.
