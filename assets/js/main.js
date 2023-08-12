/*=============== SHOW MENU ===============*/
const navMenu = document.getElementById('nav-menu'),
    navToggele = document.getElementById('nav-toggle'),
    navClose = document.getElementById('nav-close')

/*====MENU SHOW====*/
/*validate if constant exists*/
if (navToggele) {
    navToggele.addEventListener('click', () => {
        navMenu.classList.add('show-menu')
    })
}

/*====MENU HIDDEN====*/
/*validate if constant exists*/
if (navClose) {
    navClose.addEventListener('click', () => {
        navMenu.classList.remove('show-menu')
    })
}

/*=============== REMOVE MENU MOBILE ===============*/
const navLink = document.querySelectorAll('.nav-link')

const linkAction = () => {
    const navMenu = document.getElementById('nav-menu')
    navMenu.classList.remove('show-menu')
}
navLink.forEach(n => n.addEventListener('click', linkAction))

/*=============== ADD BLUR TO HEADER ===============*/
const header = document.getElementById('header');
const handleScroll = () => {
    if (window.scrollY > 100) {
        header.classList.add('blur');
    } else {
        header.classList.remove('blur');
    }
};

// Attach the scroll event listener
window.addEventListener('scroll', handleScroll);


/*=============== EMAIL JS ===============*/

/*=============== SHOW SCROLL UP ===============*/
const scrollUp = () => {
    const scrollUp = document.getElementById('scroll-up');

    // Check if the page is scrolled down (scrollY is greater than 0)
    if (window.scrollY > 350) {
        scrollUp.classList.add('show-scroll');
    } else {
        scrollUp.classList.remove('show-scroll');
    }
};

window.addEventListener('scroll', scrollUp);

/*=============== SCROLL SECTIONS ACTIVE LINK ===============*/
const sections = document.querySelectorAll('section[id]')

const scrollActive = () => {
    const scrollY = window.pageYOffset

    sections.forEach(current => {
        const sectionHeight = current.offsetHeight,
            sectionTop = current.offsetTop - 58,
            sectionId = current.getAttribute('id'),
            sectionsClass = decument.querySelector('.nav__menu a[href*=' + sectionId + ']')

        if (scrollY > sectionTop && scrollY <= sectionTop + sectionHeight) {
            sectionsClass.classList.add('active-link')
        } else {
            sectionsClass.classList.remove('active-link')
        }
    })
}

window.addEventListener('scroll', scrollActive)
/*=============== SCROLL REVEAL ANIMATION ===== ==========*/
const sr = ScrollReveal({
    origin: 'top',
    distance: '60px',
    duration: 2500,
    delay: 200,
    reset: true
})

sr.reveal('.home__data, .home__social, .contact__container, .footer__container')
sr.reveal('.home__image', { origin: 'bottom' })
sr.reveal('.about__data', { origin: 'left' })
sr.reveal('.about__image', { origin: 'right' })
sr.reveal('.services__card', '.projects__card', { interval: 100 })
