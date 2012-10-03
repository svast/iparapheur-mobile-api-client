import urllib2
from urllib2 import HTTPError

import json
import pprint
import os, re
import threading

pp = pprint.PrettyPrinter(indent=2)


class ParapheurController(object):
    """Defines the controller that uses the basic functions exposed by the API"""

    #def uniqueFilename(self, filename, index):
    #	if (not os.path.isfile()):

    def _apiRequest(self, uri, apipath, args):
        content = json.dumps(args);

        req = urllib2.Request(uri+apipath,
            headers = {
                "Content-Type": "application/json",
                "Accept": "*/*",
                "User-Agent": "ph-ws-py/1",
                },
            data = content)
        try:
            r = urllib2.urlopen(req)
        except HTTPError as err:
            print uri+apipath
            print err
        else:
            response = r.read()
            jsonData = json.loads(response)

            pp.pprint(jsonData)

            return  jsonData

    def apiRequest(self, uri, apipath, args, suffix = ""):
        if (self.logging):
            fname = os.path.split(apipath)[1]
            m = re.match("^([A-Za-z]+)", fname)
            if (m):
                fname = m.group(0) + suffix

            fd = os.open("/tmp/"+fname+"_in.js", os.O_WRONLY| os.O_CREAT);

            os.write(fd , json.dumps(args, indent=4));
            os.fsync(fd)
            os.close(fd)

        retval = self._apiRequest(uri, apipath, args)

        if (self.logging):
            fd = os.open("/tmp/"+fname+"_out.js", os.O_WRONLY | os.O_CREAT);

            os.write(fd , json.dumps(retval, indent=4));
            os.fsync(fd)
            os.close(fd)

        return retval

    def apiAuthRequest(self, uri, apipath, args, suffix = ""):
        assert(self.ticket)
        return  self.apiRequest(uri, apipath+"?alf_ticket="+self.ticket, args, suffix)


    def __init__(self, endPoint):
        super(ParapheurController, self).__init__()
        self.endPoint = endPoint
        self.ticket = None
        self.logging = False

    def isLoggued(self):
        return self.ticket != None

    def login(self, username, password):
        ret = self.apiRequest(self.endPoint, '/parapheur/api/login', {'username': username, 'password': password})
        if (ret):
            self.ticket = ret["data"]["ticket"]

        return self.ticket

    def logout(self, ticket):
        req = {"ticket": ticket};

        return self.apiAuthRequest(self.endPoint, '/parapheur/api/logout', req, self.ticket)


    def getBureaux(self, username):
        assert(self.ticket);
        assert(username);

        req = {"username": username};

        return self.apiAuthRequest(self.endPoint, '/parapheur/api/getBureaux', req, self.ticket)

    def getTypologie(self, bureauRef):
        assert(bureauRef)

        req = {"bureauRef": bureauRef}

        return self.apiAuthRequest(self.endPoint, '/parapheur/api/getTypologie', req, self.ticket)

    def getDossier(self, dossierRef):
        assert(dossierRef)

        req = {"dossierRef": dossierRef}

        return self.apiAuthRequest(self.endPoint, '/parapheur/api/getDossier', req, self.ticket)

    # gets the circuit instance for dossier
    def getCircuit(self, dossieRef):
        assert(dossierRef)

        req = {"dossierRef": dossierRef}

        return self.apiAuthRequest(self.endPoint, '/parapheur/api/getCircuit', req, self.ticket)

    #gets the circuit template for emetteur with type/subType
    def getCircuit(self, emetteurRef, _type, sousType):
        req = {"emetteurRef": emetteurRef, "type": _type, "sousType": sousType}

        return self.apiAuthRequest(self.endPoint , '/parapheur/api/getCircuit', req, self.ticket)

