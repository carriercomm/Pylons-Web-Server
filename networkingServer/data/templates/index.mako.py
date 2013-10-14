# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1381668766.791983
_template_filename='/home/dan/Desktop/Fall_2013/Networking/pylonsProjects/Pylons-Web-Server/networkingServer/networkingserver/templates/index.mako'
_template_uri='/index.mako'
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
        __M_writer(u'<!--\n Dan Robinson\n 0700662\n-->\n<html>\n<head>\t\n\t<title>Networking</title>\n\t<link rel="stylesheet" type="text/css" href="/css/bootstrap.min.css">\n\t<link rel="stylesheet" type="text/css" href="/css/site.css">\n\t<script src="/js/jquery-1.10.2.min.js" type="text/javascript"></script>\n\t<script type="text/javascript" src="/js/bootstrap.min.js"></script>\n\t<script type="text/javascript">\n\t\t$(function(){\n\t\t\t/*$(\'#mainButton\').popover();*/\n\t\t\t$(\'#mainButton\').click(function(){\n\t\t\t\trotateDiv(\'#rotatingDiv\');\n\t\t\t});\n\n\t\t\tif ($(\'#messageBar\').length > 0){\n\t\t\t\t// set timeout to hide message\n\t\t\t\tvar messageTimeout = window.setTimeout(function(){hideMessage()}, 2000);\n\t\t\t\t\n\t\t\t\t// Remove message so that it doesn\'t show the next time the page is loaded\t\t\n\t\t\t\tremoveMessage();\n\t\t\t}\n\n\t\t\t/* Add Character */\n\t\t\t$(\'#addCharacterForm\').on("submit", function(event){\n\t\t\t\tevent.preventDefault();\n\t\t\t\t\n\t\t\t\t$.ajax({\n\t\t\t\t    type: "POST",\n\t\t\t\t    url: \'/users/\' + $(\'#addCharacterForm input[name="userid"]\').val(),\n\t\t\t\t    data: $(this).serialize(),\n\t\t\t\t    success: function(data) {\n\t\t\t\t\tpostMessage(data);\n\t\t\t\t\twindow.location.reload();\n\t\t\t\t    },\n\t\t\t\t    \terror: function(data) {           // Stuff to run on error\n\t\t\t\t\t   alert(\'ERROR\');\n\t\t\t\t       }\n\t\t\t\t })\n\t\t\t});\n\n\t\t\t$(\'#editCharacterForm\').on("submit", function(event){\n\t\t\t\tevent.preventDefault();\n\t\t\t\t/* Delete old user and then add new user with updated fields */\n\t\t\t\t$.ajax({\n\t\t\t\t\ttype: "DELETE",\n\t\t\t\t\turl: \'/users/\' + $(\'#editCharacterForm\').find(\'.oldName\').html(),\n\t\t\t\t\terror: function(data){\n\t\t\t\t\t\tconsole.log("Character delete failed " + data);\n\t\t\t\t\t},\n\t\t\t\t\tsuccess: function(data){\n\t\t\t\t\t\tupdateCharacter($(\'#editCharacterModal\').find(\'input[name="userid"]\').val(),$(\'#editCharacterModal\').find(\'input[name="image"]\').val());\n\t\t\t\t\t}\n\t\t\t\t});\n\t\t\t});\n            \t});\n\n\t\tfunction postMessage(message){\n\t\t\t$.ajax({\n\t\t\t\ttype: "POST",\n\t\t\t\turl: \'/message/\' + message,\n\t\t\t\terror: function(data) {\n\t\t\t\t\tconsole.log("message post failed " + data);\n\t\t\t\t}\n\t\t\t});\n\t\t}\n\n\t\tfunction removeMessage(){\n\t\t\t$.ajax({\n\t\t\t\ttype: "DELETE",\n\t\t\t\turl: \'/message/xxx\',\n\t\t\t\terror: function(data){\n\t\t\t\t\tconsole.log("message delete failed " + data);\n\t\t\t\t}\n\t\t\t});\n\t\t}\n\t\tfunction editCharacter(character){\n\t\t\t$.ajax({\n\t\t\t\ttype: "GET",\n\t\t\t\turl: \'/users/\' + character,\n\t\t\t\terror: function(data){\n\t\t\t\t\tconsole.log("Character Edit failed " + data)\n\t\t\t\t},\n\t\t\t\tsuccess: function(data){\n\t\t\t\t\tvar jsonData = $.parseJSON(data);\n\t\t\t\t\tvar userid = jsonData.userid;\n\t\t\t\t\tvar image = jsonData.image;\n\t\t\t\n\t\t\t\t\t$(\'#editCharacterModal\').find(\'.oldName\').html(userid);\n\t\t\t\t\t$(\'#editCharacterModal\').find(\'input[name="userid"]\').val(userid);\n\t\t\t\t\t$(\'#editCharacterModal\').find(\'input[name="image"]\').val(image);\n\t\t\t\t\t$(\'#editCharacterModal\').modal();\n\t\t\t\t}\n\t\t\t});\n\t\t\t\t\t\t\n\t\t}\n\t\tfunction updateCharacter(character, image){\n\t\t\t$.ajax({\n\t\t\t    type: "POST",\n\t\t\t    url: \'/users/\' + character,\n\t\t\t    data: \'image=\' + encodeURIComponent(image),\n\t\t\t    success: function(data) {\n\t\t\t\tpostMessage(data);\n\t\t\t\twindow.location.reload();\n\t\t\t    },\n\t\t\t    \terror: function(data) {           // Stuff to run on error\n\t\t\t\t   alert(\'ERROR\');\n\t\t\t       }\n\t\t\t });\n\t\t}\n\t\tfunction deleteCharacter(character){\n\t\t\t$.ajax({\n\t\t\t\ttype: "DELETE",\n\t\t\t\turl: \'/users/\' + character,\n\t\t\t\terror: function(data){\n\t\t\t\t\tconsole.log("Character delete failed " + data);\n\t\t\t\t},\n\t\t\t\tsuccess: function(data){\n\t\t\t\t\tpostMessage(data);\n\t\t\t\t\twindow.location.reload();\n\t\t\t\t}\n\t\t\t});\n\t\t}\n\t\tfunction hideMessage(){\n\t\t\t$(\'#messageBar\').slideUp();\n\t\t}\n\t\tfunction rotateDiv(toRotate){\n\t\t\tvar el = $(\'#rotatingDiv\');\n\t\t\tel.animate({\'z-index\': el.css(\'z-index\')}, {duration: 1000, queue:false, step:function(now,fx){\n                \t\ttmpval = Math.round(fx.pos*360)%360;\n               \t\t\tel.css({\n                    \t\t\t\'transform\': \'rotate(\'+tmpval+\'deg)\',\n                    \t\t\t\'-moz-transform\':\'rotate(\'+tmpval+\'deg)\',\n                  \t  \t\t\'-webkit-transform\': \'rotate(\'+tmpval+\'deg)\'\n                \t\t})\t\n\t\t\t}})\n\t\t\treturn el;\n\t\t}\n\n\t\tfunction checkCharacter(){\n\t\t\t// Get character selected\n\t\t\tvar character  = $(\'#characterSelector\').find(\'.active img\').attr(\'data-name\');\n\t\t\t$(\'#characterSelectorInput\').val(character);\n\t\t\t\t\t\n\t\t}\n\t</script>\n</head>\n<body>\n\t<div class="pageContent">\n\t\t<div id="mainMenu">\n\t\t\t<ul class="nav nav-pills">\n \t\t\t\t<li class="active">\n    \t\t\t\t\t<a href="/">Home</a>\n  \t\t\t\t</li>\n\t\t\t\t<li>\n\t\t\t\t\t<a href="#addCharacterModal" data-toggle="modal">Add Character</a>\n\t\t\t\t</li>\n\t\t\t</ul>\n\t\t</div>\n')
        # SOURCE LINE 163
        if c.message:
            # SOURCE LINE 164
            __M_writer(u'\t\t<div id="messageBar">\n\t\t\t<div class="content">\n\t\t\t\t')
            # SOURCE LINE 166
            __M_writer(escape(c.message))
            __M_writer(u'\n\t\t\t</div>\n\t\t</div>\n')
            pass
        # SOURCE LINE 170
        __M_writer(u'\n\t\t<div id="addCharacterModal" class="modal hide fade" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">\t\t\n\t\t\t<form id="addCharacterForm" name="addCharacter" action="" method="POST">\n\t\t\t\t<div class="modal-header">\t\t\t\n\t\t\t\t\t<h2>Add a Character</h2>\n\t\t\t\t</div>\t\n\t\t\t\t<div class="modal-body">\n\t\t\t\t\t<label>Enter the character\'s name</label>\n\t\t\t\t\t<input type="text" placeholder="Name" name="userid" />\n\t\t\t\t\t<label>Enter a link to your characters image </label>\n\t\t\t\t\t<input type="text" placeholder="Ex. http://samplewebsite.com/image.jpg" name="image" />\n\t\t\t\t</div>\n\t\t\t\t<div class="modal-footer">\n\t\t\t\t\t<button class="btn" data-dismiss="modal" aria-hidden="true">Close</button>\n\t\t\t\t\t<input class="btn" type="submit" name="submit" value="Submit" />\n\t\t\t\t</div>\t\n\t\t\t</form>\n\t\t</div>\n\t\t<div id="editCharacterModal" class="modal hide fade" tabindex="-1" role="dialog" aria-labelledby="editCharacter" aria-hidden="true">\t\t\n\t\t\t<form id="editCharacterForm" name="editCharacterForm" action="" method="POST">\n\t\t\t\t<div class="modal-header">\t\t\t\n\t\t\t\t\t<h2>Edit Character</h2>\n\t\t\t\t\t<div class="oldName hidden"></div>\n\t\t\t\t</div>\t\n\t\t\t\t<div class="modal-body">\n\t\t\t\t\t<label>Name</label>\n\t\t\t\t\t<input type="text" placeholder="" name="userid" />\n\t\t\t\t\t<label>Image</label>\n\t\t\t\t\t<input type="text" placeholder="" name="image" />\n\t\t\t\t</div>\n\t\t\t\t<div class="modal-footer">\n\t\t\t\t\t<button class="btn" data-dismiss="modal" aria-hidden="true">Close</button>\n\t\t\t\t\t<input class="btn" type="submit" name="save" value="Save" />\n\t\t\t\t</div>\t\n\t\t\t</form>\n\t\t</div>\n\t\t<div class="mainContent">\n\t\t\t<h1>Networking Lab 4</h1>\n\t\t\t<h2>Daniel Robinson 0700662</h2>\n\t\t\t<h1>Choose Your Character</h1>\t\t\t\n\t\t\t<div id="characterSelector">\n\t\t\t\t')
        # SOURCE LINE 211

        count=0
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['count'] if __M_key in __M_locals_builtin_stored]))
        # SOURCE LINE 213
        __M_writer(u'\n')
        # SOURCE LINE 214
        for character in c.characters:
            # SOURCE LINE 215
            __M_writer(u'\t\t\t\t\t<div class="character">\n\t\t\t\t\t\t<a href="/play/')
            # SOURCE LINE 216
            __M_writer(escape(character))
            __M_writer(u'"><img data-name="')
            __M_writer(escape(character))
            __M_writer(u'" src="')
            __M_writer(escape(c.characters[character]))
            __M_writer(u'" /></a>\n\t\t\t\t\t\t<div class="bottom buttons">\t\t\t\t\t\t\n\t\t\t\t\t\t\t<button class="btn btn-small btn-inverse" onclick="editCharacter(\'')
            # SOURCE LINE 218
            __M_writer(escape(character))
            __M_writer(u'\');">Edit</button>\n\t\t\t\t\t\t\t<button class="btn btn-small btn-danger" onclick="deleteCharacter(\'')
            # SOURCE LINE 219
            __M_writer(escape(character))
            __M_writer(u'\');">Delete</button>\n\t\t\t\t\t\t</div>\n\t\t\t\t\t</div>\n\t\t\t\t\t')
            # SOURCE LINE 222
                                                        
            count+=1
            
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['count'] if __M_key in __M_locals_builtin_stored]))
            # SOURCE LINE 224
            __M_writer(u'\n')
            pass
        # SOURCE LINE 226
        __M_writer(u'\t\t\t\t<!--<a class="carousel-control left" href="#characterSelector" data-slide="prev">&lsaquo;</a>\n\t\t\t\t<a class="carousel-control right" href="#characterSelector" data-slide="next">&rsaquo;</a>\n\t\t\t\t-->\n\t\t\t</div>\n\t\t</div>\n\n\t\t<div id="footer">\n\t\t\t<h3>Lab 4</h3>\n\t\t\t<p><b>Nosetests:</b></p>\n\t\t\t<ul>\n\t\t\t\t<li>Navigate to the networkingServer/ directory.</li>\n\t\t\t\t<li>Run:</li>\n\t\t\t\t<ul><li>nosetests networkingserver/tests/functional/test_mainController.py</li></ul>\n\t\t\t\t<li>The output should indicate 3 tests run and passed.</li>\n\t\t\t</ul>\n\t\t\t<p><b>Selenium:</b></p>\n\t\t\t<ul>\n\t\t\t\t<li>Start up the server:</li>\n\t\t\t\t<ul><li>paster serve --reload development.ini</li></ul>\n\t\t\t\t<li>Open Selenium IDE in Firefox</li>\n\t\t\t\t<li>Load the test suite named "Selenium.txt" in the root directory.</li>\n\t\t\t\t<li>Run the test suite.</li>\n\t\t\t</ul>\n\t\t</div>\n\t</div>\n</body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


