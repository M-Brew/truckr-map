var map;
var directionsService;
var directionsDisplay;
var latitude;
var longitude;

function updateMap(){
    //get current location of tracking device from database
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open("GET", "truckr.php", true);
    xmlHttp.send();
    xmlHttp.onreadystatechange = function(){
        if(this.readyState == 4 && this.status == 200){
            var data = JSON.parse(this.responseText);
            latitude = data.latitude;
            longitude = data.longitude;
            console.log(latitude);
            console.log(longitude);

            //plot route when a change in coordinates is detected
            var lat;
            var lng;
            do{
                plotRoute();
                lat = latitude;
                lng = longitude;
            }while(latitude != lat && longitude != lng);
        }
    }
}

function initializeMap(){
    directionsService = new google.maps.DirectionsService();
    directionsDisplay = new google.maps.DirectionsRenderer();
    var accra = new google.maps.LatLng(5.6037, -0.1870);
    var mapOptions = {
        zoom: 14,
        center: accra
    }
    map = new google.maps.Map(
        document.getElementById('mapContainer'), mapOptions);
    directionsDisplay.setMap(map);

    setInterval(function(){
        updateMap();
        console.log("updating map...");
    }, 60000);
}

function plotRoute(){
    var startingPoint = new google.maps.LatLng(5.5480, -0.1927);
    var currentLocation = new google.maps.LatLng(latitude, longitude);
    var request = {
        origin: startingPoint,
        destination: currentLocation,
        travelMode: 'DRIVING'
    };
    directionsService.route(request, function(response, status){
        if(status == "OK"){
            directionsDisplay.setDirections(response);
        }
    });
}



