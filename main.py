from core.AnnotationController import AnnotationController
from core.DossierController import DossierController
from core.ParapheurController import ParapheurController
from core.Requester import Requester


# Scenario "Documentation"
requester = Requester("http://dev-parapheur.local/alfresco/s")
requester.logging = True
requester.login("eperalta", "secret")

annotationController = AnnotationController(requester)
dossierController = DossierController(requester)
parapheurController = ParapheurController(requester)

bureaux = parapheurController.getBureaux("eperalta")

typologie = parapheurController.getTypologie(bureaux['data']['bureaux'][0]['nodeRef'])

