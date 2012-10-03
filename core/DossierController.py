
class DossierController(object):
    def __init__(self, requester):
        self.requester = requester

    def beginCreateDossier(self, bureau):
        req = {"bureauRef": bureau}
        return self.requester.apiAuthRequest("/parapheur/api/beginCreateDossier", req)

    def setDossierProperties(self, dossier, properties):
        return None

    def addDocument(self, dossier, fileName):
        return None

    def finalizeCreateDossier(self, dossier):
        return None