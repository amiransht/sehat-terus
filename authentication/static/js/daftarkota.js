$.ajax({
    url: 'https://dev.farizdotid.com/api/daerahindonesia/provinsi',
    type: 'GET',
    dataType: 'json',
    success: function(data){
        var provinsi = data.provinsi;
        var provinsiSelect = document.getElementById('id_provinsi');
        for (var i = 0; i < provinsi.length; i++) {
            var option = document.createElement('option');
            option.value = provinsi[i].id;
            option.text = provinsi[i].nama;
            provinsiSelect.appendChild(option);
        }
    }
});
function getCity(){
    var provinsi = document.getElementById('id_provinsi').value;
    $.ajax({
        url: 'https://dev.farizdotid.com/api/daerahindonesia/kota?id_provinsi=' + provinsi,
        type: 'GET',
        dataType: 'json',
        success: function(data){
            var kota = data.kota_kabupaten;
            var kotaSelect = document.getElementById('id_kota');
            kotaSelect.innerHTML = '';
            for (var i = 0; i < kota.length; i++) {
                var option = document.createElement('option');
                option.value = kota[i].id;
                option.text = kota[i].nama;
                kotaSelect.appendChild(option);
            }
        }
    });
}
function getDistrict(){
    var kota = document.getElementById('id_kota').value;
    $.ajax({
        url: 'https://dev.farizdotid.com/api/daerahindonesia/kecamatan?id_kota=' + kota,
        type: 'GET',
        dataType: 'json',
        success: function(data){
            var kecamatan = data.kecamatan;
            var kecamatanSelect = document.getElementById('id_kecamatan');
            kecamatanSelect.innerHTML = '';
            for (var i = 0; i < kecamatan.length; i++) {
                var option = document.createElement('option');
                option.value = kecamatan[i].id;
                option.text = kecamatan[i].nama;
                kecamatanSelect.appendChild(option);
            }
        }
    });
}