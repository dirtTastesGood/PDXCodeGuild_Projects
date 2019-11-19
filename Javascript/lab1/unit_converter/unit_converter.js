
function units_to_meters(distance, units) {
    const u_to_m = {"feet":.3048, "meters":1};
    
    let new_dist = distance * u_to_m[units];

    return new_dist
};

function main(){
    const readline = require('readline-sync');
    let dist = 0;
    let units = "feet";

    while(true){
        let user_dist = parseInt(readline.question('Enter distance in feet: '));

        if(user_dist){
            dist = user_dist;
            break;
        } else {
            console.log("That is not a valid number.\n");
        }
    }


    console.log(`${dist} ${units} is ${units_to_meters(dist, units)} meters`);


    let to_m = units_to_meters(dist, units);
    
};

main();