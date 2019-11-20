function rotateString(str, offset){
    let abc = "abcdefghijklmnopqrstuvwxyz";
    
    offset = offset % abc.length;

    let abcLeft = abc.slice(0, offset);
    let abcRight = abc.slice(offset, abc.length);
    
    let abcRotated = abcRight + abcLeft;
    
    strArr = str.split('');

    for(let i=0; i<strArr.length; i++){
        if(strArr[i].match(/([a-zA-Z])/)){
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