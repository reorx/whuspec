var toggleHandler = function(toggle) {
    var toggle = toggle;
    var radio = $(toggle).find("input");

    var checkToggleState = function() {
        if (radio.eq(0).is(":checked")) {
            $(toggle).removeClass("toggle-off");
        } else {
            $(toggle).addClass("toggle-off");
        }
    };

    checkToggleState();

    radio.eq(0).click(function() {
        $(toggle).toggleClass("toggle-off");
    });

    radio.eq(1).click(function() {
        $(toggle).toggleClass("toggle-off");
    });
};

$(function() {
    $('.record-button').click(function() {
        $(this).hide();
        $('.record').show();
    });

    $('.record .close').click(function() {
        $('.record').hide();
        $('.record-button').show();
    });

    var dateFormat = "yy-mm-dd";
    var dp = $('.column-right .datepicker').datepicker({
        // inline: true,
        prevText: "<",
        nextText: ">",
        dateFormat: dateFormat,
        showMonthAfterYear: true,
        monthNames: [
            "一月", "二月", "三月", "四月",
            "五月", "六月", "七月", "八月",
            "九月", "十月", "十一月", "十二月"],
        dayNamesMin: ["日", "一", "二", "三",
            "四", "五", "六"],

        // select event
        onSelect: function(dateText, dp) {
            $('.record .date input[name="date"]').val(dateText);
        }
    });

    // $('.record .date input[name="date"]').on('keydown keypress keyup', false);
    $('.record .date input[name="date"]').val(
        $.datepicker.formatDate(dateFormat, dp.datepicker('getDate')));

    $(".toggle").each(function(index, toggle) {
        toggleHandler(toggle);
    });
});
