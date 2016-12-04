var currentRating = 0;

$(document).ready(function() {
        $(".form_star").hover(function() {
            $(this).removeClass("glyphicon-star-empty");
            $(this).prevAll().removeClass("glyphicon-star-empty");

            $(this).addClass("glyphicon-star");
            $(this).prevAll().addClass("glyphicon-star");

        }, function() {
            $(this).addClass("glyphicon-star-empty");
            $(this).prevAll().addClass("glyphicon-star-empty");

            $(this).removeClass("glyphicon-star");
            $(this).prevAll().removeClass("glyphicon-star");
        });

        // Select rating with star
        $(".form_star").on("click", function() {
            var rating = $(this).data("review");
            currentRating = rating;
            $("#form_rating").val(rating);

            $(".form_star").unbind('mouseenter mouseleave');
            $(this).removeClass("glyphicon-star glyphicon-star-empty");
            $(this).prevAll().removeClass("glyphicon-star glyphicon-star-empty");
            $(this).nextAll().removeClass("glyphicon-star glyphicon-star-empty");

            $(this).addClass("glyphicon-star");
            $(this).prevAll().addClass("glyphicon-star");
            $(this).nextAll().addClass("glyphicon-star-empty");
        });
});
