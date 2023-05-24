window.onload = function () {
    // Initialize and add the map
    let map;
    let directionsService;
    let directionsRenderer;

    async function initMap() {
        // The locations
        const position = { lat: 46.81293664397313, lng: 13.777807556365659 };
        const position2 = { lat: 46.772742777277074, lng: 13.746221862548072 };

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

        // Initialize Directions Service and Renderer
        directionsService = new google.maps.DirectionsService();
        directionsRenderer = new google.maps.DirectionsRenderer();
        directionsRenderer.setMap(map);

        // Define the route request
        const request = {
            origin: position,
            destination: position2,
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