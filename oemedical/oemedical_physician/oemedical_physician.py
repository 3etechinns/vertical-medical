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


class OeMedicalPhysician(osv.osv):
    _name = 'oemedical.physician'

    _columns = {
        'info': fields.text(string='Extra info'),
        'rec_name': fields.char(size=256, string='Name', required=True),
        'code': fields.char(size=256, string='ID', required=True),
        'name': fields.many2one('res.partner', string='Health Professional', ),
        'specialty': fields.many2one('oemedical.specialty', string='Specialty', ),
        'institution': fields.many2one('res.partner', string='Institution', ),
    }

OeMedicalPhysician()
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
