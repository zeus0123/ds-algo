function bubbleSort(array) {
    for(let i = array.length -1; i > 0; i--) {
        for(let j = 0; j < i; j++) {
            if(array[j] > array[j + 1]) {
                let temp = array[j+1];
                array[j+1] = array[j];
                array[j] = temp;
            }
        }
    }
    console.log(array)
    return array;
}

bubbleSort([4,2,6,5,1,3])