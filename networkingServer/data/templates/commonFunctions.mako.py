# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1382465779.212981
_template_filename=u'/home/dan/Desktop/Fall_2013/Networking/pylonsProjects/Pylons-Web-Server/networkingServer/networkingserver/templates/commonFunctions.mako'
_template_uri=u'/commonFunctions.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['head', 'nav', 'footer']


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 78
        __M_writer(u'\n')
        # SOURCE LINE 134
        __M_writer(u'\n\n')
        # SOURCE LINE 155
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_head(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n\n<head>\t\n\t<title>Networking</title>\n\t<link rel="stylesheet" type="text/css" href="/css/bootstrap.min.css">\n\t<link rel="stylesheet" type="text/css" href="/css/site.css">\n\t<script src="/js/jquery-1.10.2.min.js" type="text/javascript"></script>\n\t<script type="text/javascript" src="/js/bootstrap.min.js"></script>\n\t<script type="text/javascript" src="/js/userFunctions.js"></script>\n\t<script type="text/javascript">\n\t\t$(function(){\n\t\t\t/*$(\'#mainButton\').popover();*/\n\t\t\t$(\'#mainButton\').click(function(){\n\t\t\t\trotateDiv(\'#rotatingDiv\');\n\t\t\t});\n\n\t\t\tif ($(\'#messageBar\').length > 0){\n\t\t\t\t// set timeout to hide message\n\t\t\t\tvar messageTimeout = window.setTimeout(function(){hideMessage()}, 2000);\n\t\t\t\t\n\t\t\t\t// Remove message so that it doesn\'t show the next time the page is loaded\t\t\n\t\t\t\tremoveMessage();\n\t\t\t}\n\n\t\t\t/* Register */\n\t\t\t$(\'#addForm\').on("submit", function(event){\n\t\t\t\tvar name = $(\'#addUserForm input[name="userid"]\').val();\n\t\t\t\tvar image = $(\'#addUserForm input[name="image"]\').val();\n\t\t\t\t\n\t\t\t\taddUser(name, image);\t\t\t\t\n\t\t\t\treturn false;\n\t\t\t});\n\t\t\tupdateUserList();\n            \t});\n\n\t\tfunction postMessage(message){\n\t\t\t$.ajax({\n\t\t\t\ttype: "POST",\n\t\t\t\turl: \'/message/\' + message,\n\t\t\t\terror: function(data) {\n\t\t\t\t\tconsole.log("message post failed " + data);\n\t\t\t\t}\n\t\t\t});\n\t\t}\n\n\t\tfunction removeMessage(){\n\t\t\t$.ajax({\n\t\t\t\ttype: "DELETE",\n\t\t\t\turl: \'/message/xxx\',\n\t\t\t\terror: function(data){\n\t\t\t\t\tconsole.log("message delete failed " + data);\n\t\t\t\t}\n\t\t\t});\n\t\t}\n\n\t\tfunction showMessage(msg){\n\t\t\t$(\'#messageBar .content\').html(msg);\n\t\t\t$(\'#messageBar\').slideDown();\n\t\t\tvar messageTimeout = window.setTimeout(function(){hideMessage()}, 2000);\n\t\t}\n\t\tfunction hideMessage(){\n\t\t\t$(\'#messageBar\').slideUp();\n\t\t}\n\t\tfunction rotateDiv(toRotate){\n\t\t\tvar el = $(\'#rotatingDiv\');\n\t\t\tel.animate({\'z-index\': el.css(\'z-index\')}, {duration: 1000, queue:false, step:function(now,fx){\n                \t\ttmpval = Math.round(fx.pos*360)%360;\n               \t\t\tel.css({\n                    \t\t\t\'transform\': \'rotate(\'+tmpval+\'deg)\',\n                    \t\t\t\'-moz-transform\':\'rotate(\'+tmpval+\'deg)\',\n                  \t  \t\t\'-webkit-transform\': \'rotate(\'+tmpval+\'deg)\'\n                \t\t})\t\n\t\t\t}})\n\t\t\treturn el;\n\t\t}\n\t</script>\n</head>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_nav(context):
    context.caller_stack._push_frame()
    try:
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 79
        __M_writer(u'\n\t<header class="navbar navbar-inverse navbar-fixed-top bs-docs-nav">\n\t\t<div class="container">\n\t\t\t<div class="navbar-header">\n\t\t\t\t<a class="navbar-brand" href="/">Networking</a>\n\t\t\t</div>\n\t\t\t<nav class="collapse navbar-collapse bs-navbar-collapse" role="navigation">\n\t\t\t\t<ul id="mainMenu" class="nav navbar-nav navbar-inverse">\n\t\t\t\t\t<li class="active">\n\t\t\t\t\t\t<a href="/">Home</a>\n\t\t\t\t\t</li>\n\t\t\t\t\t<li>\n\t\t\t\t\t\t<a href="#registerModal" data-toggle="modal">Register</a>\n\t\t\t\t\t</li>\n\t\t\t\t\t<li>\n\t\t\t\t\t\t<a onclick="logout();">Logout</a>\n\t\t\t\t\t</li>\n\t\t\t\t</ul>\n\t\t\t</nav>\n\t\t</div>\n')
        # SOURCE LINE 99
        if c.message:
            # SOURCE LINE 100
            __M_writer(u'\t\t<div id="messageBar">\n')
            # SOURCE LINE 101
        else:
            # SOURCE LINE 102
            __M_writer(u'\t\t<div id="messageBar" style="display: none;">\n')
            pass
        # SOURCE LINE 104
        __M_writer(u'\t\t\t<div class="content">\n\t\t\t\t')
        # SOURCE LINE 105
        __M_writer(escape(c.message))
        __M_writer(u'\n\t\t\t</div>\n\t\t</div>\n\t</header>\n\t<div id="registerModal" class="modal fade" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">\t\t\n\t\t<form role="form" id="registerForm" name="addUser" action="" method="POST">\n\t\t\t<div class="modal-dialog">\n\t\t\t\t<div class="modal-content">\n\t\t\t\t\t<div class="modal-header">\t\t\t\n\t\t\t\t\t\t<h2>Register</h2>\n\t\t\t\t\t</div>\t\n\t\t\t\t\t<div class="modal-body">\n\t\t\t\t\t\t<div class="form-group">\n\t\t\t\t\t\t\t<label>Username</label>\n\t\t\t\t\t\t\t<input id="regUsername" class="form-control" type="text" placeholder="Name" name="username" />\n\t\t\t\t\t\t</div>\n\t\t\t\t\t\t<div class="form-group">\n\t\t\t\t\t\t\t<label>Password</label>\n\t\t\t\t\t\t\t<input id="regPassword" class="form-control" type="password" placeholder="" name="password" />\n\t\t\t\t\t\t</div>\n\t\t\t\t\t</div>\n\t\t\t\t\t<div class="modal-footer">\n\t\t\t\t\t\t<button class="btn" data-dismiss="modal" aria-hidden="true">Close</button>\n\t\t\t\t\t\t<input class="btn btn-default btn-primary" type="button" name="submit" value="Submit" onclick="register($(\'#regUsername\').val(), $(\'#regPassword\').val());" />\n\t\t\t\t\t</div>\n\t\t\t\t</div>\n\t\t\t</div>\n\t\t</form>\n\t</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_footer(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 136
        __M_writer(u'\n\t<footer id="footer">\n\t\t<h3>Lab 4</h3>\n\t\t<p><b>Nosetests:</b></p>\n\t\t<ul>\n\t\t\t<li>Navigate to the networkingServer/ directory.</li>\n\t\t\t<li>Run:</li>\n\t\t\t<ul><li>nosetests networkingserver/tests/functional/test_mainController.py</li></ul>\n\t\t\t<li>The output should indicate 3 tests run and passed.</li>\n\t\t</ul>\n\t\t<p><b>Selenium:</b></p>\n\t\t<ul>\n\t\t\t<li>Start up the server:</li>\n\t\t\t<ul><li>paster serve --reload development.ini</li></ul>\n\t\t\t<li>Open Selenium IDE in Firefox</li>\n\t\t\t<li>Load the test suite named "Selenium.txt" in the root directory.</li>\n\t\t\t<li>Run the test suite.</li>\n\t\t</ul>\n\t</footer>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


