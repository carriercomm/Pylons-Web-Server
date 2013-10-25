<%def name="head()">

<head>	
	<title>Networking</title>
	<link rel="stylesheet" type="text/css" href="/css/bootstrap.min.css">
	<link rel="stylesheet" type="text/css" href="/css/site.css">
	<script src="/js/jquery-1.10.2.min.js" type="text/javascript"></script>
	<script type="text/javascript" src="/js/bootstrap.min.js"></script>
	<script type="text/javascript" src="/js/userFunctions.js"></script>
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
			var el = $('#rotatingDiv');
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
	</script>
</head>
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
		<h3>Lab 4</h3>
		<p><b>Nosetests:</b></p>
		<ul>
			<li>Navigate to the networkingServer/ directory.</li>
			<li>Run:</li>
			<ul><li>nosetests networkingserver/tests/functional/test_mainController.py</li></ul>
			<li>The output should indicate 3 tests run and passed.</li>
		</ul>
		<p><b>Selenium:</b></p>
		<ul>
			<li>Start up the server:</li>
			<ul><li>paster serve --reload development.ini</li></ul>
			<li>Open Selenium IDE in Firefox</li>
			<li>Load the test suite named "Selenium.txt" in the root directory.</li>
			<li>Run the test suite.</li>
		</ul>
	</footer>
</%def>
