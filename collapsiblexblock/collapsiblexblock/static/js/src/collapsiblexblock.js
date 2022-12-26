/* Javascript for CollapsibleXBlock. */
function CollapsibleXBlock(runtime, element) {

    function updateResult(result) {
        $('.collapsible', element).text(result.header);
        $('.content', element).text(result.content);
    }

    var coll = $('.collapsible', element);
    var i;

    for (i = 0; i < coll.length; i++) {
        coll[i].addEventListener("click", function () {
            this.classList.toggle("active");
            var content = this.nextElementSibling;
            if (content.style.display === "block") {
                content.style.display = "none";
            } else {
                content.style.display = "block";
            }
        });
    }

    var handlerUrl = runtime.handlerUrl(element, 'apply_data');

    $('#applyButton', element).click(function(eventObject) {
        $.ajax({
            type: "POST",
            url: handlerUrl,
            data: JSON.stringify({
                "headerText":$('#headerText').val(),
                "contentText":$('#contentText').val()
             }),
            success: updateResult,
            dataType: "json"
        });
    });

}


