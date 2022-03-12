$(document).ready(function(jQuery) {
    jQuery(function ($) {
        let csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
        let patient_field = $('select#id_patient');
        let exempt_field = $('select#id_exempt');
        let service_field = $('select#id_services');
        let summa_field = $('input#id_summa')
        let patient = id_patient.value;
        let exempt_value = id_exempt.value;
        let exempt = 0;
        let services = service_field.val();
        let cost = id_cost.value;
        let isStaff = false;
        let balance = 0;
        let temp_balance = 0;
        let policy = 0;

        get_patient().then(function(data){
            console.log(data)
        }).catch(function (err){
            console.log(err)
        });

        get_cost().then( response =>{
                 console.log('service connection successful; response is: ' + response);
                 let js_response = JSON.parse(response)
                 id_cost.value = js_response['cost']
                 cost = js_response['cost']
                 summa_calculation()
        });

        get_exempt().then( function (response){
                console.log('exempt connection successful; response is: ' + response);
                summa_calculation()
        });

        function get_patient(){
            return new Promise(function(resolve, reject){
                $.ajax({
                    type: "POST",
                    url: "{{ '../../../../../../../get_patient' }}",
                    data: { csrfmiddlewaretoken: csrftoken, text: patient },
                    success: function callback(response){
                                console.log('patient connection successful; response is: ' + response);
                                response = JSON.parse(response);
                                isStaff = response['isStaff'];
                                balance = response['balance'];
                                policy = response['policy'];
                                if (isStaff){
                                    alert("Пациент являет сотрудником компании, поэтому лечение пройдет бесплатно")
                                    id_summa.value = 0
                                    summa_field.attr('disabled', true)
                                } else {
                                    summa_field.attr('disabled', false)
                                    if (policy == 0){
                                        alert('У пациента нет страхового полиса, скидка не предоставляется')
                                    } else {
                                        if (balance > 0){
                                            alert('Страховой полис пациента может погасить до ' + balance + ' рублей')
                                        }
                                    }

                                }
                                summa_calculation()
                                resolve('Данные пациента загружены')
                    },
                    error: function (err) {
                        reject('Пациент не найден')
                    }
                });
            });
        }



        var frm = $('form');
        var chosenBtn = frm.find('[name="_save"]');
        var btns = frm.find('[name="_save"], [name="_addanother"], [name="_continue"]');
        btns.unbind('click.btnAssign').bind('click.btnAssign', function(e)
        {
            chosenBtn = $(this);
        });
        frm.unbind('submit.saveStuff').bind('submit.saveStuff', function(e)
        {

            summa_field.attr("disabled", false);
            change_balance().then(function(response){
                console.log(response);
            }).catch(function (err){
                console.log('Баланс не был успешно изменен');
            });

            frm.append(
            [
                '<input type="hidden" name="',
                chosenBtn.attr('name'),
                '" value="',
                chosenBtn.attr('value'),
                '" />'
            ].join(''));
        });


         patient_field.on('change', function() {
             console.log(id_patient.value);
             patient = id_patient.value;
             get_patient().then(function(data){
                console.log(data)
             }).catch(function (err){
                console.log(err)
             })
        });

        service_field.on('change', function() {
             get_cost().then( response =>{
                 console.log('service connection successful; response is: ' + response);
                 let js_response = JSON.parse(response)
                 id_cost.value = js_response['cost']
                 cost = js_response['cost']
                 summa_calculation()
            });
        });

        exempt_field.on('change', function() {
            get_exempt().then( function (response){
                console.log('exempt connection successful; response is: ' + response);
                summa_calculation()
            })
        });

        function get_exempt(){
            exempt_value = id_exempt.value;
            var text = exempt_value
            return $.ajax({
                type: "POST",
                url: "{{ '../../../../../../../get_exempt' }}",
                data: { csrfmiddlewaretoken: csrftoken, text: text },
                success: function (response){
                    response = JSON.parse(response);
                    exempt = response['exempt'];
                },
                error: function (err) {
                    exempt = 0;
                    summa_calculation()
                }
            });
        }

        function change_balance(){
            return new Promise(function (resolve, reject){
                var text = temp_balance
                $.ajax({
                    type: "POST",
                    url: "{{ '../../../../../../../change_balance' }}",
                    data: { csrfmiddlewaretoken: csrftoken, text: text, patient: patient},
                    success: function (response){
                        resolve(response)
                    },
                    error: function (err) {
                        reject(err)
                    }
                });
            });
        }

        function get_cost(){
            return new Promise(function (resolve){
                var selected = $('select#id_services').val();
                var text = JSON.stringify(selected)
                 $.ajax({
                    type: "POST",
                    url: "{{ '../../../../../../../get_cost' }}",
                    data: { csrfmiddlewaretoken: csrftoken, text: text },
                    success: function (response){
                        resolve(response)
                    }
                });
            });
        }

        function summa_calculation(){
            console.log('cost is:' + cost)
            console.log('exempt is:' + exempt)
            temp_balance = balance
            if (isStaff){
                id_summa.value = 0
            } else {
                // console.log(id_summa.value)
                let summa = cost * ((100-exempt)/100)
                if (temp_balance > 0){
                    temp_balance = temp_balance - summa
                    summa = 0
                    if (temp_balance < 0){
                        summa = summa + temp_balance * (-1)
                        temp_balance = 0
                    }
                }
                console.log('К оплате: ' + summa)
                console.log('Баланс: '+ temp_balance)
                id_summa.value = summa.toFixed()
            }
        }
    });
});