window.onload = function () {
    // *Preloader
    var preloader = (document.getElementsByClassName("preloader"))[0];
    if (preloader != undefined && preloader != null)
        preloader.classList.add("done");

    function findAncestor(el, sel) {
        while ((el = el.parentElement) && !((el.matches || el.matchesSelector).call(el, sel)));
        return el;
    }

    // * Menu bar

    var menu = document.getElementById("menu");
    var main_nav = document.getElementsByClassName("main_nav")[0];

    if (menu != null)
        menu.addEventListener("mousedown", function () {
            if (main_nav.classList.contains("responsive")) {
                main_nav.classList.remove("responsive");

            } else {
                main_nav.classList.add("responsive");

            }
        });

    // *Sticky navbar

    window.onscroll = function () {
        sticky_navbar_anim()
    };

    var navbar = document.getElementsByClassName("fixed_nav");

    function sticky_navbar_anim() {
        if (navbar != null && navbar[0] != undefined) {

            if (window.pageYOffset > 0) {
                navbar[0].classList.add("nav_animation");
            } else {
                if (main_nav.classList.contains("responsive")) {
                    // close menu
                    main_nav.classList.remove("responsive");
                }

                navbar[0].classList.remove("nav_animation");
            }
        }
    }
    sticky_navbar_anim()

    // * Form submit

    var button = document.getElementById("submit_form");

    if (button !== undefined && button !== null) {
        var form_to_submit = document.getElementById("get_in_touch_form")
        var token = form_to_submit.querySelector("[name='csrfmiddlewaretoken']");

        button.onclick = function () {
            // form_to_submit.submit();
            $.ajax({
                url: "", // the endpoint
                type: "POST", // http method
                data: {
                    csrfmiddlewaretoken: token.getAttribute("value"),
                    sender_name: $('#sender_name').val(),
                    sender_email: $('#sender_email').val(),
                    subject: $('#subject').val(),
                    sender_message: $('#sender_message').val(),
                }, // data sent with the post request

                // handle a successful response
                success: function (json) {

                    for (var item in json) {

                        if (item === "success") {
                            var label = document.getElementById("success");
                            label.innerText = json[item];
                            var error;
                            while (error = document.querySelector(".error"))
                                error.parentNode.removeChild(error);
                        } else
                            // If there is not errors
                            if (document.getElementById(item).nextSibling === null || !document.getElementById(item).nextSibling.classList.contains("error")) {
                                // Create element with text error and place it near appropriate input
                                var error = document.createElement("p");
                                error.classList.add("error");
                                error.innerText = json[item]
                                document.getElementById(item).parentNode.insertBefore(error, document.getElementById(item).nextSibling);
                            }


                    }
                },

                // handle a non-successful response
                error: function (xhr, errmsg, err) {
                    console.log(xhr.responseText)
                    console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
                    console.log(errors)

                }
            });
        };
    }

    // * Smooth scrolling

    var scroll_buttons = document.getElementsByClassName("smooth_scroll");

    if (scroll_buttons !== null) {

        Array.prototype.forEach.call(scroll_buttons, element => {
            var anchor_point = element.dataset.anchor
            var duration = element.dataset.duration

            if (anchor_point !== undefined && anchor_point !== null && duration !== undefined && duration !== null)
                element.onclick = function () {
                    var anchor_obj = document.getElementById(element.dataset.anchor);

                    var start_position = window.pageYOffset;
                    var end_position = anchor_obj.offsetTop;
                    var distance = end_position - start_position;
                    var startTime = null

                    function animate(currentTime) {
                        if (startTime === null) {
                            startTime = currentTime;
                        }

                        var timeElepsed = currentTime - startTime;

                        var go_to = ease(timeElepsed, start_position, distance, duration);
                        window.scrollTo(0, go_to);

                        if (timeElepsed < duration)
                            requestAnimationFrame(animate)
                    }

                    function ease(t, b, c, d) {
                        t /= d / 2;
                        if (t < 1) return c / 2 * t * t * t + b;
                        t -= 2;
                        return c / 2 * (t * t * t + 2) + b;
                    }

                    requestAnimationFrame(animate);
                }
        });

    }

    // *Carousel animation

    var carousel_container = document.getElementsByClassName("carousel");

    function animate_carousel(slides, next_slide = null) {
        if (next_slide === null) {

            next_slide = 0;

            for (var i = 0; i < slides.length; i++) {
                if (slides[i].classList.contains("active"))
                    if (i + 1 < slides.length)
                        next_slide = i + 1;
                    else
                        next_slide = 0;

            }
        }

        for (var item of slides)
            if (item.classList.contains("passive"))
                item.classList.remove("passive");

        var change = false;
        for (var y = 0; i < slides.length; i++) {
            var item = slides[y];
            if (item.classList.contains("active") && !change) {
                slides[next_slide].classList.add("active");
                item.classList.add("passive");
                item.classList.remove("active");
                change = true;
            }
        }

    }

    // Set interval
    if (carousel_container !== null) {

        Array.prototype.forEach.call(carousel_container, element => {
            var carousel_items = element.getElementsByClassName("carousel_item");

            if (carousel_items !== null) {
                var slide_time = 0;

                if (element.dataset.slide_time === undefined)
                    slide_time = 6000;
                else
                    slide_time = element.dataset.slide_time;

                // Get set interval id and set it as data attr
                var id = setInterval(function () {
                    animate_carousel(carousel_items)
                }, slide_time);
                element.setAttribute("data-set_interval_id", id);
            }
        });

    }

    // Slide controll
    var slide_controlls = document.getElementsByClassName("slide_controll");

    Array.prototype.forEach.call(slide_controlls, element => {
        // findAncestor(slide)
        var carousel = element.closest(".carousel");
        var slides = carousel.getElementsByClassName("carousel_item");

        if (slides === null || carousel == null)
            new Error("wrong carousel_item location");

        // Which button has pressed
        var is_next_slide_controll = element.classList.contains("right");
        element.onclick = function () {

            clearInterval(carousel.dataset.set_interval_id);
            if (is_next_slide_controll)
                animate_carousel(slides);
            else {

                for (var i = 0; i < slides.length; i++)
                    if (slides[i].classList.contains("active")) {
                        var previous_slide_id = i - 1
                        break;
                    }

                if (previous_slide_id === undefined) {
                    if (element.dataset.slide_time === undefined)
                        slide_time = 6000;
                    else
                        slide_time = element.dataset.slide_time;


                    // Get set interval id and set it as data attr
                    var id = setInterval(function () {
                        animate_carousel(slides)
                    }, slide_time);
                    carousel.setAttribute("data-set_interval_id", id);
                    return;
                }

                if (previous_slide_id < 0)
                    previous_slide_id = slides.length - 1
                else if (previous_slide_id >= slides.length)
                    previous_slide_id = 0

                animate_carousel(slides, previous_slide_id);
            }

            if (element.dataset.slide_time === undefined)
                slide_time = 6000;
            else
                slide_time = element.dataset.slide_time;


            // Get set interval id and set it as data attr
            var id = setInterval(function () {
                animate_carousel(slides)
            }, slide_time);
            carousel.setAttribute("data-set_interval_id", id);
        };
    });


}