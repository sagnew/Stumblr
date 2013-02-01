$(document).ready(function(){

    $('#prompt').hide();
    $('#frame').hide();
    $('#list').hide();
    $('#add_to_favorites').hide();

    if($('#user').val() == ''){
        $('#prompt').slideDown('slow');
        $('#group').fadeOut('slow');
    }else{
        $('#frame').fadeIn('slow');
        $('#group').fadeIn('slow');
    }

    $('#favorites').click(function(){
        $('#frame').fadeOut('slow');
        $('#add_to_favorites').fadeIn('slow');
    });

    $('#view').click(function(){
       $('#list').slideToggle('slow');
       $('#frame').slideToggle('slow');
    });

    $('.fav_icon').click(function(){
        $(this).preventDefault();
        $('#frame').attr("src", $(this).attr("href"));
        $('#list').slideToggle('slow');
        $('#frame').slideToggle('slow');
    });

});

function submitForm(){
    document.form.action = document.pressed;
    return true;
}
