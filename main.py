from core.AnnotationController import AnnotationController, Annotation, Point, Rect
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

docPrincipal = dossierController.addDocumentPrincipal(dossier, "fixtures/minimal.pdf")
#annexe = dossierController.addAnnexe(dossier, "fixtures/annexe.pdf")

properties = {
    "cm:name": "Test EPA Mobile API"
}

dossierController.setDossierProperties(dossier, properties)
#dossierController.finalizeCreateDossier(dossier)


annotation = Annotation()

annotation.page = 0
annotation.rect = Rect(Point(0,0), Point(100, 100))
annotation.text = "coucou"
annotation.type = "text"

annotationController.addAnnotation(dossier, annotation)
annotationController.getAnnotations(dossier)

#dossierController.deleteNode(dossier)

#annotationController.updateAnnotation(dossier, annotation)

