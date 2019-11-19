function normalize_units(units) {
    if(units == "miles" || units == "mi") {
        units = "mi";
    } else if(units == "feet" || units == "ft"){
        units = "ft";
    } else if(units == "yards" || units == "yrds"){
        units = "yd";
    } else if(units == "meters" || units == "m"){
        units = "m";
    } else if(units == "kilometers" || units == "km"){
        units = "km";
    } else if(units == "inches" || units == "in"){
        units = "in";
    } else {
        units = "";
    }

    return units
}

function units_to_meters(distance, units) {
    const u_to_m = {"in":0.0254, "ft":.3048, "km": 1609.34, "m":1, "mi":1609.34, "yd":0.9144};
    
    let new_dist = distance * u_to_m[units];

    return new_dist
};

function main(){
    const readline = require('readline-sync');
    let dist = 0;
    let units = "";

    while(true){
        let user_dist = parseInt(readline.question('Enter distance: '));

        if(user_dist){
            dist = user_dist;
            break;
        } else {
            console.log("That is not a valid number.\n");
        }
    }
    
    while(true){
        let user_unit = readline.question('Enter units: ');
        let result = normalize_units(user_unit);
        
        if(result != ""){
            units = result;
            break;
        } else {
            console.log("That is not a valid unit.\n");
        }
    }
    
    let to_m = units_to_meters(dist, units);
    
    console.log(`${dist} ${units} is ${to_m} meters`);
};

main();