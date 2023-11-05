from odoo import api, fields, models
from odoo.exceptions import ValidationError
from datetime import date, datetime


class Hospitalpatient(models.Model):
    _name = "hospital_patient"
    _inherit = ['portal.mixin', 'mail.thread', 'mail.activity.mixin', 'utm.mixin']
    _description = "Info Hospital"

    def action_draft(self):
        for rec in self:
            rec.state = 'draft'

    def action_done(self):
        for rec in self:
            rec.state = 'done'

    def action_cancel(self):
        for rec in self:
            rec.state = 'cancel'

    name = fields.Char(string='Name')
    age = fields.Integer(string="Age")
    birthday = fields.Date()
    gender = fields.Selection(
        [('male', 'Male'), ('famle', 'Female')]
    )
    state = fields.Selection(
        [('draft', 'Draft'), ('done', 'Done'), ('cancel', 'Cancel')],
        default='draft'
    )

    @api.constrains('name')
    def _check_date_end(self):
        for record in self:
            patient = self.env['hospital_patient'].search([('name', '=', record.name), ('id', '!=', record.id)])
            if patient:
                raise ValidationError(("Name %s Already Exist" % record.name))

    @api.constrains('age')
    def _check_date_end2(self):
        for record in self:
            if record.age == 0:
                raise ValidationError(" Age cannot be zero ")
            elif record.age > 80:
                raise ValidationError(" Age cannot greater than 80 ")
            elif record.age < 10:
                raise ValidationError(" Age cannot Less than 10 ")

        # newfield = fields.One2many('doctor_doctor', 'newfield2', String='Doc')

    def newtest2332(self):
        for rec in self:
            rec.creatby = self.env.user

    def actions_act_material(self):
        newfield = self.mapped('newfield')
        domain = [('id', 'in', newfield.ids)]
        context = {
            'default_newfield2': self.id
        }
        return {
            'type': 'ir.actions.act_window',
            'name': 'settting',
            'view_mode': 'tree',
            'res_model': 'doctor_doctor',
            'domain': domain,
            'context': context
        }


class Hospitaldoctor(models.Model):
    _name = "doctor_doctor"
    _inherit = ['portal.mixin', 'mail.thread', 'mail.activity.mixin', 'utm.mixin']
    _description = "Infoooo Hospital"

    def action_draft(self):
        for rec in self:
            rec.state = 'draft'

    def action_done(self):
        for rec in self:
            rec.state = 'done'

    def action_cancel(self):
        for rec in self:
            rec.state = 'cancel'

    name = fields.Char(string='Name')
    age = fields.Integer(string="Age")
    date2 = fields.Date(string="Age2")
    gender = fields.Selection(
        [('male', 'Male'), ('famle', 'Female')]
    )
    state = fields.Selection(
        [('draft', 'Draft'), ('done', 'Done'), ('cancel', 'Cancel')],
        default='draft'
    )
    newfield2 = fields.Many2one('hospital_patient', string='Many2one')

    def default_get(self, fields):
        res = super(Hospitaldoctor, self).default_get(fields)
        res['age'] = 55
        res['name'] = 'momo'
        return res

    # @api.model
    # def _name_search(self, name='', args=None, operator='ilike', limit=100):
    #     if args is None:
    #         args = []
    #     domain = args + ['|', ('age', operator, name), ('gender', operator, name)]
    #     return super(Hospitaldoctor,self).search(domain,limit=limit).name_get


    def write(self,vals):
        print(vals)
        vals['name'] = self.env.user.name
        return super(Hospitaldoctor,self).write(vals)








    
