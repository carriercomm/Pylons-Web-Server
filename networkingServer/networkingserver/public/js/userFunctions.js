function login(uname, passwd){
	$.ajax({
	    type: "POST",
	    url: '/login',
	    data: { 
		username: uname,
		password: passwd
	    },
	    success: function(data) {
		console.log(data);
		data = $.trim(data);
		if (data == "Valid"){
			showMessage("Welcome " + uname);
			window.location = "/dashboard/" + uname;
		} else if (data == "Invalid"){
			showMessage("Invalid username or password, please try again.");
		}
				
		/* window.location.reload(); */ 
	    },
	    error: function(data) {           // Stuff to run on error
		   alert('ERROR');
	    }
	});
	return false;
}
function logout(){
	$.ajax({
	    type: "POST",
	    url: '/logout',
	    success: function(data) {
		window.location.reload();
	    },
	    error: function(data) {           // Stuff to run on error
		   alert('ERROR');
	    }
	});
	return false;
}
function register(uname, passwd){
	$.ajax({
	    type: "POST",
	    url: '/users',
	    data: {
		username: uname,
		password: passwd
	    },
	    success: function(data) {
		showMessage(data);
		updateUserList();
		$('#registerModal').modal('hide');
		/* window.location.reload(); */
	    },
	    	error: function(data) {           // Stuff to run on error
		    alert('ERROR');
	       }
	 });
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
		showMessage(data);
		updateUserList();
	    },
	    	error: function(data) {           // Stuff to run on error
		   alert('ERROR');
	       }
	 });
}
function deleteUser(uid){
	$.ajax({
		type: "DELETE",
		url: '/users/' + uid,
		data: {
			userid: uid
		},
		success: function(data){
			showMessage(data);
			updateUserList();
		}, 
		error: function(data){
			showMessage("Character delete failed " + data);
		}
	});
}
function checkUser(){
	// Get user selected
	var user  = $('#userSelector').find('.active img').attr('data-name');
	$('#userSelectorInput').val(user);
			
}

function updateUserList(){
	// GET user list here.
	$.ajax({
		type: "GET",
		url: '/users',
		error: function(data){
			showMessage("User Listing failed. " + data);
		},
		success: function(data){
			if (data.length == 0){
				showMessage("User Listing failed. Cannot connect to the database, please try again.");
				return false
			}
			var userList = $.parseJSON(data);
			var template = '';
			for (var i = 0; i < userList.length; i++) {
				template = template + '<tr><td>' + userList[i].userid + '</td><td>' + userList[i].username + '</td><td><button class="btn btn-danger" onclick="deleteUser(\'' + userList[i].userid + '\');">Delete</button></tr>'
			}
			$('#userList').find('tbody').html(template);
		}
	});
}
