// testing if we are getting data from home.html
//console.log(array);


window.initMap = function() {
  var pinColor = "FE7569";
  var pinColor2 = "FFFFFF"
    var pinImage = new google.maps.MarkerImage("http://chart.apis.google.com/chart?chst=d_map_pin_letter&chld=%E2%80%A2|" + pinColor,
        new google.maps.Size(21, 34),
        new google.maps.Point(0,0),
        new google.maps.Point(10, 34));
    var pinImage2 = new google.maps.MarkerImage("http://chart.apis.google.com/chart?chst=d_map_pin_letter&chld=%E2%80%A2|" + pinColor2,
      new google.maps.Size(21, 34),
      new google.maps.Point(0,0),
      new google.maps.Point(10, 34));
    var pinShadow = new google.maps.MarkerImage("http://chart.apis.google.com/chart?chst=d_map_pin_shadow",
        new google.maps.Size(40, 37),
        new google.maps.Point(0, 0),
        new google.maps.Point(12, 35));

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
        //this is the contindents fill color.
        // I kinda liked having #f52245. it's striking
        // second choice: e0a96d

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

  const map = new google.maps.Map(document.getElementById("map"), {
    zoom: 1.5,
    center: new google.maps.LatLng(29.40297, 1.09515),
    mapTypeControlOptions: {
      mapTypeIds: ["map"],
    },
  });

  map.mapTypes.set("styled_map", styledMapType);
  map.setMapTypeId("styled_map");

  const infowindow = new google.maps.InfoWindow({
    content: "contentString",
  });

  for (i = 0; i < array.length; i++) {
    if(array[i][2]==userid){
      marker = new google.maps.Marker({
        position: new google.maps.LatLng(array[i][0], array[i][1]),
        map: map,
        icon: pinImage,
        shadow: pinShadow,
        id: array[i][4],
        pinid: array[i][3],
        address: array[i][5],
        //label: `${array[i][2]}`
      })
    } else {
         marker = new google.maps.Marker({
        position: new google.maps.LatLng(array[i][0], array[i][1]),
        map: map,
        icon: pinImage2,
        shadow: pinShadow,
        id: array[i][4],
        pinid: array[i][3],
        address: array[i][5],
        //label: `${array[i][2]}`
      })
    }
   
    google.maps.event.addListener(marker, "click", function () {
      // do something with this marker ...
      //could somehow fetch the name of this user here
      infowindow.setContent(`${this.id}<br>${this.address}<br>
      <a href="../pins/${this.pinid}">click here for more info</a>
      `);
      infowindow.open(map, this);
    });
  }
}
