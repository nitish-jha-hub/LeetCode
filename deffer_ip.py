class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        add1 = address.split('.')
        defIp = '[.]'.join(add1)
        return (defIp)