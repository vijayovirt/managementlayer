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
