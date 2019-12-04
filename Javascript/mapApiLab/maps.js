
const generateMap = (lat, lng, zoom) => {
    let myMap = L.map('map').setView([lat, lng], zoom);

    L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
        attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a><br/> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
        maxZoom: 18,
        id: 'mapbox/streets-v11',
        accessToken: `${mapbox_token}`
    }).addTo(myMap);

    return myMap
}

const generateMarkers = (map, markerCount) => {

    let left = map.getBounds()._southWest.lng;
    let right = map.getBounds()._northEast.lng;
    let top = map.getBounds()._northEast.lat;
    let bottom = map.getBounds()._southWest.lat;

    for(let i=0; i<markerCount; i++){
        let lat = Math.random() * (bottom - top) + top;
        let lng = Math.random() * (right - left) + left;

        L.marker([lat,lng]).addTo(map);
    }
}

const main = () => {
    let lat = 45.523064;
    let lng = -122.676483;
    let zoom = 3;
    
    const myMap = generateMap(lat,lng,zoom);
    generateMarkers(myMap, 10);
}

main();