$(function() {
    $('#upload-pac-btn').click(function() {
        var form_data = $('#pac-script').val();
        $.post('/api/uploadpac/', {pac: form_data} );
    });
});
