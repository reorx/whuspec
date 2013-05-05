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

    $('.record .datepicker').datepicker({
        // inline: true,
        prevText: "<",
        nextText: ">",
        dateFormat: "yy-mm-dd",
        showMonthAfterYear: true,
        monthNames: [
            "一月", "二月", "三月", "四月",
            "五月", "六月", "七月", "八月",
            "九月", "十月", "十一月", "十二月"],
        dayNamesMin: ["日", "一", "二", "三",
            "四", "五", "六"]
    }).datepicker('setDate', new Date());

    $(".toggle").each(function(index, toggle) {
        toggleHandler(toggle);
    });
});
