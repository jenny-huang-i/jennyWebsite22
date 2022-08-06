

var typingTexts = document.getElementsByClassName("typingText");

var tts = document.getElementsByClassName('tt');
window.addEventListener("scroll", function(event) {

   for(var i = 0; i < typingTexts.length; i++)
   {
    console.log('d');
    if(isInViewport(typingTexts[i]))
    {
        tts[i].classList.add('typingTextAnimation');
    }
   }
    
    

});

function isInViewport(element) {
    const rect = element.getBoundingClientRect();
    return (
        rect.top >= 0 &&
        rect.left >= 0 &&
        rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
        rect.right <= (window.innerWidth || document.documentElement.clientWidth)
    );
}