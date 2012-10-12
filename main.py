from core.AnnotationController import AnnotationController, Annotation, Point, Rect
from core.DossierController import DossierController
from core.ParapheurController import ParapheurController
from core.Requester import Requester


# Scenario "Documentation"
requester = Requester("http://parapheur-dev.local:8080/alfresco/s")
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

dossierController.setCircuit(dossier, bureauCourant, typologie.keys()[0], typologie[typologie.keys()[0]][0])

docDelete = dossierController.addDocument(dossier, "fixtures/minimal.pdf", bureauCourant)
docPrincipal = dossierController.addDocumentVisu(dossier, "fixtures/min.xml", "fixtures/minimal.pdf", bureauCourant)

dossierController.removeDocument(docDelete, bureauCourant)

properties = {
    "cm:name": "Test EPA Mobile API"
}

dossierController.setDossierProperties(dossier, bureauCourant, properties)
dossierController.finalizeCreateDossier(dossier, bureauCourant)


annotation = Annotation()

annotation.page = 0
annotation.rect = Rect(Point(0,0), Point(100, 100))
annotation.text = "coucou"
annotation.type = "text"

annotationController.addAnnotation(dossier, annotation)
annotationController.getAnnotations(dossier)

data = dossierController.getDossier(dossier, bureauCourant)

dossierController.deleteNodes(dossier)

#annotationController.updateAnnotation(dossier, annotation)

