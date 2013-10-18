<!--
 Dan Robinson
 0700662
-->
<html>
<head>	
	<title>Networking</title>
	<link rel="stylesheet" type="text/css" href="/css/bootstrap.min.css">
	<link rel="stylesheet" type="text/css" href="/css/site.css">
	<script src="/js/jquery-1.10.2.min.js" type="text/javascript"></script>
	<script type="text/javascript" src="/js/bootstrap.min.js"></script>
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

			/* Add User */
			$('#addUserForm').on("submit", function(event){
				var name = $('#addUserForm input[name="userid"]').val();
				var image = $('#addUserForm input[name="image"]').val();
				
				addUser(name, image);				
				return false;
			});

			$('#editUserForm').on("submit", function(event){
				/* Delete old user and then add new user with updated fields */
				$.ajax({
					type: "DELETE",
					url: '/users/' + $('#editUserForm').find('.oldName').html(),
					error: function(data){
						console.log("User delete failed " + data);
					},
					success: function(data){
						updateUser($('#editUserModal').find('input[name="userid"]').val(),$('#editUserModal').find('input[name="image"]').val());
					}
				});

				return false;
			});
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

		function addUser(name, img){
			$.ajax({
			    type: "POST",
			    url: '/users/' + name,
			    data: { image: img },
			    success: function(data) {
				postMessage(data);
				window.location.reload();
			    },
			    	error: function(data) {           // Stuff to run on error
				   alert('ERROR');
			       }
			 })
		}
		function editUser(uname){
			$.ajax({
				type: "GET",
				url: '/users/' + uname,
				error: function(data){
					console.log("User Edit failed " + data)
				},
				success: function(data){
					var jsonData = $.parseJSON(data);
					var userid = jsonData.userid;
					var image = jsonData.image;
			
					$('#editUserModal').find('.oldName').html(userid);
					$('#editUserModal').find('input[name="userid"]').val(userid);
					$('#editUserModal').find('input[name="image"]').val(image);
					$('#editUserModal').modal();
				}
			});
						
		}
		function updateUser(uname, image){
			$.ajax({
			    type: "POST",
			    url: '/users/' + uname,
			    data: 'image=' + encodeURIComponent(image),
			    success: function(data) {
				postMessage(data);
				window.location.reload();
			    },
			    	error: function(data) {           // Stuff to run on error
				   alert('ERROR');
			       }
			 });
		}
		function deleteUser(uname){
			$.ajax({
				type: "DELETE",
				url: '/users/' + character,
				error: function(data){
					console.log("Character delete failed " + data);
				},
				success: function(data){
					postMessage(data);
					window.location.reload();
				}
			});
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

		function checkUser(){
			// Get user selected
			var user  = $('#userSelector').find('.active img').attr('data-name');
			$('#userSelectorInput').val(user);
					
		}
	</script>
</head>
<body>
	<div class="pageContent">
		<div id="mainMenu">
			<ul class="nav nav-pills">
 				<li class="active">
    					<a href="/">Home</a>
  				</li>
				<li>
					<a href="#addUserModal" data-toggle="modal">Add User</a>
				</li>
			</ul>
		</div>
		% if c.message:
		<div id="messageBar">
			<div class="content">
				${c.message}
			</div>
		</div>
		% endif

		<div id="addUserModal" class="modal hide fade" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">		
			<form id="addUserForm" name="addUser" action="" method="POST">
				<div class="modal-header">			
					<h2>Add a User</h2>
				</div>	
				<div class="modal-body">
					<label>Enter the name for the new user</label>
					<input type="text" placeholder="Name" name="userid" />
					<label>Enter a link to the users' image </label>
					<input type="text" placeholder="Ex. http://samplewebsite.com/image.jpg" name="image" />
				</div>
				<div class="modal-footer">
					<button class="btn" data-dismiss="modal" aria-hidden="true">Close</button>
					<input class="btn" type="submit" name="submit" value="Submit" />
				</div>	
			</form>
		</div>
		<div id="editUserModal" class="modal hide fade" tabindex="-1" role="dialog" aria-labelledby="editUser" aria-hidden="true">		
			<form id="editUserForm" name="editUserForm" action="" method="POST">
				<div class="modal-header">			
					<h2>Edit User</h2>
					<div class="oldName hidden"></div>
				</div>	
				<div class="modal-body">
					<label>Name</label>
					<input type="text" placeholder="" name="userid" />
					<label>Image</label>
					<input type="text" placeholder="" name="image" />
				</div>
				<div class="modal-footer">
					<button class="btn" data-dismiss="modal" aria-hidden="true">Close</button>
					<input class="btn" type="submit" name="save" value="Save" />
				</div>	
			</form>
		</div>
		<div class="mainContent">
			<h1>Networking Lab 4</h1>
			<h2>Daniel Robinson 0700662</h2>
			<h1>Choose a user to log in</h1>			
			<div id="userSelector">
				<%
				count=0
				%>
				% for user in c.users:
					<div class="user">
						<a href="/play/${user}"><img data-name="${user}" src="${c.users[user]}" /></a>
						<div class="bottom buttons">						
							<button class="btn btn-small btn-inverse" onclick="editUser('${user}');">Edit</button>
							<button class="btn btn-small btn-danger" onclick="deleteUser('${user}');">Delete</button>
						</div>
					</div>
					<%							
					count+=1
					%>
				% endfor				
			</div>
		</div>

		<div id="footer">
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
		</div>
	</div>
</body>
</html>
