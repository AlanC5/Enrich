$(document).ready(function() {
    $("#STEM_button").on("click", function() {
        $(this).toggleClass("btn-primary");
        $("#id_category_0").prop("checked", !$("#id_category_0").prop("checked"));
    });

    $("#arts_button").on("click", function() {
        $(this).toggleClass("btn-primary");
        $("#id_category_1").prop("checked", !$("#id_category_1").prop("checked"));
    });

    $("#academic_button").on("click", function() {
        $(this).toggleClass("btn-primary");
        $("#id_category_2").prop("checked", !$("#id_category_2").prop("checked"));
    });

    $("#sports_button").on("click", function() {
        $(this).toggleClass("btn-primary");
        $("#id_category_3").prop("checked", !$("#id_category_3").prop("checked"));
    });

    $("#tuition_button").on("click", function() {
        $(this).toggleClass("btn-primary");
        $("#id_price_0").prop("checked", !$("#id_price_0").prop("checked"));
    });


});
