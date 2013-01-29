$(document).ready(function(){

    var hasBeenClicked = false;

    $('#prompt').hide();
    $('#frame').hide();
    $('#list').hide();

    if($('#user').val() == ''){
        $('#prompt').slideDown('slow');
        $('group').hide();
    }else{
        $('#frame').fadeIn('slow');
    }

    $('#view').on("click", function(){
        if(hasBeenClicked){
            $('#list').slideUp('slow');
            $('#frame').slideDown('slow');
            hasBeenClicked = false;
        }else{
            $('#frame').slideUp('slow');
            $('#list').slideDown('slow');
            hasBeenClicked = true;
        }
    });

});

function submitForm(){
    document.form.action = document.pressed;
    return true;
}
