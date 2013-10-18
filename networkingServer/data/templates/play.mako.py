# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1381884493.72936
_template_filename='/home/dan/Desktop/Fall_2013/Networking/pylonsProjects/Pylons-Web-Server/networkingServer/networkingserver/templates/play.mako'
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
        __M_writer(u'<!--\n Dan Robinson\n 0700662\n-->\n<html>\n<head>\t\n\t<title>Networking</title>\n\t<link rel="stylesheet" type="text/css" href="/css/bootstrap.min.css">\n\t<link rel="stylesheet" type="text/css" href="/css/site.css">\n\t<script src="/js/jquery-1.10.2.min.js" type="text/javascript"></script>\n\t<script type="text/javascript" src="/js/bootstrap.min.js"></script>\n\t<script type="text/javascript">\n\t\t$(function(){\n\t\t\t/*$(\'#mainButton\').popover();*/\n\t\t\t$(\'#mainButton\').click(function(){\n\t\t\t\trotateDiv(\'#rotatingDiv\');\n\t\t\t});\n\n\t\t\tif ($(\'#messageBar\').length > 0){\n\t\t\t\t// set timeout to hide message\n\t\t\t\tvar messageTimeout = window.setTimeout(function(){hideMessage()}, 2000);\n\t\t\t\t\n\t\t\t\t// Remove message so that it doesn\'t show the next time the page is loaded\t\t\n\t\t\t\tremoveMessage();\n\t\t\t}\n\n\t\t\t/* Add User */\n\t\t\t$(\'#addUserForm\').on("submit", function(event){\n\t\t\t\tvar name = $(\'#addUserForm input[name="userid"]\').val();\n\t\t\t\tvar image = $(\'#addUserForm input[name="image"]\').val();\n\t\t\t\t\n\t\t\t\taddUser(name, image);\t\t\t\t\n\t\t\t\treturn false;\n\t\t\t});\n\n\t\t\t$(\'#editUserForm\').on("submit", function(event){\n\t\t\t\t/* Delete old user and then add new user with updated fields */\n\t\t\t\t$.ajax({\n\t\t\t\t\ttype: "DELETE",\n\t\t\t\t\turl: \'/users/\' + $(\'#editUserForm\').find(\'.oldName\').html(),\n\t\t\t\t\terror: function(data){\n\t\t\t\t\t\tconsole.log("User delete failed " + data);\n\t\t\t\t\t},\n\t\t\t\t\tsuccess: function(data){\n\t\t\t\t\t\tupdateUser($(\'#editUserModal\').find(\'input[name="userid"]\').val(),$(\'#editUserModal\').find(\'input[name="image"]\').val());\n\t\t\t\t\t}\n\t\t\t\t});\n\n\t\t\t\treturn false;\n\t\t\t});\n            \t});\n\n\t\tfunction postMessage(message){\n\t\t\t$.ajax({\n\t\t\t\ttype: "POST",\n\t\t\t\turl: \'/message/\' + message,\n\t\t\t\terror: function(data) {\n\t\t\t\t\tconsole.log("message post failed " + data);\n\t\t\t\t}\n\t\t\t});\n\t\t}\n\n\t\tfunction removeMessage(){\n\t\t\t$.ajax({\n\t\t\t\ttype: "DELETE",\n\t\t\t\turl: \'/message/xxx\',\n\t\t\t\terror: function(data){\n\t\t\t\t\tconsole.log("message delete failed " + data);\n\t\t\t\t}\n\t\t\t});\n\t\t}\n\n\t\tfunction addUser(name, img){\n\t\t\t$.ajax({\n\t\t\t    type: "POST",\n\t\t\t    url: \'/users/\' + name,\n\t\t\t    data: { image: img },\n\t\t\t    success: function(data) {\n\t\t\t\tpostMessage(data);\n\t\t\t\twindow.location.reload();\n\t\t\t    },\n\t\t\t    \terror: function(data) {           // Stuff to run on error\n\t\t\t\t   alert(\'ERROR\');\n\t\t\t       }\n\t\t\t })\n\t\t}\n\t\tfunction editUser(uname){\n\t\t\t$.ajax({\n\t\t\t\ttype: "GET",\n\t\t\t\turl: \'/users/\' + uname,\n\t\t\t\terror: function(data){\n\t\t\t\t\tconsole.log("User Edit failed " + data)\n\t\t\t\t},\n\t\t\t\tsuccess: function(data){\n\t\t\t\t\tvar jsonData = $.parseJSON(data);\n\t\t\t\t\tvar userid = jsonData.userid;\n\t\t\t\t\tvar image = jsonData.image;\n\t\t\t\n\t\t\t\t\t$(\'#editUserModal\').find(\'.oldName\').html(userid);\n\t\t\t\t\t$(\'#editUserModal\').find(\'input[name="userid"]\').val(userid);\n\t\t\t\t\t$(\'#editUserModal\').find(\'input[name="image"]\').val(image);\n\t\t\t\t\t$(\'#editUserModal\').modal();\n\t\t\t\t}\n\t\t\t});\n\t\t\t\t\t\t\n\t\t}\n\t\tfunction updateUser(uname, image){\n\t\t\t$.ajax({\n\t\t\t    type: "POST",\n\t\t\t    url: \'/users/\' + uname,\n\t\t\t    data: \'image=\' + encodeURIComponent(image),\n\t\t\t    success: function(data) {\n\t\t\t\tpostMessage(data);\n\t\t\t\twindow.location.reload();\n\t\t\t    },\n\t\t\t    \terror: function(data) {           // Stuff to run on error\n\t\t\t\t   alert(\'ERROR\');\n\t\t\t       }\n\t\t\t });\n\t\t}\n\t\tfunction deleteUser(uname){\n\t\t\t$.ajax({\n\t\t\t\ttype: "DELETE",\n\t\t\t\turl: \'/users/\' + character,\n\t\t\t\terror: function(data){\n\t\t\t\t\tconsole.log("Character delete failed " + data);\n\t\t\t\t},\n\t\t\t\tsuccess: function(data){\n\t\t\t\t\tpostMessage(data);\n\t\t\t\t\twindow.location.reload();\n\t\t\t\t}\n\t\t\t});\n\t\t}\n\t\tfunction hideMessage(){\n\t\t\t$(\'#messageBar\').slideUp();\n\t\t}\n\t\tfunction rotateDiv(toRotate){\n\t\t\tvar el = $(\'#rotatingDiv\');\n\t\t\tel.animate({\'z-index\': el.css(\'z-index\')}, {duration: 1000, queue:false, step:function(now,fx){\n                \t\ttmpval = Math.round(fx.pos*360)%360;\n               \t\t\tel.css({\n                    \t\t\t\'transform\': \'rotate(\'+tmpval+\'deg)\',\n                    \t\t\t\'-moz-transform\':\'rotate(\'+tmpval+\'deg)\',\n                  \t  \t\t\'-webkit-transform\': \'rotate(\'+tmpval+\'deg)\'\n                \t\t})\t\n\t\t\t}})\n\t\t\treturn el;\n\t\t}\n\n\t\tfunction checkUser(){\n\t\t\t// Get user selected\n\t\t\tvar user  = $(\'#userSelector\').find(\'.active img\').attr(\'data-name\');\n\t\t\t$(\'#userSelectorInput\').val(user);\n\t\t\t\t\t\n\t\t}\n\t</script>\n</head>\n<body>\n\t<div class="pageContent">\n\t\t<div id="mainMenu">\n\t\t\t<ul class="nav nav-pills">\n \t\t\t\t<li>\n    \t\t\t\t\t<a href="/">Home</a>\n  \t\t\t\t</li>\n\t\t\t</ul>\n\t\t</div>\n\t\t<div class="mainContent">\t\t\t\n\t\t\t<h1>Hello ')
        # SOURCE LINE 168
        __M_writer(escape(c.userid))
        __M_writer(u'</h1>\n\t\t\t<div id="rotatingDiv"><img src=')
        # SOURCE LINE 169
        __M_writer(escape(c.image))
        __M_writer(u'></div>\n\t\t\t<button type="button" id="mainButton" class="btn btn-danger btn-large">Do a barrel roll!</button>\n\t\t</div>\n\t</div>\n</body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


