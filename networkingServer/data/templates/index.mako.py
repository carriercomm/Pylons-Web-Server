# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1382717922.529631
_template_filename='/home/dan/Desktop/Fall_2013/Networking/pylonsProjects/Pylons-Web-Server/networkingServer/networkingserver/templates/index.mako'
_template_uri='/index.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = []


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 5
    ns = runtime.TemplateNamespace(u'commonFunctions', context._clean_inheritance_tokens(), templateuri=u'commonFunctions.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, u'commonFunctions')] = ns

def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        commonFunctions = _mako_get_namespace(context, 'commonFunctions')
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<!--\n Dan Robinson\n 0700662\n-->\n')
        # SOURCE LINE 5
        __M_writer(u'\n<html>\n<head>\n')
        # SOURCE LINE 8
        __M_writer(escape(commonFunctions.head()))
        __M_writer(u'\n</head>\n<body>\n\t<div class="pageContent">\n\t\t')
        # SOURCE LINE 12
        __M_writer(escape(commonFunctions.nav()))
        __M_writer(u'\n\t\t<div class="mainContent">\n\t\t\t<h1>Networking Lab 6</h1>\n\t\t\t<h2>Daniel Robinson 0700662</h2>\n\t\t\t<h1>Please Sign In</h1>\t\t\t\n\t\t\t<form role="form" id="signInForm" name="signInForm" action="">\n\t\t\t\t<div class="form-group">\n\t\t\t\t\t<input type="text" class="form-control" id="inputUname" placeholder="Username" />\n\t\t\t\t</div>\n\t\t\t\t<div class="form-group">\n\t\t\t\t\t<input type="password" class="form-control" id="inputPassword" placeholder="Password" />\n\t\t\t\t</div>\n\t\t\t\t<div class="form-group">\n\t\t\t\t\t<button type="button" class="btn btn-default" onclick="login($(\'#inputUname\').val(), $(\'#inputPassword\').val());" >Sign in</button>\n\t\t\t\t</div>\n\t\t\t</form>\n\t\t</div>\n\t\t<div id="userList">\n\t\t\t<table class="table table-striped">\n\t\t\t\t<thead>\t\n\t\t\t\t\t<th>User ID</th>\n\t\t\t\t\t<th>User Name</th>\n\t\t\t\t\t<th>Action</th>\n\t\t\t\t</thead>\n\t\t\t\t<tbody>\n\t\t\t\t</tbody>\n\t\t\t</table>\n\t\t</div>\n\t\t')
        # SOURCE LINE 40
        __M_writer(escape(commonFunctions.footer()))
        __M_writer(u'\n\t</div>\n</body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


