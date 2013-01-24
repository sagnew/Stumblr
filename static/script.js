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
    function submitForm()
    {
        document.form.action = document.pressed;
        data.url = $('#tumblr').val();
        $.post(document.pressed, data);
        return true;
    }

});
