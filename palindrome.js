/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    let newString = s.replace(/[^A-Za-z]/g, '').toLowerCase();
    if(newString.length === 0 || newString.length === 1)
        return true
    var flag=0;
    for(let i=0,j=newString.length-1;i<j;i++,j--){
        console.log(newString[i],newString[j])
        if(newString[i] !== newString[j]) {
            return false;
        } else {
            flag = 1;
        }
    }
    if(flag==1)
        return true
    else
        return false    
};

isPalindrome()