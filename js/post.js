$(function(){
$("[name='image']").on('change', function () {
  var file = this.files[0];

  if (file.size > 1024) {
    alert('max upload size is 1k');
  }

  // Also see .name, .type
});
$('#myform').on('submit', function () {
  $.ajax({
    // Your server script to process the upload
    url: '/create',
    type: 'POST',

    // Form data
    data: new FormData($('#myform')[0]),

    // Tell jQuery not to process data or worry about content-type
    // You *must* include these options!
    cache: false,
    contentType: false,
    processData: false,

    // Custom XMLHttpRequest
    success: function (data) {
window.location="/myshop";
},
    xhr: function () {
      var myXhr = $.ajaxSettings.xhr();
      if (myXhr.upload) {
        // For handling the progress of the upload
        myXhr.upload.addEventListener('progress', function (e) {
          if (e.lengthComputable) {
            $('progress').attr({
              value: e.loaded,
              max: e.total,
            });
          }
        }, false);
      }
      return myXhr;
    }
  });
	return false;
});
});
