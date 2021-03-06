import time
from dateutil.relativedelta import relativedelta
from datetime import datetime, timedelta
import openerp
from openerp import pooler, tools
from openerp.osv import osv, fields
from openerp.tools.translate import _
from connect_partner import test_connect
import fcntl
import sys

class openmrs_connection(osv.osv):

    def create(self, cr, uid, vals, context={}):
        recIds = self.search(cr, uid, [], offset=0, limit=None, order=None, context=None, count=False)
        #raise osv.except_osv(_('Error:'),_('Cannot create more than one connection res = %s' % res))
        if len(recIds) >= 1:
            raise osv.except_osv(_('Error:'),_('Cannot create more than one connection'))
        else:
            res = super(openmrs_connection, self).create(cr, uid, vals)
            return res

    def test_sync(self, cr, uid, context={}, *args):
        recId = self.search(cr, uid, [], offset=0, limit=1, order=None, context=None, count=False)[0]
        openmrs_object = self.pool.get('openmrs.connect')
        username = openmrs_object.browse(cr, uid, recId, context={}).username
        ip_address = openmrs_object.browse(cr, uid, recId, context={}).ip_address
        port = openmrs_object.browse(cr, uid, recId, context={}).port
        password = openmrs_object.browse(cr, uid, recId, context={}).password
        database = openmrs_object.browse(cr, uid, recId, context={}).database
        try:
            test_connect(ip_address, port, username, password, database)
            message = 'accepted'
        except:
            message = 'failed'

        raise osv.except_osv(_('Connection Status:'),_('Connection %s' % message))

    def synchronize(self, cr, uid, *args):
        syncIds = self.pool.get('res.partner').search(cr, uid, [('for_synchronization', '=', True)], offset=0, limit=None, order=None, context=None, count=False)
        self.pool.get('res.partner').write(cr, uid, syncIds, {}, context={})
        raise osv.except_osv(_('Synchronization:'),_('Complete'))

  
  
    _name = "openmrs.connect"
    _columns = {
        'ip_address' : fields.char ('ip_address', size=50, help='IP address of your OpenMRS mysql server' ),
        'port' : fields.char ('port', size=50, help='port of your OpenMRS mysql server'),
        'username' : fields.char ('username', size=50, help='Username of your OpenMRS mysql server'),
        'password' :fields.char ('password', size=50, help='Password of your OpenMRS mysql server'),
        'database' :fields.char ('database', size=50, help='Database of OpenMRS in your mysql server'),
        'identifier_type' : fields.integer('identifier_type', help='ID of the identifier type \n Ex. 2 for Old OpenMRS Identifier'),
    }

openmrs_connection()

