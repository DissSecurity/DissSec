# Date: 9/8/2019
# Author: Diss.Security
# Description: Proxy


class Proxy(object):

    def __init__(self, proxy):
        self.proxy = proxy

    @property
    def ip(self):
        return self.proxy['ip']

    @property
    def port(self):
        return self.proxy['port']

    @property
    def country(self):
        return self.proxy['country']

    @property
    def addr(self):
        addr = '{}:{}'.format(self.proxy['ip'], self.proxy['port'])
        return {'http': addr, 'https': addr}
