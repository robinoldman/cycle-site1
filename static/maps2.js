window.onload = function () {
    // Initialize and add the map
    let map;
    let directionsService;
    let directionsRenderer;

    async function initMap() {
        // The locations
        const position = { lat: 46.56554034613842, lng: 13.835657442284012 };
        const position2 = { lat: 46.4982834709951, lng: 13.320001793665154 };
        const position3 = { lat: 46.62451688781255, lng: 13.372616010150164 };
        // The map, centered at the new location
        map = new google.maps.Map(document.getElementById("map"), {
            zoom: 9,
            center: position,
        });

        // The marker, positioned at the new location
        const marker1 = new google.maps.Marker({
            map: map,
            position: position,
            title: "Marker Location",
        });

        // The second marker, positioned at a different location
        const marker2 = new google.maps.Marker({
            map: map,
            position: position2,
            title: "Marker Location 2",
        });

        // The second marker, positioned at a different location
        const marker3 = new google.maps.Marker({
            map: map,
            position: position3,
            title: "Marker Location 3",
        });

        // Initialize Directions Service and Renderer
        directionsService = new google.maps.DirectionsService();
        directionsRenderer = new google.maps.DirectionsRenderer();
        directionsRenderer.setMap(map);

        // Define the route request
        const request = {
            origin: position,
            waypoints: [
                {
                    location: position2,
                    stopover: true,
                },
            ],
            destination: position3,
            travelMode: google.maps.TravelMode.BICYCLING,
        };

        // Calculate the route and display it on the map
        directionsService.route(request, function (result, status) {
            if (status === google.maps.DirectionsStatus.OK) {
                directionsRenderer.setDirections(result);
            }
        });
    }

    initMap();
};