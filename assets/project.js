$(document).ready(function () {
    $.getJSON('/fetchallproducttype', function (data) {
        data.map((item) => {
            $('#producttype').append($('<option>').text(item.producttype).val(item.productid))
        })
    })
    $('#producttype').change(function () {
        $.getJSON('/fetchallcompanyname', { "productid": $('#producttype').val() }, function (data) {
            $('#companyname').empty()
            $('#companyname').append($('<option>').text("-Select Company-"))
            data.map((item) => {
                $('#companyname').append($('<option>').text(item.companyname).val(item.companyid))
            })
        })
    });

    $('#companyname').change(function () {
        // alert($('#companyname').val())
        $.getJSON('/fetchallproductmodel', { "companyid": $('#companyname').val() }, function (data) {
            // alert(JSON.stringify(data))
            $('#modelname').empty()
            $('#modelname').append($('<option>').text("-Select Model-"))
            data.map((item) => {
                $('#modelname').append($('<option>').text(item.modelname).val(item.modelid))
            })
        })
    })
})