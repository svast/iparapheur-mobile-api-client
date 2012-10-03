import urllib2
from urllib2 import HTTPError

import json
import pprint
import os, re
import threading



class ParapheurController(object):
    """Defines the controller that uses the basic functions exposed by the API"""

    def __init__(self, requester):
        super(ParapheurController, self).__init__()
        self.requester = requester

    def getBureaux(self, username):
        assert(username);

        req = {"username": username};

        return self.requester.apiAuthRequest('/parapheur/api/getBureaux', req)

    def getTypologie(self, bureauRef):
        assert(bureauRef)

        req = {"bureauRef": bureauRef}

        return self.requester.apiAuthRequest('/parapheur/api/getTypologie', req)

    def getDossier(self, dossierRef):
        assert(dossierRef)

        req = {"dossierRef": dossierRef}

        return self.requester.apiAuthRequest('/parapheur/api/getDossier', req)

    # gets the circuit instance for dossier
    def getCircuit(self, dossieRef):
        assert(dossierRef)

        req = {"dossierRef": dossierRef}

        return self.requester.apiAuthRequest('/parapheur/api/getCircuit', req)

    #gets the circuit template for emetteur with type/subType
    def getCircuit(self, emetteurRef, _type, sousType):
        req = {"emetteurRef": emetteurRef, "type": _type, "sousType": sousType}

        return self.requester.apiAuthRequest('/parapheur/api/getCircuit', req)

