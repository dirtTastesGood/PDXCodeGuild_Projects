
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

        let marker = L.marker([lat,lng]).addTo(map);

        marker.addEventListener('click', () => {
            let latLng = marker.getLatLng();
            
            getWeather(latLng.lat, latLng.lng, marker);
        });
    }
}

const buildPopup = (response='error', marker) => {
    console.log(response.data);
    let content;

    if(response.data){
        let latitude = response.data.coord.lat;
        let longitude = response.data.coord.lon;
        let temp = response.data.main.temp;
        let weather = response.data.weather[0].main;
    
        content = `Latitude: ${latitude}<br/>Longitude: ${longitude}<br/>Temperature: ${temp}&#8457;<br/>Weather: ${weather}`
    } else {
        content = 'Sorry, no data available';
    }

    marker.bindPopup(content).openPopup();
}

const getWeather = (lat, lng, marker) => {
    let url = `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lng}&units=imperial&appid=${open_weather_api_key}`
    
    axios.get(url)
    .then(response => {
        buildPopup(response, marker);
    })
    .catch(error => {
        buildPopup(error, marker);
    })
}

const main = () => {
    let lat = 45.523064;
    let lng = -122.676483;
    let zoom = 2;
    
    const myMap = generateMap(lat,lng,zoom);
    generateMarkers(myMap, 10);
}

main();