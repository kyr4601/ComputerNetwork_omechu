

add1 = document.querySelector('#btn1');
add2 = document.querySelector('#btn2');
add3 = document.querySelector('#btn3');
add4 = document.querySelector('#btn4');
Container = document.querySelector('.res-box');

add1.addEventListener('click', function(){   
    axios("/ko", {
        method: "get",
        })
         .then((response) => {
          
          food.innerText = response.data.name;
          })
         .catch((error) => {
           console.log(error);
         }); 
  
       
})

add2.addEventListener('click', function(){    
    axios("/jp", {
        method: "get",
        })
         .then((response) => {
          
          food.innerText = response.data.name;
          })
         .catch((error) => {
           console.log(error);
         }); 
})

add3.addEventListener('click', function(){    
    axios("/us", {
        method: "get",
        })
         .then((response) => {
          
          food.innerText = response.data.name;
          })
         .catch((error) => {
           console.log(error);
         }); 
})

add4.addEventListener('click', function(){    
    axios("/ch", {
        method: "get",
        })
         .then((response) => {
          
          food.innerText = response.data.name;
          })
         .catch((error) => {
           console.log(error);
         }); 
})

