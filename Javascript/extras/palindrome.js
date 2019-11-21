
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
    console.log(isPalindrome("t a  co cat"));
    console.log(isPalindrome("t a  co cadt"));
    console.log(isPalindrome("A nut for a jar of tuna"));
    



}

main();