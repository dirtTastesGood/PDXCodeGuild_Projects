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

function unitsToMeters(distance, conversion_rate) {

    let new_dist = distance * conversion_rate;

    return new_dist
};

function metersToUnits(distance, conversion_rate){
    new_dist = distance / conversion_rate

    return new_dist
}



function main(){
    const readline = require('readline-sync');
    let dist = 0;
    let units = "";
    const u_to_m = {"in":0.0254, "ft":.3048, "km": 1609.34, "m":1, "mi":1609.34, "yd":0.9144};
    
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

    while(true){
        let user_unit2 = readline.question('Enter units: ');
        let result2 = normalize_units(user_unit2);
        
        if(result2 != ""){
            units2 = result2;
            break;
        } else {
            console.log("That is not a valid unit.\n");
        }
    }

    let conversion_rate = u_to_m[units];
    let to_m = unitsToMeters(dist, conversion_rate);
    let to_u = metersToUnits(to_m, conversion_rate);
    console.log(`${dist} ${units} is ${to_u} ${units2}`);
};

main();