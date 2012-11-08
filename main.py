from core.AnnotationController import AnnotationController, Annotation, Point, Rect
from core.DossierController import DossierController
from core.ParapheurController import ParapheurController
from core.Requester import Requester
import time

# Scenario "Documentation"
requester = Requester("http://parapheur-dev.local:8080/alfresco/s")
requester.logging = True
requester.login("eperalta", "secret")

#Services Definitions
annotationController = AnnotationController(requester)
dossierController = DossierController(requester)
parapheurController = ParapheurController(requester)



bureaux = parapheurController.getBureaux("eperalta")

bureauCourant = bureaux['bureaux'][0]['nodeRef']
bureauDGS = bureaux['bureaux'][1]['nodeRef']

typologie = parapheurController.getTypologie(bureauCourant)

dossier = dossierController.beginCreateDossier(bureauCourant)

dossierController.setCircuit(dossier, bureauCourant, typologie.keys()[1], typologie[typologie.keys()[1]][0])

docDelete = dossierController.addDocument(dossier, "fixtures/minimal.pdf", bureauCourant)
docPrincipal = dossierController.addDocumentVisu(dossier, "fixtures/min.xml", "fixtures/minimal.pdf", bureauCourant)

dossierController.removeDocument(docDelete, dossier, bureauCourant)

properties = {
    "cm:name": "Test EPA Mobile API"
}

parapheurController.getCircuit(bureauCourant, typologie.keys()[1], typologie[typologie.keys()[1]][0])

dossierController.setDossierProperties(dossier, bureauCourant, properties)
dossierController.finalizeCreateDossier(dossier, bureauCourant)


annotation = Annotation()

annotation.page = 0
annotation.rect = Rect(Point(0,0), Point(100, 100))
annotation.text = "coucou"
annotation.type = "text"

annotation.uuid = annotationController.addAnnotation(dossier, annotation)['uuids'][0]
annotationController.getAnnotations(dossier)

annotation.text = "test"


data = dossierController.getDossier(dossier, bureauCourant)

parapheurController.getDossiersHeaders(bureauCourant)

parapheurController.getArchives()

dossierController.getImages(dossier)

parapheurController.getMetadonnees(typologie.keys()[2], typologie[typologie.keys()[2]][0])

dossierController.visa(dossier, "Annotation publique", "Annotation publique", bureauCourant)

time.sleep(1)

dossierController.remorse(dossier, bureauCourant)

time.sleep(1)

dossierController.visa(dossier, "Annotation publique", "Annotation publique", bureauCourant)

time.sleep(1)

dossierController.reject(dossier, "Annotation publique", "Annotation publique", bureauDGS)

time.sleep(2)

dossierController.raz(dossier, bureauCourant)

time.sleep(1)

dossierController.deleteNodes(dossier)

