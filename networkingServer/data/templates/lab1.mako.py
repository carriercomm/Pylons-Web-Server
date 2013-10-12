# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1379696732.17011
_template_filename='/home/dan/Desktop/pylonsProjects/networkingServer/networkingserver/templates/lab1.mako'
_template_uri='/lab1.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<html>\n<head>\n\t<link rel="stylesheet" type="text/css" href="/css/bootstrap.min.css">\n\t<link rel="stylesheet" type="text/css" href="/css/site.css">\n\t<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js" type="text/javascript"></script>\n\t<script type="text/javascript" src="/js/bootstrap.min.js"></script>\n\t<script type="text/javascript">\n\t\t$(function(){\n\t\t\t/*$(\'#mainButton\').popover();*/\n\t\t\t$(\'#mainButton\').click(function(){\n\t\t\t\trotateDiv(\'#rotatingDiv\');\n\t\t\t});\n\t\t\t\t\n            \t});\n\t\tfunction rotateDiv(toRotate){\n\t\t\tvar el = $(\'#rotatingDiv\');\n\t\t\tel.animate({\'z-index\': el.css(\'z-index\')}, {duration: 1000, queue:false, step:function(now,fx){\n                \t\ttmpval = Math.round(fx.pos*360)%360;\n               \t\t\tel.css({\n                    \t\t\t\'transform\': \'rotate(\'+tmpval+\'deg)\',\n                    \t\t\t\'-moz-transform\':\'rotate(\'+tmpval+\'deg)\',\n                  \t  \t\t\'-webkit-transform\': \'rotate(\'+tmpval+\'deg)\'\n                \t\t})\t\n\t\t\t}})\n\t\t\treturn el;\n\t\t}\n\t</script>\n</head>\n<body>\n\t<div class="pageContent">\n\t\t<div class="half top blue">\n\t\t</div>\n\t\t<div id="rotatingDiv"><img src="/img/peppy.gif"/></div>\n\t\t<button type="button" id="mainButton" class="btn btn-danger btn-large" data-placement="top" data-content="Good work, now click again!">Do a barrel roll!</button>\n\t\t<div class="half bottom white">\n\t\t</div>\n\t</div>\n</body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


