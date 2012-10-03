
class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Rect(object):
    def __init__(self, topLeft, bottomRight):
        self.topLeft = topLeft
        self.bottomRight = bottomRight

class Annotation(object):
    def __init__(self):
        self.uuid = None
        self.type = "text"
        self.page = 0
        self.text = None
        self.rect = None

class AnnotationController(object):
    def __init__(self, requester):
        self.requester = requester

    def addAnnotation(self, dossier, annotation):
        bottomRight = annotation.rect.bottomRight
        topLeft = annotation.rect.topLeft

        req =  { "dossier": dossier,
                 "annotations": [{ "page": annotation.page,
                 "text": annotation.text,
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

        req = {"dossierRef": dossier,
               "uuid": uuid,
               "page": page}

        return self.requester.apiAuthRequest("/parapheur/api/removeAnnotation", req)

    #FIXME: return List Annotation Object
    def getAnnotations(self, dossier):

        req = {"dossierRef": dossier}

        return self.requester.apiAuthRequest("/parapheur/api/getAnnotations", req)


