// Sort binary array in linear time

// Input:  { 1, 0, 1, 0, 1, 0, 0, 1 }
 
// Output: { 0, 0, 0, 0, 1, 1, 1, 1 }


const sortArray = arr => {
    const length = arr.length;

    let j = -1;
    for(let i = 0; i < length; i++) {
        if(arr[i] < 1) {
            j++;
            console.log(j);
            let temp = arr[j];
            console.log(temp);
            arr[j] = arr[i];
            console.log(arr[j]);
            arr[i] = temp;
            console.log(arr[i])
        }
    }

    console.log(arr);
}

sortArray([1, 0, 1, 0, 1, 0, 0, 1 ]);