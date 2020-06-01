var csrftoken = $.cookie('csrftoken');
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));

}

// Sets up AJAX
$.ajaxSetup({
    beforeSend: function (xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

$(document).ready(function () {
    $('a.plus-or-minus').click(function (e) {
        e.preventDefault();

        var previous_action = $(this).data('action');

        if ($(this).hasClass('fa-plus')) {
            $(this).removeClass('fa-plus').addClass('fa-minus')
        } else {
            $(this).removeClass('fa-minus').addClass('fa-plus')
        }

        $(this).data('action', previous_action == 'open' ? 'close' : 'open');


        if (previous_action == 'open') {
            $(this).parent().next().slideDown()
        } else {
            $(this).parent().next().slideUp()
        }
    })
});