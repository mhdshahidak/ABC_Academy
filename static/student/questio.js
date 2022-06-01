$(document).ready(function () {
    questions()
})

function questions() {
    data = {
        'exam_id': $("#examId").val(),
        csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val()
    }
    $.ajax({
        url: "/student/questions/",
        data: data,
        type: "POST",
        success: function (response) {
            console.log(response)
            if (response['lenght'] == 0) {
                $("#exampleModal").modal('show')
            }
            else{
                $("#questionsDiv").empty();
                $("#questionsDiv").append(' <h6 class="card-title d-flex justify-content-between">\
                <span> Question Number : </span>\
                <span> Mark : '+ response['mark'] + '</span>\
            </h6><br>\
                <ul class="list-group list-group-numbered">\
                    <li class="py-0">\
                      '+ response['question'] + '\
                    </li>\
                </ul>\
                <input type="number" name="questionId" value='+ response['id'] + ' hidden>\
                <div id="answerDiv">\
                </div>\
                <div class="row">\
                <div class="col-lg-12">\
                    <div class="btn-toolbar text-center">\
                        <div class=" btn-group-md">\
                            <button type="button" class="btn btn-primary">Mark For Review</button>\
                            <button type="button" class="btn btn-primary"> Skip</button>\
                            <button type="button" class="btn btn-primary">Reset</button>\
                        </div>\
                        <div class="d-grid gap-2 d-md-flex text-end" >\
                            <button type="submit" class="btn btn-success">Save &\
                                Next</button>\
                        </div>\
                    </div>\
                </div>\
            </div>')
                if (response['type'] == 'mcq') {
                    $.each(response['option'], function (key, value) {
                        $("#answerDiv").append(' <ul class="list-group list px-4 ">\
                        <li>\
                            <input name="answer" class="form-check-input me-1" type="checkbox" value='+ value + '\
                                aria-label="...">\
                            '+ value + '\
                        </li>\
                    </ul>')
                    });
    
                }
                else {
                    $("#answerDiv").append('<div class="col-10">\
                    <div class="form-group">\
                        <textarea class="form-control" required name="answer"\
                            id="editquestion"></textarea>\
                    </div>\
                </div>')
            }
            }
        },
        error: function () {
        }
    })
}

$("#questionsForm").validate({
    rules: {
        questionId: {
            required: true,
        },
        answer: {
            required: true,
        },
    },
    messages: {
        questionId: {
            required: "This field is required"
        },
        answer: {
            required: "This field is required",
        }
    },
    submitHandler: function (e) {
        var data = $("#questionsForm").serializeArray();
        savedata(data)
    }
})


function savedata(data) {
    console.log(data)
    $.ajax({
        url: "/student/datasave/",
        type: 'POST',
        data: data,
        success: function (responce) {
            questions()

        }

    })
    return false;
}

