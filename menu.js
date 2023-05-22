

add1 = document.querySelector('#btn1');
add2 = document.querySelector('#btn2');
add3 = document.querySelector('#btn3');
add4 = document.querySelector('#btn4');
Container = document.querySelector('.res-box');

add1.addEventListener('click', function(){    
    food.innerText = '한식!'
})

add2.addEventListener('click', function(){    
    food.innerText = '일식!'
})

add3.addEventListener('click', function(){    
    food.innerText = '양식!'
})

add4.addEventListener('click', function(){    
    food.innerText = '중식!'
})