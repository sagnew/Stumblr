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

    $('#stumbl').click( function(){
	alert(userid);
    });
    var userid, tok;
    function init(id)
    {
	userid = id;
	alert("init");
    }
    
    // $('#stumbl').click( function(){
    // 	FB.getLoginStatus(function(response) {
    // 	    if (response.status === 'connected')
    // 	    {
    // 		$.ajax({
    // 		    type: "POST",
    // 		    url: "/submit",
    // 		    data: response,
    // 		    dataType: "json",
    // 		    success: function(msg) {
    // 			alert("Fuck yea");
    // 		    },
    // 		    error: fuck(errormessage) {
    // 			alert("Fuck no");
    // 		    }
		    
    // 		})
    
    // 	    }
    // 	    else {
    // 		alert("no connection");
    // 	    }
    // 	});
    // });
    // $('#stumbl').click( function(){
    //      $.post("/submit", {userID: uid, accessToken: tok});

    // 	});


    // $('#stumbl').click( function(){
    // 	$.ajax({
    // 	    url: "{{ url_for( 'response.authResponse.userID')}}",
    // 	    type: "POST",
    // 	    data: response,
    // 	    success: success,
    // 	    dataType: dataType
	    
    // 	})
	// $.post("/stumbl", 
	//     {userId: response.authResponse.userID,
	//      accessToken: response.authResponse.accessToken
	     
	// }); 


    //});



});
