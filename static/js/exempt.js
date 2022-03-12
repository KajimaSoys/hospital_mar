$(document).ready(function(jQuery) {
    jQuery(function ($) {
        $('input#id_exempt').on('change', function() {
            console.log("Работаем")
            let exempt = $('input#id_exempt')
            console.log(exempt.value)
            if (exempt.value > 100){
                exempt.value = 0;
                alert('Процент не может превышать значение 100');
            } else if (exempt.value < 0) {
                exempt.value = 0;
                alert('Процент не может быть меньше 0');
            }
        });
    });
});