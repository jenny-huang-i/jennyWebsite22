var body = document.getElementsByTagName("body")[0];
var container = document.getElementsByClassName("tabsContainer")[0];

var ogBot = container.getBoundingClientRect().bottom
window.addEventListener("scroll", function(event) {
    if(body.scrollTop > container.getBoundingClientRect().bottom)
    {
        console.log('hi')
        container.classList.add('stick');
    }
    // else if(body.scrollTop <= ogBot)
    // {
    //     container.classList.remove('stick');
    // }  

});
