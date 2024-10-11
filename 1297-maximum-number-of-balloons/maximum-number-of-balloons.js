/**
 * @param {string} text
 * @return {number}
 */
var maxNumberOfBalloons = function(text) {
    let balloon = {}
    for (letter of "balloon"){
        if (letter in balloon){
            balloon[letter]+=1
        }
        else{
            balloon[letter]=1
        }
    }
    let frequency = {}
    for (letter of text){
        if (letter in balloon){
            if(letter in frequency){
                frequency[letter]+=1
            }
            else{
                frequency[letter]=1
            }
        }
    }
    
    if (Object.keys(frequency).length!=Object.keys(balloon).length){
        return 0
    }
    let minimum = Infinity
    for (key of Object.keys(frequency)){
        if (frequency[key]<balloon[key]){
            return 0
        }
        minimum = Math.min(minimum,Math.floor(frequency[key]/balloon[key]))
    }
    return minimum
};