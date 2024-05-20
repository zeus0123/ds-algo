function insertionSort(array) {
    let temp;
    for(let i = 1; i < array.length; i++) {
        temp = array[i];
        console.log(temp, 'temp---')
        for(var j = i - 1; array[j] > temp && j > -1; j--) {
            console.log(j + 1, 'j ===');
            array[j + 1] = array[j];
            console.log(array[j], 'j--->')
        }
        console.log(j + 1, 'j >>>>');
        array[j + 1] = temp;
        console.log(array[j+1], 'j<<<<<')
        console.log("array ---->", array)
    }
    return array;
}

 

let myArray = [4,2,6,5,1,3];
insertionSort(myArray);
console.log(myArray);