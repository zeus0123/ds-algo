var removeDuplicates = function(nums) {
    let k = 0;
    let output = [];
    console.log(nums)
    for (i = 0; i < nums.length; i++) {
        console.log(nums[i])
        if(output.length === 0) {
            output.push(nums[i])
        } else if(!output.includes(nums[i])) {
            output.push(nums[i])
        }
    }

    console.log(output)

    return output
};

console.log(removeDuplicates([0,0,1,1,1,2,2,3,3,4]));