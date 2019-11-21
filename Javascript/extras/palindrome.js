
function isPalindrome(aString, index=0){
    aString = aString.replace(/\s/g, '').toLowerCase();

    while(true){
        let first = index;
        let last = aString.length-(index+1);
        if(aString[first] === aString[last]){
            aString = aString.slice(first+1, last);
            index++;
            
            if(aString.length <= 1){
                return true
            }

            isPalindrome(aString, index);
        } else {
            return false
        }
    }
}

function main(){
    const readline = require('readline-sync');

    while(true){

        userString = readline.question('Enter a word or phrase to check if it is a palindrome (enter \'q\' to quit): ');

        if(userString.toLowerCase() === 'q'){
            break
        } else {
            let palindrome = isPalindrome(userString);

            let msg;
            palindrome ?  msg = "is a palindrome." : msg = "is not a palindrome.";

            console.log(`\n\"${userString}\" ${msg}`)
        }
    }

}

main();