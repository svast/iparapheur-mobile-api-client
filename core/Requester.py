import urllib2
from urllib2 import HTTPError
import pprint
import json
import os, re

pp = pprint.PrettyPrinter(indent=2)


class RequestException(Exception):
    def _get_message(self):
        return self._message
    def _set_message(self, message):
        self._message = message
    message = property(_get_message, _set_message)

class Requester(object):
    def __init__(self, endPoint):
        super(Requester, self).__init__()
        self.endPoint = endPoint
        self.logging = False


    def _apiRequest(self, uri, apipath, args):
        content = json.dumps(args)

        req = urllib2.Request(uri + apipath,
            headers={
                "Content-Type": "application/json",
                "Accept": "*/*",
                "User-Agent": "ph-ws-py/1",
                },
            data=content)
        try:
            r = urllib2.urlopen(req)
        except HTTPError as err:
            errorBody = err.read()
            jerr = json.loads(errorBody)
            raise RequestException(jerr["message"])

        else:
            response = r.read()
            jsonData = json.loads(response)

            pp.pprint(jsonData)
            return  jsonData

    def wrapLinesSmart(self, lineslist, size=100, delimiters='.,:\t '):
        "wrap at first delimiter left of size"

        wraplines = []
        for line in lineslist:
            while True:
                if len(line) <= size:
                    wraplines += [line]
                    break
                else:

#                    indent_match = re.match("( +)", line)
#                    indent = ""
#                    if (indent_match):
#                        indent = indent_match.group(0)

                    for look in range(size - 1, size / 2, -1):
                        if line[look] in delimiters:
                            front, line = line[:look + 1], line[look + 1:]
                            break
                    else:
                        front, line = line[:size], line[size:]
                    wraplines += [front]
        return wraplines

    def writeToFile(self, fname, content, suffix):

        raw_lines = content.split("\n")

        lines = self.wrapLinesSmart(raw_lines)

        file = open("snippets/" + fname + suffix, "w")
        for line in lines:
            file.write(line+'\n')


    def apiRequest(self, uri, apipath, args, suffix=""):
        fname = ""
        if self.logging:
            fname = os.path.split(apipath)[1]
            m = re.match("^([A-Za-z]+)", fname)
            if m:
                fname = m.group(0) + suffix

            self.writeToFile(fname, json.dumps(args, indent=4), "_in.js")


        retval = self._apiRequest(uri, apipath, args)

        if self.logging:

            self.writeToFile(fname, json.dumps(retval, indent=4), "_out.js")


        return retval


    def apiAuthRequest(self, apipath, args, suffix=""):
        assert self.ticket
        return self.apiRequest(self.endPoint, apipath + "?alf_ticket=" + self.ticket, args, suffix)


    def login(self, username, password):
        ret = self.apiRequest(self.endPoint, '/parapheur/api/login', {'username': username, 'password': password})

        if ret:
            self.ticket = ret["data"]["ticket"]

        return self.ticket


    def logout(self, ticket):
        req = {"ticket": ticket}

        return self.apiAuthRequest(self.endPoint, '/parapheur/api/logout', req)


