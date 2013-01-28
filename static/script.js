$(document).ready(function(){

    $('#prompt').hide();
    $('#frame').hide();
    if($('#user').val() == ''){
        $('#prompt').slideDown('slow');
    }else{
        $('#frame').fadeIn('slow');
    }

});

function submitForm()
{
    document.form.action = document.pressed;
    data.url = $('#tumblr').val();
    $.post(document.pressed, data);
    return true;
}
