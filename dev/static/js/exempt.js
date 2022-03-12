$(document).ready(function(jQuery) {
    jQuery(function ($) {

        $('input#id_exempt').on('change', function() {
            let exempt = id_exempt.value;

            if (exempt> 100){
                id_exempt.value = 0;
                alert('Процент не может превышать значение 100');
            } else if (exempt < 0) {
                id_exempt.value = 0;
                alert('Процент не может быть меньше 0');
            }
        });
    });
});