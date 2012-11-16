import base64
import os

class DossierController(object):
    def __init__(self, requester):
        self.requester = requester

    def beginCreateDossier(self, bureau):
        req = {"bureauCourant": bureau}
        return self.requester.apiAuthRequest("/parapheur/api/createDossier", req)["dossierRef"]

    def setDossierProperties(self, dossier, bureau, properties):
        req = {"dossier": dossier,
               "bureauCourant": bureau,
               "properties": properties}

        return self.requester.apiAuthRequest("/parapheur/api/setDossierProperties", req)

    def addDocumentVisu(self, dossier, fileName, visuName, bureau):
        f = open(fileName)
        ff = open(visuName)
        content = f.read()
        ccontent = ff.read()
        b64Content = base64.standard_b64encode(content);
        bb64Content = base64.standard_b64encode(ccontent);

        head, tail = os.path.split(fileName)
        head, taill = os.path.split(visuName)

        req = {"dossier": dossier,
               "bureauCourant" : bureau,
               "name": tail,
               "content": b64Content,
               "visualname": taill,
               "visualcontent": bb64Content}

        return self.requester.apiAuthRequest("/parapheur/api/addDocument", req, "_visuel") ["success"]
        
    def addDocument(self, dossier, fileName, bureau):
        f = open(fileName)
        content = f.read()
        b64Content = base64.standard_b64encode(content);

        head, tail = os.path.split(fileName)

        req = {"dossier": dossier,
               "bureauCourant" : bureau,
               "name": tail,
               "content": b64Content,
               "visualname": "",
               "visualcontent": ""}

        return self.requester.apiAuthRequest("/parapheur/api/addDocument", req) ["success"]

    def removeDocument(self, document, dossier, bureauCourant):
        req = {"document": document,
               "dossier": dossier,
               "bureauCourant": bureauCourant}
               
        return self.requester.apiAuthRequest("/parapheur/api/removeDocument", req)

    def setCircuit(self, dossier, bureau, _type, sousType):
        req = {"dossier": dossier,
			   "bureauCourant": bureau,
               "type": _type,
               "sousType": sousType}

        return self.requester.apiAuthRequest("/parapheur/api/setCircuit", req)

    def finalizeCreateDossier(self, dossier, bureau):
        req = {"dossier": dossier,
               "bureauCourant": bureau}

        return self.requester.apiAuthRequest("/parapheur/api/finalizeCreateDossier", req)

    def deleteNodes(self, dossier):
        req = {"nodes": [dossier]}

        return self.requester.apiAuthRequest("/parapheur/api/deleteNodes", req)

    def getDossier(self, dossier, bureau):

        req = {"dossier": dossier,
               "bureauCourant": bureau}

        return self.requester.apiAuthRequest("/parapheur/api/getDossier", req)
        
    def getImages(self, dossier):
        req = {"dossier":dossier}
        
        return self.requester.apiAuthRequest("/parapheur/api/getImages", req)
        
    def raz(self, dossiers, bureauCourant):
        req = {"dossiers":[dossiers],
               "bureauCourant":bureauCourant}
        
        return self.requester.apiAuthRequest("/parapheur/api/razDossier", req)
        
    def reject(self, dossiers, annotPub, annotPriv, bureauCourant):
        req = {"dossiers":[dossiers],
               "annotPub":annotPub,
               "annotPriv":annotPriv,
               "bureauCourant":bureauCourant}
        
        return self.requester.apiAuthRequest("/parapheur/api/reject", req)
        
    def remorse(self, dossiers, bureauCourant):
        req = {"dossiers":[dossiers],
               "bureauCourant":bureauCourant}
        
        return self.requester.apiAuthRequest("/parapheur/api/remorseDossier", req)
        
    def visa(self, dossiers, annotPub, annotPriv, bureauCourant):
        req = {"dossiers":[dossiers],
               "annotPub":annotPub,
               "annotPriv":annotPriv,
               "bureauCourant":bureauCourant}
        
        return self.requester.apiAuthRequest("/parapheur/api/visa", req)
        
    def archive(self, dossiers, bureauCourant):
        req = {"dossiers":[dossiers],
               "bureauCourant":bureauCourant}
        
        return self.requester.apiAuthRequest("/parapheur/api/archive", req)
        
    def getSignInfo(self, dossiers):
        req = {"dossiers":[dossiers]}
        
        return self.requester.apiAuthRequest("/parapheur/api/getSignInfo", req)
        
    def signature(self, dossiers, signatures, annotPub, annotPriv, bureauCourant):
        req = {"dossiers":[dossiers],
               "signatures":[signatures],
               "annotPub":annotPub,
               "annotPriv":annotPriv,
               "bureauCourant":bureauCourant} 
               
        return self.requester.apiAuthRequest("/parapheur/api/signature", req)
