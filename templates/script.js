alert('Fuck');
$(document).ready(function(){
    $('#user').hide();

    if($('#user').val() == 'empty'){
        $('#user').slideDown('slow');
    }

    $(document).on('click', '#like', function(){
        //Do stuff here
        alert('Placeholder');
    });

    $(document).on('click', '#dislike', function(){
        //Do stuff here
        alert('Placeholder');
    });

    $(document).on('click', '#favorites', function(){
        //Do stuff here
        alert('Placeholder');
    });

});
