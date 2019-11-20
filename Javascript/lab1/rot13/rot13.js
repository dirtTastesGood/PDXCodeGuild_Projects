function rotateString(str, offset){
    let abc = "abcdefghijklmnopqrstuvwxyz";
    let ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

    offset = offset % abc.length;

    let abcLeft = abc.slice(0, offset);
    let abcRight = abc.slice(offset, abc.length);
    
    let ABCLeft = ABC.slice(0, offset);
    let ABCRight = ABC.slice(offset, ABC.length);

    let abcRotated = abcRight + abcLeft;
    let ABCRotated = ABCRight + ABCLeft;
    
    strArr = str.split('');

    for(let i=0; i<strArr.length; i++){
        if(strArr[i].match(/([A-Z])/)){
            let index = ABC.indexOf(strArr[i]);
            let newChar = ABCRotated[index];
            strArr[i] = newChar;

        } else if(strArr[i].match(/([a-z])/)){            
            let index = abc.indexOf(strArr[i]);            
            let newChar = abcRotated[index];
            strArr[i] = newChar;
        }
    }
    return strArr.join('');
};

function main(){
    const readline = require('readline-sync');

    let userString = readline.question("Please enter a string: ");
    let rotation = parseInt(readline.question("Please enter the rotation: "));

    console.log(`Rotated: ${rotateString(userString, rotation)}`);

};

main();