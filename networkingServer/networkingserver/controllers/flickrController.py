import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from networkingserver.model.flickrModel import flickrModel

from networkingserver.lib.base import BaseController, render

log = logging.getLogger(__name__)

class FlickrcontrollerController(BaseController):

    def index(self):
        # Return a rendered template
        #return render('/flickrController.mako')
        # or, return a string
        return 'Hello World'

    def getPictures(self):

        if 'searchTerm' in request.params and 'numResults' in request.params:
          keyword = request.params['searchTerm']
          numResults = request.params['numResults']
        else:
          keyword = 'test'
          numResults = 1

        flickr = flickrModel()
        return flickr.getPictures(keyword, numResults)
