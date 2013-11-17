$(function(){
  $('#searchForm').on('submit', function(){
      var searchField = $('#searchTerm').val();
      var numResults = $('#numResults').val();
      searchImages(searchField, numResults);
      return false;
  });
});


function searchImages(searchTerm, numResults){
    var imageContainer = $('#imageSlider');
    showLoading(imageContainer);

    $.ajax({
      type: "GET",
      url: '/pictures',
      data: {'searchTerm': searchTerm, 'numResults': numResults},
      success: function(data) {
        data = $.trim(data);
        images = $.parseJSON(data);

        if (images.message){
            showMessage(images.message);
        } else {
            for (var index in images) {
                var imageUrl = images[index].url;
                console.log(imageUrl);
                $("#imageSlider .carousel-inner").append('<div class="imageBox"><img src="' + imageUrl + '" alt="flickr image"/></div>');
            }
        }
        showImages(imageContainer);
      },
      error: function(data) {           // Stuff to run on error
        alert('ERROR');
      }
  });
}

function showLoading(imageContainer){
    imageContainer.find(".carousel-inner").hide();
    imageContainer.find(".carousel-inner").html('');
    imageContainer.find('.loading').show();
}
function showImages(imageContainer){
    imageContainer.find('.loading').hide();
    imageContainer.find('.carousel-inner').fadeIn('slow');
}