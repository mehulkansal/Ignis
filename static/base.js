$(".like__button").click(function (e) {
    const id = e.target.classList[2].split('-')[1]
    if ($(`.${e.target.classList[2]}`)[0].innerHTML == 'favorite_border') {
        $(`.${e.target.classList[2]}`)[0].innerHTML = 'favorite'
        $(`.${e.target.classList[2]}`).addClass('add-color')

        $.ajax({
            type: 'GET',
            url: `/post/like/${id}/`,
            success: function (response) {
                console.log(response)
                if (response['status']) {
                    console.log('liked')
                }
            },
            error: function (err) {
                console.log(err)
            }
        })

    }
    else {
        $(`.${e.target.classList[2]}`)[0].innerHTML = 'favorite_border'
        $(`.${e.target.classList[2]}`).removeClass('add-color')

        $.ajax({
            type: 'GET',
            url: `/post/unlike/${id}/`,
            success: function (response) {
                console.log(response)
                if (response['status']) {
                    console.log('disliked')
                }
            },
            error: function (err) {
                console.log(err)
            }
        })
    }
})