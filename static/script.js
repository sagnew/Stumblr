$(document).ready(function(){

    $('#prompt').hide();
    $('#frame').hide();
    $('#list').hide();

    if($('#user').val() == ''){
        $('#prompt').slideDown('slow');
        $('#group').fadeOut('slow');
    }else{
        $('#frame').fadeIn('slow');
        $('#group').fadeIn('slow');
    }

    $('#view').click(function(){
       $('#list').slideToggle('slow');
       $('#frame').slideToggle('slow');
    });

});

function submitForm(){
    document.form.action = document.pressed;
    return true;
}
