$(document).ready(function() {
    $(':input[name$=estado]').on('change', function() {
        var prefix = $(this).getFormPrefix();
        $(':input[name=' + prefix + 'cidade]').val(null).trigger('change');
    });
});
