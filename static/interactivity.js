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
    $view.hide();
    $fav_icon.hide();

    if($user.val() == ''){
        $userPrompt.slideDown('slow');
        $group.fadeOut('slow');
    }else{
        $frame.fadeIn('slow');
        $group.fadeIn('slow');
    }

    $favorites.click(function(){
        if($list.is(":visible")){
            $list.fadeOut('slow');

            if($frame.is(":visible")){
                $frame.slideUp();
                $add_to_favorites.slideDown('slow');
            }else{
                $add_to_favorites.slideDown('slow');
            }

        }else{
            $frame.slideToggle('slow');
            $add_to_favorites.slideToggle('slow');
        }
    });

    $view.click(function(){

        if($add_to_favorites.is(":visible")){
            $add_to_favorites.fadeOut('slow');

            if($frame.is(":visible")){
                $frame.slideUp('slow');
                $list.slideDown('slow');
            }else{
                $list.slideDown('slow');
            }

        }else{
            $frame.slideToggle('slow');
            $list.slideToggle('slow');
        }
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
