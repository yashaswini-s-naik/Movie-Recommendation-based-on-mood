// Mood Card Selection
const cards = document.querySelectorAll('.mood-card');
cards.forEach(card => {
    card.addEventListener('click', () => {
        cards.forEach(c => c.classList.remove('active'));
        card.classList.add('active');
        card.querySelector('input').checked = true;
    });
});

// Confetti Animation on Movies Page
window.addEventListener('load', function(){
    if(document.querySelector('.movie-grid')){
        createConfetti(100);
    }
});

function createConfetti(count){
    for(let i=0;i<count;i++){
        let confetti = document.createElement('div');
        confetti.classList.add('confetti-piece');
        confetti.style.left = Math.random()*100 + "vw";
        confetti.style.backgroundColor = randomColor();
        confetti.style.animationDuration = 2 + Math.random()*3 + "s";
        confetti.style.width = 5 + Math.random()*10 + "px";
        confetti.style.height = confetti.style.width;
        document.body.appendChild(confetti);
        setTimeout(()=>{ confetti.remove(); }, 5000);
    }
}

function randomColor(){
    const colors = ["#ff595e","#ffca3a","#8ac926","#1982c4","#6a4c93"];
    return colors[Math.floor(Math.random()*colors.length)];
}
