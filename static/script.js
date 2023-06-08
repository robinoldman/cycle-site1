window.onload = function () {
    // Initialize and add the map
    let map;
    let directionsService;
    let directionsRenderer;

    async function initMap() {
        // The locations
        const position = { lat: 46.86297383978578, lng: 13.895879728836016 };
        const position2 = { lat: 46.72194183472748, lng: 13.608861910802464 };

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

window.onload = function () {
    // Initialize and add the map
    let map1;
    let directionsService;
    let directionsRenderer;

    async function initMap() {
        // The locations
        const position = { lat: 46.7884568546075, lng: 14.212468405696109 };
        const position2 = { lat: 46.63765231190369, lng: 14.166646881038057 };

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


