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
       $('#list').slideToggle('slow');
       $('#frame').slideToggle('slow');
    });

});

function submitForm(){
    document.form.action = document.pressed;
    return true;
}
