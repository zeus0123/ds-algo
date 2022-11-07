// Check if a subarray with 0 sum exists or not

// Input:  { 3, 4, -7, 3, 1, 3, 1, -4, -2, -2 }
 
// Output: Subarray with zero-sum exists
 
// The subarrays with a sum of 0 are:
 
// { 3, 4, -7 }
// { 4, -7, 3 }
// { -7, 3, 1, 3 }
// { 3, 1, -4 }
// { 3, 1, 3, 1, -4, -2, -2 }
// { 3, 4, -7, 3, 1, 3, 1, -4, -2, -2 }

let subWithZero = (arr) => {
    //create a new set
    const sumSet = new Set();
 
    // Traverse through array
    // and store prefix sums
    let sum = 0;
    for (let i = 0 ; i < arr.length ; i++)
    {
        sum += arr[i];
 
        // If prefix sum is 0
        // or it is already present
        if (sum === 0 || sumSet.has(sum))
            return sumSet;
 
        sumSet.add(sum);
    }
    return false;
   }

console.log(subWithZero([3, 4, -7, 3, 1, 3, 1, -4, -2, -2]));
[0,0,]