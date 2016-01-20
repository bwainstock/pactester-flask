$(function() {
    $('#info-btn').click(function() {
        var pac_string = $('#pac-script').val();
        var form_data = {
            pac_string: $('#pac-script').val(),
            myip: $('#myip').val(),
            test_url: $('#url').val()
        };
        var submit = $.post('/api/uploadpac/', form_data );
        submit.done(function( data ) {
           $('#error').html(data);
        });
    });
});
