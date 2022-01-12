function get_rapo(number) {
    var today = new Date();
    var yr = today.getFullYear();
    var mth = today.getMonth() + 1;
    var day = today.getDate();


    var jqxhr = $.getJSON("static/js/secr.json", function (data) {
        var s_k = data['salt_s_key'];
        var s_key = day + mth + yr + s_k;
        s_key = md5(s_key);

        var url_final = 'http://localhost:8000/api_rest/'+s_key+'/'+number;

        $.ajax({

            type: 'GET',

            url: url_final,

            dataType: "json",

            success: function (data) {
                $("#right").append('<h2>'+data.nr+'</h2><br><h1>'+data.data+'</h1><br><h3>'+data.nazwa+'</h1><br><h4>'+data.temat+'</h4><br><p>'+data.tresc+'</p><br>');
            },

            error: function (response) {

                alert(response["responseJSON"]["error"]);

            }

        })
    })
}


function control_rapo(number, mode='create'){
    $("#right").empty();
    if (mode == 'create') {
        var hash_id = '#'+number;
        $(hash_id).css('color', 'red');
        get_rapo(number);
    }
    if (mode == 'delete') {
        $("#right").empty();
    }
}
