const sr = ScrollReveal({
    origin: 'top',
    distance: '60px',
    duration: 2500,
    delay: 200,
    reset: true
})

sr.reveal('.home_data, .homesocial, .contactcontainer, .footer_container')
sr.reveal('.home__image', { origin: 'bottom' })