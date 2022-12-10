
__version__ = '0.0.1'

from erpnext.portal import utils
from sweat_zone.events.utils import custom_create_customer_or_supplier

utils.create_customer_or_supplier = custom_create_customer_or_supplier