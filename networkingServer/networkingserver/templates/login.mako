<html>
<head>
	<link rel="stylesheet" type="text/css" href="/css/bootstrap.min.css">
	<link rel="stylesheet" type="text/css" href="/css/site.css">
	<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js" type="text/javascript"></script>
	<script type="text/javascript" src="/js/bootstrap.min.js"></script>
	<script type="text/javascript">
		$(function(){
			/*$('#mainButton').popover();*/
			$('#mainButton').click(function(){
				rotateDiv('#rotatingDiv');
			});

			// Create the character Slider
			$('#characterSelector').carousel('pause');
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
		<div class="half top blue">
		</div>
		<div class="mainContent">			
			<div id="rotatingDiv"><img src="/img/${c.character}.gif"/></div>
			<button type="button" id="mainButton" class="btn btn-danger btn-large" data-placement="top" data-content="Good work, now click again!">Do a barrel roll!</button>
		</div>
		<div class="half bottom white">
		</div>
	</div>
</body>
</html>
