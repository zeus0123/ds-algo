/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function (strs) {

    const alpha = Array.from(Array(26)).map((e, i) => i + 65);
    let alphabet = alpha.map((x) => String.fromCharCode(x).toLowerCase());
    alphabet = alphabet.reduce((a, v) => ({ ...a, [v]: 0 }), {})

    let common = "";
    for (i = 0; i < strs.length; i++) {
        let current = strs[i];
        current = [...new Set(current.split(""))].join("");
        for (j = 0; j < current.length; j++) {
            Object.keys(alphabet).forEach((item, index) => {
                if (item === current[j]) {
                    alphabet[item] = alphabet[item] + 1;
                }
            })
        }

    }

    Object.keys(alphabet).forEach((item, index) => {
        if (alphabet[item] === strs.length) {
            common = common + item;
        }
    })

    return common;

};

longestCommonPrefix(["flower", "flow", "flight"])

// Common Characters;


const longestCommonPrefixTwo = (strs) => {
    // const firstItem = strs[0];
    // let firstItemObj = {};

    // let output = "";

    // for(i = 0; i < firstItem.length; i++) {
    //     firstItemObj[firstItem[i]] = 1;
    // }

    // for(j = 1; j < strs.length; j++) {
    //     let current = strs[j];
    //     current = [...new Set(current.split(""))].join("");
    //     for(k = 0; k < current.length; k++) {
    //         Object.keys(firstItemObj).forEach((item, index) => {
    //             if (item === current[k]) {
    //                 firstItemObj[item] = firstItemObj[item] + 1;
    //             }
    //         })
    //     }
        
    // }

    // let charArray = Object.keys(firstItemObj);

    // for(m = 0; m < charArray.length; m++) {
    //     console.log(firstItemObj[charArray[m]]);
    //     if (firstItemObj[charArray[m]] === strs.length) {
    //         output = output + charArray[m];
    //     } else {
    //         break;
    //     }
    // }   
   

    // console.log(firstItemObj);

    // console.log(output);

    // return output;

    let sorted = strs.sort((a,b) => a < b? -1:1);
    console.log(sorted);

    let output = []
    let firstword = sorted[0];
    console.log(firstword);
    let lastword = sorted[sorted.length -1];
    console.log(lastword);
    for (var i = 0; i < firstword.length; i++) {
        if (firstword[i] ==lastword[i] ){
            output.push(firstword[i])
        }else{       
            break
        }
   }


    return output.join("")
}

console.log(longestCommonPrefixTwo(["dog","racecar","car"]));