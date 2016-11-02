$(function () {
    $('[data-toggle="tooltip"]').tooltip()
});

var supportOnInput = 'oninput' in document.createElement('input');
var tweetButton = $('#tweet-button');
var newTweetForm = $('#new-tweet');

$('input[max-length]').each(function() {
    var $this = $(this);
    var maxLength = parseInt($this.attr('max-length'));
    $this.attr('max-length', null);

    var el = $('<span class="character-count">' + maxLength + '</span>');
    el.insertAfter($this);

    $this.bind(supportOnInput ? 'input' : 'keyup', function() {
        var cc = $this.val().length;

        el.text(maxLength - cc);

        if(maxLength < cc) {
            el.css('color', 'red');
            tweetButton.prop('disabled', true);
            newTweetForm.submit(function(e) {
                e.preventDefault();
            });
        } else {
            el.css('color', '');
            tweetButton.prop('disabled', false);
            newTweetForm.unbind('submit');
        }
    });
});

