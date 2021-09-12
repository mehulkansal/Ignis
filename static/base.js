$(".like__button").click(function (e) {
    if ($(`.${e.target.classList[2]}`)[0].innerHTML == 'favorite_border') {
        $(`.${e.target.classList[2]}`)[0].innerHTML = 'favorite'
        $(`.${e.target.classList[2]}`).addClass('add-color')
    }
    else {
        $(`.${e.target.classList[2]}`)[0].innerHTML = 'favorite_border'
        $(`.${e.target.classList[2]}`).removeClass('add-color')
    }
})