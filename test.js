// Input - 1 0 0 2 1 0 2 1
// Output - 0 0 0 1 1 1 2 2

const findBestWay = (arr) => {
    // let temp = [...new Set(arr)];
    // console.log(temp);

    // let sort = arr.sort((a, b) => a - b); // O(n)
    // console.log(sort);

    // Convert array to Object
    const test = Object.assign({}, arr);
    console.log(test);
}

findBestWay([1, 0, 0, 2, 1, 0, 2, 1])
