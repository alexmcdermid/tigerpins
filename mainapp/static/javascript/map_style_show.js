console.log("comeon");

function initMap() {
  const styledMapType = new google.maps.StyledMapType(
    [
      { elementType: "geometry", stylers: [{ color: "#f52245" }] },
      { elementType: "labels.text.fill", stylers: [{ color: "#523735" }] },
      { elementType: "labels.text.stroke", stylers: [{ color: "#f5f1e6" }] },
      {
        featureType: "administrative",
        elementType: "geometry.stroke",
        stylers: [{ color: "#c9b2a6" }],
      },
      {
        featureType: "administrative.land_parcel",
        elementType: "geometry.stroke",
        stylers: [{ color: "#f52245" }],
      },
      {
        featureType: "administrative.land_parcel",
        elementType: "labels.text.fill",
        stylers: [{ color: "#ae9e90" }],
      },
      {
        featureType: "landscape.natural",
        elementType: "geometry",
        stylers: [{ color: "#ab7b48" }],
      },
      {
        featureType: "poi",
        elementType: "geometry",
        stylers: [{ color: "#dfd2ae" }],
      },
      {
        featureType: "poi",
        elementType: "labels.text.fill",
        stylers: [{ color: "#93817c" }],
      },
      {
        featureType: "poi.park",
        elementType: "geometry.fill",
        stylers: [{ color: "#a5b076" }],
      },
      {
        featureType: "poi.park",
        elementType: "labels.text.fill",
        stylers: [{ color: "#447530" }],
      },
      {
        featureType: "road",
        elementType: "geometry",
        stylers: [{ color: "#f5f1e6" }],
      },
      {
        featureType: "road.arterial",
        elementType: "geometry",
        stylers: [{ color: "#fdfcf8" }],
      },
      {
        featureType: "road.highway",
        elementType: "geometry",
        stylers: [{ color: "#f8c967" }],
      },
      {
        featureType: "road.highway",
        elementType: "geometry.stroke",
        stylers: [{ color: "#e9bc62" }],
      },
      {
        featureType: "road.highway.controlled_access",
        elementType: "geometry",
        stylers: [{ color: "#e98d58" }],
      },
      {
        featureType: "road.highway.controlled_access",
        elementType: "geometry.stroke",
        stylers: [{ color: "#db8555" }],
      },
      {
        featureType: "road.local",
        elementType: "labels.text.fill",
        stylers: [{ color: "#806b63" }],
      },
      {
        featureType: "transit.line",
        elementType: "geometry",
        stylers: [{ color: "#dfd2ae" }],
      },
      {
        featureType: "transit.line",
        elementType: "labels.text.fill",
        stylers: [{ color: "#8f7d77" }],
      },
      {
        featureType: "transit.line",
        elementType: "labels.text.stroke",
        stylers: [{ color: "#ebe3cd" }],
      },
      {
        featureType: "transit.station",
        elementType: "geometry",
        stylers: [{ color: "#dfd2ae" }],
      },
      {
        featureType: "water",
        elementType: "geometry.fill",
        stylers: [{ color: "#201e20" }],
      },
      {
        featureType: "water",
        elementType: "labels.text.fill",
        stylers: [{ color: "#f52245" }],
      },
    ],
    { name: "Styled Map" }
  );

  const center = {
    lat: parseFloat("{{pin.lat}}"),
    lng: parseFloat("{{pin.long}}"),
  };
  const map = new google.maps.Map(document.getElementById("map"), {
    center: center,
    zoom: 4,
    mapTypeControlOptions: {
            mapTypeIds: ["map"],
          },
  });

//     const map = new google.maps.Map(document.getElementById("map"), {
//       zoom: 4,
//       center: new google.maps.LatLng(29.40297, 1.09515),
//       mapTypeControlOptions: {
//       mapTypeIds: ["map"],
//     },
//   });

  map.mapTypes.set("styled_map", styledMapType);
  map.setMapTypeId("styled_map");

  // The marker, positioned at center
  const marker = new google.maps.Marker({
    position: center,
    map: map,
  });
}

// function initMap() {
//     // The location of center
//     const center = { lat: parseFloat("{{pin.lat}}"), lng: parseFloat("{{pin.long}}") };
//     const map = new google.maps.Map(document.getElementById("map"), {
//         center: center,
//         zoom: 4,
//     });
//     // The marker, positioned at center
//     const marker = new google.maps.Marker({
//     position: center,
//     map: map,
//     });
// }
