function countDown(num) {
    if(num <= 0) {
        console.log('Mind Blows');
        return;
    }

    console.log(num);
    num--;
    countDown(num);
}

countDown(5);