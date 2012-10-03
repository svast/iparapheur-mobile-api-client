from core.AnnotationController import AnnotationController
from core.DossierController import DossierController
from core.ParapheurController import ParapheurController
from core.Requester import Requester


# Scenario "Documentation"
requester = Requester("http://dev-parapheur.local/alfresco/s")
requester.logging = True
requester.login("eperalta", "secret")

#Services Definitions
annotationController = AnnotationController(requester)
dossierController = DossierController(requester)
parapheurController = ParapheurController(requester)



bureaux = parapheurController.getBureaux("eperalta")

bureauCourant = bureaux['data']['bureaux'][0]['nodeRef']

typologie = parapheurController.getTypologie(bureauCourant)

dossier = dossierController.beginCreateDossier(bureauCourant)
dossierController.setCircuit(dossier, typologie.keys()[0], typologie[typologie.keys()[0]][0])

docPrincipal = dossierController.addDocumentPrincipal(dossier, "fixtures/main.pdf")
annexe = dossierController.addAnnexe(dossier, "fixtures/annexe.pdf")

properties = {
    "cm:name": "Test EPA Mobile API"
}

dossierController.setDossierProperties(dossier, properties)
#dossierController.finalizeCreateDossier(dossier)

