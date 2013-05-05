$(function() {
    $('.record-button').click(function() {
        $(this).hide();
        $('.record').show();
    });

    $('.record .close').click(function() {
        $('.record').hide();
        $('.record-button').show();
    });

    // $('.record .date').click(function() {
    // });
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
});
