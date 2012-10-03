import urllib2
from urllib2 import HTTPError
import pprint
import json
import os, re

pp = pprint.PrettyPrinter(indent=2)


class Requester(object):
    def __init__(self, endPoint):
        super(Requester, self).__init__()
        self.endPoint = endPoint
        self.logging = False


    def _apiRequest(self, uri, apipath, args):
        content = json.dumps(args)

        req = urllib2.Request(uri + apipath,
            headers={
                "Content-Type": "application/json",
                "Accept": "*/*",
                "User-Agent": "ph-ws-py/1",
                },
            data=content)
        try:
            r = urllib2.urlopen(req)
        except HTTPError as err:
            print uri + apipath
            print err
        else:
            response = r.read()
            jsonData = json.loads(response)

            pp.pprint(jsonData)
            return  jsonData


    def apiRequest(self, uri, apipath, args, suffix=""):
        fname = ""
        if self.logging:
            fname = os.path.split(apipath)[1]
            m = re.match("^([A-Za-z]+)", fname)
            if m:
                fname = m.group(0) + suffix

            fd = os.open("/tmp/" + fname + "_in.js", os.O_WRONLY | os.O_CREAT)

            os.write(fd, json.dumps(args, indent=4))
            os.fsync(fd)
            os.close(fd)

        retval = self._apiRequest(uri, apipath, args)

        if self.logging:
            fd = os.open("/tmp/" + fname + "_out.js", os.O_WRONLY | os.O_CREAT)

            os.write(fd, json.dumps(retval, indent=4))
            os.fsync(fd)
            os.close(fd)

        return retval


    def apiAuthRequest(self, apipath, args, suffix=""):
        assert self.ticket
        return self.apiRequest(self.endPoint, apipath + "?alf_ticket=" + self.ticket, args, suffix)


    def login(self, username, password):
        ret = self.apiRequest(self.endPoint, '/parapheur/api/login', {'username': username, 'password': password})

        if ret:
            self.ticket = ret["data"]["ticket"]

        return self.ticket


    def logout(self, ticket):
        req = {"ticket": ticket}

        return self.apiAuthRequest(self.endPoint, '/parapheur/api/logout', req)


