
class ParapheurController(object):
    """Defines the controller that uses the basic functions exposed by the API"""

    def __init__(self, requester):
        super(ParapheurController, self).__init__()
        self.requester = requester

    def getBureaux(self, username):
        assert username;

        req = {"username": username}

        return self.requester.apiAuthRequest('/parapheur/api/getBureaux', req)

    def getTypologie(self, bureauRef):
        assert bureauRef

        req = {"bureauRef": bureauRef}

        return self.requester.apiAuthRequest('/parapheur/api/getTypologie', req)["data"]["typology"]

    def getDossiersHeaders(self, bureauCourant):
        assert bureauCourant

        req = {"bureauCourant": bureauCourant, "page" : "0", "pageSize" : "10", "parent" : "en-preparation"}

        return self.requester.apiAuthRequest('/parapheur/api/getDossiersHeaders', req)

    #gets the circuit template for emetteur with type/subType
    def getCircuit(self, bureauCourant, _type, sousType):
        req = {"bureauCourant": bureauCourant, "type": _type, "sousType": sousType}

        return self.requester.apiAuthRequest('/parapheur/api/getCircuit', req)
        
    def getMetadonnees(self, _type, sousType):
        req = {"type":_type, "sousType":sousType}
        
        return self.requester.apiAuthRequest("/parapheur/api/getMetadonnees", req)
        
    def getArchives(self):
        req = {"page" : "0", "pageSize" : "10"}
        
        return self.requester.apiAuthRequest("/parapheur/api/getArchives", req)

