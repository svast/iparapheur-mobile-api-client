__author__ = 'manz'

from core.ParapheurController import ParapheurController

parapheurController = ParapheurController("http://dev-parapheur.local/alfresco/s")

parapheurController.logging = True

parapheurController.login("eperalta", "secret")

bureaux = parapheurController.getBureaux("eperalta")

typologie = parapheurController.getTypologie(bureaux['data']['bureaux'][0]['nodeRef'])

