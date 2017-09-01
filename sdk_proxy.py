"""
Contains classes that allows you  to manage ovirt and calamari sdk interfaces

>>> kwargs = {"url":'https://localhost/ovirt-engine/api', "username":"admin@internal", "password":"password", 'ca_file': '/etc/pki/ovirt-engine/ca.pem', 'insecure':'True'}
>>> import proxy
>>> p = proxy.Proxy('ovirt', **kwargs)
>>> p.get_connection()
<ovirtsdk4.Connection object at 0x7f2c99791150>
>>> con = p.get_connection()
>>> con.system_service().vms_service()
<ovirtsdk4.services.VmsService object at 0x7f2c8abb3e10>
>>> vm_service  =con.system_service().vms_service()
>>> vms = vm_service.list()
[<ovirtsdk4.types.Vm object at 0x7f2c8abb3f50>, <ovirtsdk4.types.Vm object at 0x7f2c8abddc10>, <ovirtsdk4.types.Vm object at 0xcf1390>]

>>> vms
[<ovirtsdk4.types.Vm object at 0x7f2c8abb3e50>, <ovirtsdk4.types.Vm object at 0xcf40d0>, <ovirtsdk4.types.Vm object at 0xcf4810>]
"""



#import ovirt python sdk
import ovirtsdk4 as sdk
#imports for calamari will be here

class Proxy:
    def __init__(self, interface, **kwargs):
        self.interface = interface
        self.kwargs = kwargs
        print self.interface

    #TODO: we would like to have only one connection interface available .
    def get_connection(self):
        if self.interface == 'ovirt':
            return self._get_ovirt_connection()
        elif self.interface == 'calamari':
            return self._get_calami_connection()

    def _get_ovirt_connection(self):
        """"""
        connection = sdk.Connection(**self.kwargs)
        return connection

    def _get_calamari_connection(self):
        #TODO : create a connection to calamari once we have the interface to it
        pass


if __name__ == '__main__':
    # TODO : get kwargs from yaml/config file
    kwargs = {"url":'https://localhost/ovirt-engine/api', "username":"admin@internal", "password":"password", 'ca_file': '/etc/pki/ovirt-engine/ca.pem', 'insecure':'True'}
    p = proxy.Proxy('ovirt', **kwargs)
    con = p.get_connection()
    vm_service  =con.system_service().vms_service()
    vms = vm_service.list()
