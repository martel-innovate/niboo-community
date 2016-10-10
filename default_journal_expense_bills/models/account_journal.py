# -*- coding: utf-8 -*-
# © 2016 Jérôme Guerriat
# © 2016 Niboo SPRL (<https://www.niboo.be/>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from openerp import api, fields, models


class AccountJournal(models.Model):
    _inherit = 'account.journal'

    subtype = fields.Selection([
        ('expense', 'Expenses'),
        ('vendor_bills', 'Vendor Bills'),
        ('other', 'Other'),
    ])


class AccountChartTemplate(models.Model):
    _inherit = 'account.chart.template'
    _description = 'Templates for Account Chart'

    @api.multi
    def _prepare_all_journals(self, acc_template_ref, company,
                              journals_dict=None):
        journal_data = super(AccountChartTemplate, self)._prepare_all_journals(
            acc_template_ref, company, journals_dict)

        for item in journal_data:
            if item['name'] == 'Vendor Bills':
                item['subtype'] = 'vendor_bills'

        return journal_data
