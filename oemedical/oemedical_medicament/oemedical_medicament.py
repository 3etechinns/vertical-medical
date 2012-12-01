# -*- coding: utf-8 -*-
#/#############################################################################
#
#    Tech-Receptives Solutions Pvt. Ltd.
#    Copyright (C) 2004-TODAY Tech-Receptives(<http://www.techreceptives.com>)
#    Special Credit and Thanks to Thymbra Latinoamericana S.A.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#/#############################################################################
from osv import osv
from osv import fields


class OeMedicalMedicament(osv.osv):
    _name = 'oemedical.medicament'

    _columns = {
        'name': fields.char(string='Name', size=264),
        'category': fields.many2one('oemedical.medicament.category',
                                    'Category', ),
        'indications': fields.text(string='Indication'),
        'therapeutic_action': fields.char(size=256,
                                          string='Therapeutic effect',
                                          required=True),
        'product': fields.many2one('product.product', string='Product', ),
        'pregnancy_category': fields.selection([
            ('A', 'A'),
            ('B', 'B'),
            ('C', 'C'),
            ('D', 'D'),
            ('X', 'X'),
            ('N', 'N'),
        ], string='Pregnancy Category'),
        'overdosage': fields.text(string='Overdosage'),
        'pregnancy_warning': fields.boolean(string='Pregnancy Warning'),
        'notes': fields.text(string='Extra Info'),
        'storage': fields.text(string='Storage Conditions'),
        'adverse_reaction': fields.text(string='Adverse Reactions'),
        'active_component': fields.char(size=256, string='Active component',
                                        required=True),
        'dosage': fields.text(string='Dosage Instructions'),
        'pregnancy': fields.text(string='Pregnancy and Lactancy'),
        'presentation': fields.text(string='Presentation'),
        'composition': fields.text(string='Composition'),
    }

OeMedicalMedicament()
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
