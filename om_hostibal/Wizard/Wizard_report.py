from odoo import api, fields, models


class description(models.TransientModel):
    _name = "test.model.wizard"
    _description = 'Test Model Wizard'

    show = fields.Boolean(default='True')
    state = fields.Selection(
        [('draft', 'Draft'), ('done', 'Done'), ('cancel', 'Cancel')],
        String='state'
    )

    def print_qww(self):
        [data] = self.read()
        dates = {
            'ids': [],
            'model': 'hospital_patient',
            'form': data
        }
        return self.env.ref('om_hostibal.zero2one_report').report_action([], data=dates)
