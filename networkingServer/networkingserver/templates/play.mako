<!--
 Dan Robinson
 0700662
-->
<html>
<head>
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
            	});
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

		function checkCharacter(){
			// Get character selected
			var character  = $('#characterSelector').find('.active img').attr('data-name');
			$('#characterSelectorInput').val(character);
			
		}
	</script>
</head>
<body>
	<div class="pageContent">
		<div id="mainMenu">
			<ul class="nav nav-pills">
 				<li>
    					<a href="/">Home</a>
  				</li>
			</ul>
		</div>
		<div class="mainContent">			
			<h1>Hello ${c.userid}</h1>
			<div id="rotatingDiv"><img src=${c.characters[c.userid]}></div>
			<button type="button" id="mainButton" class="btn btn-danger btn-large">Do a barrel roll!</button>
		</div>
		<div id="footer">
			<h3>Lab 3</h3>
			<p>To test the REST functionality follow these steps:</p>
			<ul>
				<li>Navigate to http://127.0.0.1:5000/</li>
			</ul>
			<h4>ADD</h4>
			<ul>
				<li>Click "Add new character" in the top left nav.</li>
				<li>specify a name and link to an image.</li>
				<li>Click "Save"</li>
				<li>Your character should be added to the list, and the page will reload.</li>
				<li>When the page reloads, a message should be displayed under the main nav, telling you the success or failure of your action.</li>
			</ul>
			<h4>EDIT</h4>
			<ul>
				<li>Click one of the "edit" buttons below the character you want to change.</li>
				<li>Specify a new name or image</li>
				<li>Click "Save"</li>
				<li>Your character should be successfully changed.</li>
			</ul>
			<h4>DELETE</h4>
			<ul>
				<li>Click the "delete" button below the character you want to remove.</li>
				<li>The page should reload and your character should be gone.</li>
			</ul>
		</div>
	</div>
</body>
</html>
