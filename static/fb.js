// Additional JS functions here
window.fbAsyncInit = function() {
    FB.init({
	appId      : '290104991112550', // App ID
	channelUrl : 'http://stumblr-pennapps.herokuapp.com', // Channel File
	status     : true, // check login status
	cookie     : true, // enable cookies to allow the server to access the session
	xfbml      : true  // parse XFBML
    });
    
    // Additional init code here
    FB.getLoginStatus(function(response) {
	if (response.status === 'connected') {
	    // connected
	    alert("connected init!");
	} else if (response.status === 'not_authorized') {
	    // not_authorized
	    alert("not_authorized!");
	} else {
	    // not_logged_in
	    alert("not_logged_in, so logging in...");
	    login();
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
	    alert("connected!");
        } else {
            // cancelled
	    alert("not connected!");
        }
    });
}


