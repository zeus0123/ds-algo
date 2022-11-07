// Find a pair with the given sum in an array

// Input:
 
// nums = [8, 7, 2, 5, 3, 1]
// target = 10
 
// Output:
 
// Pair found (8, 2)
// or
// Pair found (7, 3)
 
 
// Input:
 
// nums = [5, 2, 6, 8, 1, 9]
// target = 12
 
// Output: Pair not found

// Solution


const findPair = (arr, target) => {
    let pair;

    for(i = 0; i < arr.length; i++) {
        for(j = i + 1; j < arr.length; j++) {
            if(arr[i] + arr[j] === target) {
                pair = [arr[i], arr[j]];
                console.log(pair)
                return pair;
            }
        }
    }

    return "Pair Not Found";
}

const hashMapApproach = (arr, target) => {
    let hashMap = {},
      results = []

        for (let i = 0; i < arr.length; i++){
            if (hashMap[arr[i]]){
                results.push([hashMap[arr[i]], arr[i]])
            }else{
                console.log(target - arr[i])
                // Find the next pair by subtracting it from the target
                hashMap[target - arr[i]] = arr[i];
                console.log(hashMap)
            }
          }
          return results;
}

console.log(hashMapApproach([8, 7, 2, 5, 3, 1], 10))
findPair([5, 2, 6, 8, 1, 9], 12)