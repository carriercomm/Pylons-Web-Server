# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1381090505.929452
_template_filename='/home/dan/Desktop/Fall_2013/Networking/pylonsProjects/networkingServer/networkingserver/templates/play.mako'
_template_uri='/play.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<!--\n Dan Robinson\n 0700662\n-->\n<html>\n<head>\n\t<link rel="stylesheet" type="text/css" href="/css/bootstrap.min.css">\n\t<link rel="stylesheet" type="text/css" href="/css/site.css">\n\t<script src="/js/jquery-1.10.2.min.js" type="text/javascript"></script>\n\t<script type="text/javascript" src="/js/bootstrap.min.js"></script>\n\t<script type="text/javascript">\n\t\t$(function(){\n\t\t\t/*$(\'#mainButton\').popover();*/\n\t\t\t$(\'#mainButton\').click(function(){\n\t\t\t\trotateDiv(\'#rotatingDiv\');\n\t\t\t});\n            \t});\n\t\tfunction rotateDiv(toRotate){\n\t\t\tvar el = $(\'#rotatingDiv\');\n\t\t\tel.animate({\'z-index\': el.css(\'z-index\')}, {duration: 1000, queue:false, step:function(now,fx){\n                \t\ttmpval = Math.round(fx.pos*360)%360;\n               \t\t\tel.css({\n                    \t\t\t\'transform\': \'rotate(\'+tmpval+\'deg)\',\n                    \t\t\t\'-moz-transform\':\'rotate(\'+tmpval+\'deg)\',\n                  \t  \t\t\'-webkit-transform\': \'rotate(\'+tmpval+\'deg)\'\n                \t\t})\t\n\t\t\t}})\n\t\t\treturn el;\n\t\t}\n\n\t\tfunction checkCharacter(){\n\t\t\t// Get character selected\n\t\t\tvar character  = $(\'#characterSelector\').find(\'.active img\').attr(\'data-name\');\n\t\t\t$(\'#characterSelectorInput\').val(character);\n\t\t\t\n\t\t}\n\t</script>\n</head>\n<body>\n\t<div class="pageContent">\n\t\t<div id="mainMenu">\n\t\t\t<ul class="nav nav-pills">\n \t\t\t\t<li>\n    \t\t\t\t\t<a href="/">Home</a>\n  \t\t\t\t</li>\n\t\t\t</ul>\n\t\t</div>\n\t\t<div class="mainContent">\t\t\t\n\t\t\t<h1>Hello ')
        # SOURCE LINE 49
        __M_writer(escape(c.userid))
        __M_writer(u'</h1>\n\t\t\t<div id="rotatingDiv"><img src=')
        # SOURCE LINE 50
        __M_writer(escape(c.characters[c.userid]))
        __M_writer(u'></div>\n\t\t\t<button type="button" id="mainButton" class="btn btn-danger btn-large">Do a barrel roll!</button>\n\t\t</div>\n\t\t<div id="footer">\n\t\t\t<h3>Lab 3</h3>\n\t\t\t<p>To test the REST functionality follow these steps:</p>\n\t\t\t<ul>\n\t\t\t\t<li>Navigate to http://127.0.0.1:5000/</li>\n\t\t\t</ul>\n\t\t\t<h4>ADD</h4>\n\t\t\t<ul>\n\t\t\t\t<li>Click "Add new character" in the top left nav.</li>\n\t\t\t\t<li>specify a name and link to an image.</li>\n\t\t\t\t<li>Click "Save"</li>\n\t\t\t\t<li>Your character should be added to the list, and the page will reload.</li>\n\t\t\t\t<li>When the page reloads, a message should be displayed under the main nav, telling you the success or failure of your action.</li>\n\t\t\t</ul>\n\t\t\t<h4>EDIT</h4>\n\t\t\t<ul>\n\t\t\t\t<li>Click one of the "edit" buttons below the character you want to change.</li>\n\t\t\t\t<li>Specify a new name or image</li>\n\t\t\t\t<li>Click "Save"</li>\n\t\t\t\t<li>Your character should be successfully changed.</li>\n\t\t\t</ul>\n\t\t\t<h4>DELETE</h4>\n\t\t\t<ul>\n\t\t\t\t<li>Click the "delete" button below the character you want to remove.</li>\n\t\t\t\t<li>The page should reload and your character should be gone.</li>\n\t\t\t</ul>\n\t\t</div>\n\t</div>\n</body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


