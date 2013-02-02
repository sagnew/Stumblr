$(document).ready(function(){

    $userPrompt = $('#prompt');
    $frame = $('#frame');
    $list = $('#list');
    $add_to_favorites = $('#add_to_favorites');
    $group = $('#group');
    $user = $('#user');
    $favorites = $('#favorites');
    $fav_icon = $('.fav_icon');
    $view = $('#view');

    $userPrompt.hide();
    $frame.hide();
    $list.hide();
    $add_to_favorites.hide();

    if($user.val() == ''){
        $userPrompt.slideDown('slow');
        $group.fadeOut('slow');
    }else{
        $frame.fadeIn('slow');
        $group.fadeIn('slow');
    }

    $favorites.click(function(){
        $list.fadeOut('slow');
        $frame.slideToggle('slow');
        $add_to_favorites.slideToggle('slow');
    });

    $view.click(function(){
        $add_to_favorites.fadeOut('slow');
        $list.slideToggle('slow');
        $frame.slideToggle('slow');
    });

    $fav_icon.click(function(){
        $thisIcon = $(this);

        $thisIcon.preventDefault();
        $frame.attr("src", $thisIcon.attr("href"));
        $list.slideUp('slow');
        $frame.slideDown('slow');
    });

});

function submitForm(){
    document.form.action = document.pressed;
    return true;
}
