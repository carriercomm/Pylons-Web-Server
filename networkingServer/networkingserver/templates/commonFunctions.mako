<%def name="head()">
	<title>Networking</title>
	<link rel="stylesheet" type="text/css" href="/css/bootstrap.min.css">
	<link rel="stylesheet" type="text/css" href="/css/site.css">
	<script src="/js/jquery-1.10.2.min.js" type="text/javascript"></script>
	<script type="text/javascript" src="/js/bootstrap.min.js"></script>
	<script type="text/javascript" src="/js/userFunctions.js"></script>
	<script type="text/javascript" src="/js/flickrFunctions.js"></script>
	<script type="text/javascript">
		$(function(){
			/*$('#mainButton').popover();*/
			$('#mainButton').click(function(){
				rotateDiv('#rotatingDiv');
			});

			if ($('#messageBar').length > 0){
				// set timeout to hide message
				var messageTimeout = window.setTimeout(function(){hideMessage()}, 2000);
				// Remove message so that it doesn't show the next time the page is loaded		
				removeMessage();
			}

			/* Register */
			$('#addForm').on("submit", function(event){
				var name = $('#addUserForm input[name="userid"]').val();
				var image = $('#addUserForm input[name="image"]').val();
				
				addUser(name, image);				
				return false;
			});
			updateUserList();
            	});

		function postMessage(message){
			$.ajax({
				type: "POST",
				url: '/message/' + message,
				error: function(data) {
					console.log("message post failed " + data);
				}
			});
		}

		function removeMessage(){
			$.ajax({
				type: "DELETE",
				url: '/message/xxx',
				error: function(data){
					console.log("message delete failed " + data);
				}
			});
		}

		function showMessage(msg){
			$('#messageBar .content').html(msg);
			$('#messageBar').slideDown();
			var messageTimeout = window.setTimeout(function(){hideMessage()}, 2000);
		}
		function hideMessage(){
			$('#messageBar').slideUp();
		}
		function rotateDiv(toRotate){
			var el = $('.spiral');
			el.animate({'z-index': el.css('z-index')}, {duration: 1000, queue:false, step:function(now,fx){
                		tmpval = Math.round(fx.pos*360)%360;
               			el.css({
                    			'transform': 'rotate('+tmpval+'deg)',
                    			'-moz-transform':'rotate('+tmpval+'deg)',
                  	  		'-webkit-transform': 'rotate('+tmpval+'deg)'
                		})	
			}})
			return el;
		}
		$(function(){
			$('.spiral').click(function(){
				rotateDiv($('.spiral'));
			});
		});

	</script>
</%def>
<%def name="nav()">
	<header class="navbar navbar-inverse navbar-fixed-top bs-docs-nav">
		<div class="container">
			<div class="navbar-header">
				<a class="navbar-brand" href="/">Networking</a>
			</div>
			<nav class="collapse navbar-collapse bs-navbar-collapse" role="navigation">
				<ul id="mainMenu" class="nav navbar-nav navbar-inverse">
					<li class="active">
						<a href="/">Home</a>
					</li>
					<li>
						<a href="#registerModal" data-toggle="modal">Register</a>
					</li>
					% if c.authenticated:
					<li>
						<a href="#" onclick="logout();">Logout</a>
					</li>
					% endif
				</ul>
			</nav>
		</div>
		% if c.message:
		<div id="messageBar">
		% else:
		<div id="messageBar" style="display: none;">
		% endif
			<div class="content">
				${c.message}
			</div>
		</div>
	</header>
	<div id="registerModal" class="modal fade" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">		
		<form role="form" id="registerForm" name="addUser" action="" method="POST">
			<div class="modal-dialog">
				<div class="modal-content">
					<div class="modal-header">			
						<h2>Register</h2>
					</div>	
					<div class="modal-body">
						<div class="form-group">
							<label>Username</label>
							<input id="regUsername" class="form-control" type="text" placeholder="Name" name="username" />
						</div>
						<div class="form-group">
							<label>Password</label>
							<input id="regPassword" class="form-control" type="password" placeholder="" name="password" />
						</div>
					</div>
					<div class="modal-footer">
						<button class="btn" data-dismiss="modal" aria-hidden="true">Close</button>
						<input class="btn btn-default btn-primary" type="button" name="submit" value="Submit" onclick="register($('#regUsername').val(), $('#regPassword').val());" />
					</div>
				</div>
			</div>
		</form>
	</div>
</%def>

<%def name="footer()">
	<footer id="footer">
		<h3>Lab 9</h3>
		<p><b>Security</b></p>
		<ul>
			<li>Cross Site Scripting</li>
			<ul>
					<li>Auto-escaping is turned on for all variables printed on pages. This way no scripts can be inserted into variables on the page and executed.</li>
			</ul>
			<li>SQL Injection</li>
			<ul>
					<li>I am using the database cursor object to perform all database calls. This automatically blocks most SQL injection attacks.</li>
			</ul>
			<li>Cookie Manipulation</li>
			<ul>
					<li>All cookies are stored server-side, so the client cannot manipulate the cookies.</li>
			</ul>
			<li>Path Traversal</li>
			<ul>
					<li>Using the file "routing.py" all paths default to the mainController.py, so if there is a path that is not identified in the routes, it will default to the mainController, and it wont allow traversal.</li>
			</ul>
		</ul>
	</footer>
</%def>
