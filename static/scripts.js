$('#form1').submit(function (e) {
    alert()
    var form=$('#form1').serializeArray()
    console.log(form)
    return false
})