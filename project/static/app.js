function onLocationFound(e) {
    var radius = e.accuracy;
    L.marker(e.latlng).addTo(mymap)
        .bindPopup("Accuracy is " + radius + " m").openPopup();
    L.circle(e.latlng, radius).addTo(mymap);
}

function onLocationError(e) {
    alert(e.message);
}

function makeMap() {
    var TILE_URL = "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png";
    var MB_ATTR = 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors';

    mymap = L.map('leaflet-container');
    mymap.locate({ setView: true, maxZoom: 20 });
    mymap.on('locationfound', onLocationFound);
    mymap.on('locationerror', onLocationError);

    L.tileLayer(TILE_URL, { attribution: MB_ATTR }).addTo(mymap);
}

var layer = L.layerGroup();

function renderData(areaid) {
    $.getJSON("/area/" + areaid, function (obj) {
        var markers = obj.data.map(function (arr) {
            return L.marker([arr[0], arr[1]]);
        });
        mymap.removeLayer(layer);

        layer = L.layerGroup(markers);
        mymap.addLayer(layer);
    });
}


$(function () {
    makeMap();
    renderData('0');
    $('#areaselected').change(function () {
        var val = $('#areaselected option:selected').val();
        renderData(val);
    });
})