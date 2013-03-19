import urllib2
import re

magic_url = "http://169.254.169.254/"

def apis():
    f = urllib2.urlopen(magic_url)
    output=f.read()
    f.close()
    return output.split("\n")

class InstanceData(object):
    def __init__(self, api="latest"):
        self.api=api

    def availability_zone(self):
        f = urllib2.urlopen(magic_url + self.api + "/meta-data/placement/availability-zone")
        output=f.read()
        f.close()
        return output

    def region(self):
        return re.sub("""[A-Za-z]*$""","",self.availability_zone())

    def instance_id(self):
        f = urllib2.urlopen(magic_url + self.api + "/meta-data/instance-id")
        output=f.read()
        f.close()
        return output


