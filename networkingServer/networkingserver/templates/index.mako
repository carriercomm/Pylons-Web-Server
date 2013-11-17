<!--
 Dan Robinson
 0700662
-->
<%namespace name="commonFunctions" file="commonFunctions.mako"/>
<html>
<head>
${commonFunctions.head()}
</head>
<body>
	<div class="pageContent">
		${commonFunctions.nav()}
		<div class="mainContent">
			<h1>Networking Lab 9</h1>
			<h2>Daniel Robinson 0700662</h2>
			<h1>Please Sign In</h1>			
			<form role="form" id="signInForm" name="signInForm" action="">
				<div class="form-group">
					<input type="text" class="form-control" id="inputUname" placeholder="Username" />
				</div>
				<div class="form-group">
					<input type="password" class="form-control" id="inputPassword" placeholder="Password" />
				</div>
				<div class="form-group">
					<button type="button" class="btn btn-default" onclick="login($('#inputUname').val(), $('#inputPassword').val());" >Sign in</button>
				</div>
			</form>
		</div>
		<div id="userList">
			<table class="table table-striped">
				<thead>	
					<th>User ID</th>
					<th>User Name</th>
					<th>Action</th>
				</thead>
				<tbody>
				</tbody>
			</table>
		</div>
		${commonFunctions.footer()}
	</div>
</body>
</html>
