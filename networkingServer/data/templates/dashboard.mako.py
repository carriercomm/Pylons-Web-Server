# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1382036491.521777
_template_filename='/home/dan/Desktop/Fall_2013/Networking/pylonsProjects/Pylons-Web-Server/networkingServer/networkingserver/templates/dashboard.mako'
_template_uri='/dashboard.mako'
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
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<!--\n Dan Robinson\n 0700662\n-->\n')
        # SOURCE LINE 5
        __M_writer(u'\n<html>\n')
        # SOURCE LINE 7
        __M_writer(escape(commonFunctions.head()))
        __M_writer(u'\n\n<body>\n\t<div class="pageContent">\n\t\t')
        # SOURCE LINE 11
        __M_writer(escape(commonFunctions.nav()))
        __M_writer(u'\n\t\t<div class="mainContent">\n\t\t\t<h1>')
        # SOURCE LINE 13
        __M_writer(escape(c.username))
        __M_writer(u"'s Dashboard</h1>\n\t\t</div>\n\t\t")
        # SOURCE LINE 15
        __M_writer(escape(commonFunctions.footer()))
        __M_writer(u'\n\t</div>\n</body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


