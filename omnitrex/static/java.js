document.addEventListener('DOMContentLoaded', function() {
    const images = [
        '../static/upgrade.jpg',
        '../static/heatblast.jpg',
        '../static/diamondhead.jpg',
        '../static/xlr8.jpg',
        '../static/greymatter.png',
        '../static/fourarms.jpg',
        '../static/stinkfly.jpg',
        '../static/wp.png',
        '../static/ghostfreak.jpg'
    ];

    let currentImageIndex = 0;
    const button = document.querySelector('.button');
    const menuButton = document.getElementById('menuButton');
    const sidebar = document.getElementById('sidebar');

    function playSoundAndTransform() {
        new Audio('https://www.myinstants.com/media/sounds/omnitrix-transform.mp3').play();
        currentImageIndex = (currentImageIndex + 1) % images.length;
        const nextImage = images[currentImageIndex];
        button.style.backgroundImage = `url('${nextImage}')`;
        console.log('Button clicked!');
        button.style.transform = 'rotate(45deg)';
        setTimeout(() => {
            button.style.transform = 'rotate(0deg)';
        }, 300);
    }

    function openNav() {
        console.log('openNav called');
        sidebar.style.width = '250px';
    }

    function closeNav() {
        console.log('closeNav called');
        sidebar.style.width = '0';
    }

    if (button) {
        button.addEventListener('click', playSoundAndTransform);
    }
    if (menuButton) {
        menuButton.addEventListener('click', openNav);
    }
    window.closeNav = closeNav; // Make closeNav available globally
});
