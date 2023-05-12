window.onload = function() {
  // Initialize and add the map
  let map;

  async function initMap() {
      // The location of Uluru
      const position = { lat: -25.344, lng: 131.031 };

      // The map, centered at Uluru
      map = new google.maps.Map(document.getElementById("map"), {
          zoom: 4,
          center: position,
          mapId: "DEMO_MAP_ID",
      });

      // The marker, positioned at Uluru
      const marker = new google.maps.Marker({
          map: map,
          position: position,
          title: "Uluru",
      });
  }

  initMap();
};
