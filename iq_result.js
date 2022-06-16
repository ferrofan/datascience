function output_button() {
        iq = document.getElementById('entry').value;
        var iq_num = parseFloat(iq);
        var iq_num_JSON = JSON.stringify(iq_num); // Stringify converts a JavaScript object or value to a JSON string
        alert(iq_num_JSON);
        //const data_to_pass_in = {
         //   data_sent: iq_num
            // data_retuned: undefined
         //   };
        $.ajax({
            url:"/iq_result",
            type:"POST",
            contentType: "application/json",
            data: iq_num_JSON})
        };
        var select = document.getElementById('select'), test = {{ name | tojson }};
        function openPopup(){
            openWindow = alert('O seu QI é de: ${select}')
            }
            
        function closePopup(){
            fecharWindow = openWindow.close()
        }
