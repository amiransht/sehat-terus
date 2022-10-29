$.ajax({
    url: 'https://dev.farizdotid.com/api/daerahindonesia/provinsi',
    dataType: 'json',
    type: 'GET',
    success: function(response) {
        const provinsi = response.provinsi;
        let selectBox = document.getElementById('id_provinsi');
        for (let i = 0; i < provinsi.length; i++ ) {
            let option = document.createElement('option');
            option.innerHTML = provinsi[i].nama;
            option.value = provinsi[i].id;
            selectBox.appendChild(option);
        }
    }
});

function getCity() {
    let selectBox = document.getElementById('id_provinsi');
    var value = selectBox.value;
    $.ajax({
        url: `https://dev.farizdotid.com/api/daerahindonesia/kota?id_provinsi=${value}`,
        dataType: 'json',
        type: 'GET',
        success: function(response) {
            const kota_kabupaten = response.kota_kabupaten;
            let selectBox2 = document.getElementById('id_kota');
            selectBox2.innerHTML = "";
            for (let i=0; i<kota_kabupaten.length; i++) {
                let kota = document.createElement('option');
                kota.innerHTML = kota_kabupaten[i].nama;
                kota.value = kota_kabupaten[i].id;
                selectBox2.appendChild(kota);
            }
        }
    });
}

function getDistrict() {
    let selectBox = document.getElementById('id_kota');
    var value = selectBox.value;
    $.ajax({
        url: `https://dev.farizdotid.com/api/daerahindonesia/kecamatan?id_kota=${value}`,
        dataType: 'json',
        type: 'GET',
        success: function(response) {
            const kecamatan = response.kecamatan;
            let selectBox3 = document.getElementById('id_kecamatan');
            selectBox3.innerHTML = "";
            for (let i=0; i<kecamatan.length; i++) {
                let district = document.createElement('option');
                district.innerHTML = kecamatan[i].nama;
                district.value = kecamatan[i].nama;
                selectBox3.appendChild(district);
            }
        }
    });
}