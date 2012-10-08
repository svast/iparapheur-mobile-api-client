import base64
import os

class DossierController(object):
    def __init__(self, requester):
        self.requester = requester

    def beginCreateDossier(self, bureau):
        req = {"bureauRef": bureau}
        return self.requester.apiAuthRequest("/parapheur/api/createDossier", req)["dossierRef"]

    def setDossierProperties(self, dossier, properties):
        req = {"dossierRef": dossier,
               "properties": properties}

        return self.requester.apiAuthRequest("/parapheur/api/setDossierProperties", req)

    def addDocumentPrincipal(self, dossier, fileName):
        f = open(fileName)
        content = f.read()
        b64Content = base64.standard_b64encode(content);

        head, tail = os.path.split(fileName)

        req = {"dossierRef": dossier,
               "name": tail,
               "content": b64Content,
               "mainFile": "true"}

        return self.requester.apiAuthRequest("/parapheur/api/addDocument", req)

    def addAnnexe(self, dossier, fileName):
        f = open(fileName)
        content = f.read()
        b64Content = base64.standard_b64encode(content);

        head, tail = os.path.split(fileName)

        req = {"dossierRef": dossier,
               "name": tail,
               "content": b64Content,
               "mainFile": "false"}

        return self.requester.apiAuthRequest("/parapheur/api/addDocument", req, '_annexe')

    def setCircuit(self, dossier, _type, sousType):
        req = {"dossierRef": dossier,
               "type": _type,
               "sousType": sousType}

        return self.requester.apiAuthRequest("/parapheur/api/setCircuit", req)

    def finalizeCreateDossier(self, dossier):
        req = {"nodeRef": dossier}

        return self.requester.apiAuthRequest("/parapheur/api/finalizeCreateDossier", req)

    def deleteNode(self, dossier):
        req = {"nodeRef": dossier}

        return self.requester.apiAuthRequest("/parapheur/api/deleteNode", req)