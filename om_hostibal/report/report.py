from odoo import models


class PartnerXlsx(models.AbstractModel):
    _name = 'report.om_hostibal.report_product.xlsx'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, liens):
        print("liens", liens, data)
        format1 = workbook.add_format({'font_size': 14, 'align': 'vcenter', 'bold': True})
        format2 = workbook.add_format({'font_size': 14, 'align': 'vcenter', })
        sheet = workbook.add_worksheet('XLSX FILE')
        sheet.write(2, 2, 'Name', format1)
        sheet.write(2, 3, liens.name, format2)
        sheet.write(3, 2, 'Age', format1)
        sheet.write(3, 3, liens.age, format2)
        sheet.write(4, 2, 'birthday', format1)
        sheet.write(4, 3, liens.birthday, format2)
        sheet.write(5, 2, 'gender', format1)
        sheet.write(5, 3, liens.gender, format2)
