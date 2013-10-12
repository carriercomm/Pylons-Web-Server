import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from networkingserver.lib.base import BaseController, render

log = logging.getLogger(__name__)

class Lab1Controller(BaseController):

    def index(self):
        # Return a rendered template
        #return render('/lab1.mako')
        # or, return a response
        return render('/lab1.mako'); 
