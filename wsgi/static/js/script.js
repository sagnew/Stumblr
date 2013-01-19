$(document).ready(function(){

    /*$(document).on('focus', '#text_input', function(){

        if($(this).val() == $(this)[0].defaultValue){
            $(this).val('');
        }

    });

    $(document).on('blur', '#text_input', function(){

        if($(this).val() === ''){
            $(this).val( $(this)[0].defaultValue );
        }

    });*/

    $('#like').click( function(){
        //Do stuff here
        alert('Placeholder');
    });

    $('#dislike').click( function(){
        //Do stuff here
        alert('Placeholder');
    });

    $('#favorites').click( function(){
        //Do stuff here
        alert('Placeholder');
    });

    $('#fblogin').click( function(){
        // Login to facebook!
        login();
    });


	  // Additional JS functions here
	  window.fbAsyncInit = function() {
	    FB.init({
	      appId      : '290104991112550', // App ID
	      channelUrl : 'http://app-stumblr.rhcloud.com/stumbl',  // Channel File

	      status     : true, // check login status
	      cookie     : true, // enable cookies to allow the server to access the session
	      xfbml      : true  // parse XFBML
	    });

	    // Additional init code here
	    FB.getLoginStatus(function(response) {

	  if (response.status === 'connected') {
	       // connected

	   // } else if (response.status === 'not_authorized') {
	        // not_authorized
	  } else {
               // not_logged_in, show 
	  }
	 });
	  };

	  // Load the SDK Asynchronously
	  (function(d){
	     var js, id = 'facebook-jssdk', ref = d.getElementsByTagName('script')[0];
	     if (d.getElementById(id)) {return;}
	     js = d.createElement('script'); js.id = id; js.async = true;
	     js.src = "//connect.facebook.net/en_US/all.js";
	     ref.parentNode.insertBefore(js, ref);
	   }(document));

	function login() {
	    FB.login(function(response) {
		if (response.authResponse) {
		    // connected
		} else {
		    // cancelled
		}
	    });
	}


});
