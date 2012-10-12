
class Point(object):
    """ defines a simple Point Class """
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Rect(object):
    """ defines a simple Rect class """
    def __init__(self, topLeft, bottomRight):
        self.topLeft = topLeft
        self.bottomRight = bottomRight

class Annotation(object):
    """ defines the annotation class
    """

    def __init__(self):
        self.uuid = None
        self.type = "text"
        self.page = 0
        self.text = None
        self.rect = None

class AnnotationController(object):
    """ handles annotations related requests
    """
    def __init__(self, requester):
        self.requester = requester

    def addAnnotation(self, dossier, annotation):
        bottomRight = annotation.rect.bottomRight
        topLeft = annotation.rect.topLeft

        req =  { "dossier": dossier,
                 "annotations": [{ "page": annotation.page,
                 "text": annotation.text,
                 "type" : annotation.type,
                 "rect": {"topLeft":{"x":topLeft.x, "y":topLeft.y},
                          "bottomRight":{"x":bottomRight.x, "y":bottomRight.y}}}]}

        return self.requester.apiAuthRequest("/parapheur/api/addAnnotation", req)


    def updateAnnotation(self, dossier, annotation):
        bottomRight = annotation.rect.bottomRight
        topLeft = annotation.rect.topLeft

        req =  { "dossier": dossier,
                 "annotations": [{ "uuid":annotation.uuid,
                                   "page": annotation.page,
                                   "text": annotation.text,
                                   "rect": {"topLeft":{"x":topLeft.x, "y":topLeft.y},
                                            "bottomRight":{"x":bottomRight.x, "y":bottomRight.y}}}]}

        return self.requester.apiAuthRequest("/parapheur/api/updateAnnotation", req)

    def removeAnnotation(self, dossier, uuid, page):

        req = {"dossier": dossier,
               "uuid": uuid,
               "page": page}

        return self.requester.apiAuthRequest("/parapheur/api/removeAnnotation", req)

    #FIXME: return List Annotation Object
    def getAnnotations(self, dossier):

        req = {"dossier": dossier}

        return self.requester.apiAuthRequest("/parapheur/api/getAnnotations", req)


