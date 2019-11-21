function isAnagram(string1, string2){

    string1 = string1.toLowerCase().replace(/\s/g, '');
    string2 = string2.toLowerCase().replace(/\s/g, '');

    string1 = string1.split('');

    while(true){
        let char1 = string1.pop();
        let index = string2.indexOf(char1);

        if(index < 0){
            return false
        } else {
            let char2 = string2[string2.indexOf(char1)];

            string2 = string2.replace(char2, '');

            if(string2 === ''){
                return true
            } else {
                isAnagram(string1.join(''), string2);
            }
        }
    }
}

function main(){
    const anagramStrings = [["i am lord voldemort","tom marvolo riddle"], ["you are a wizard harry", "welcome to hogwarts"], ["Hippogrif", "Dragon"], ["Arthur Weasely", "We salute harry"]]

    for(let i=0; i<anagramStrings.length; i++){
        let curStrings = anagramStrings[i];
        let result = isAnagram(curStrings[0], curStrings[1]);
        let msg = "";
        if(result == true){
            msg = `\n\"${curStrings[1]}\" is an anagram of \"${curStrings[0]}\"`;
        } else {
            msg = `\n\"${curStrings[1]}\" is not an anagram of \"${curStrings[0]}\"`;
        }

        console.log(msg);
        
    }
}

main();