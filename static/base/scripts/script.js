window.onload = function () {

    // *Animate fading in

    function y_offset_comparer(first_element, second_element) {
        if (first_element.offsetTop > second_element.offsetTop)
            return -1;
        else if (first_element.offsetTop == second_element.offsetTop)
            return 0;

        return 1;
    }


    function get_fade_in_elements() {
        var elements = document.getElementsByClassName("fade_in")

        // sort if necessary
        if (elements.length > 1)
            return (Array.prototype.slice.call(elements)).sort(y_offset_comparer);

        return elements

    }

    var animate_on_bottom_offset = 200;

    function fade_in(elements) {
        if (elements === null || elements == undefined || elements.length == 0)
            return;

        var screenBottom = window.pageYOffset + Math.max(document.documentElement.clientHeight, window.innerHeight || 0);

        while (elements.length !== 0 && (elements[elements.length - 1].offsetTop + animate_on_bottom_offset) <= screenBottom) {
            if (elements.length == 1) {
                var element_to_animate = elements[0];
                element_to_animate.classList.add("animation");
                element_to_animate.classList.remove("fade_in");
                break;
            } else
                var element_to_animate = elements.pop();

            element_to_animate.classList.add("animation");
            element_to_animate.classList.remove("fade_in");
        }

        return elements
    }

    fade_in(get_fade_in_elements());

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
        sticky_navbar_anim();
        fade_in(get_fade_in_elements());
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

                            // Clear fields
                            var fields = form_to_submit.getElementsByTagName("input");
                            var textarea = form_to_submit.getElementsByTagName("textarea");
                            textarea[0].value = "";
                            for (var i = 0; i < fields.length; i++) {
                                if (fields[i].getAttribute("name") !== "csrfmiddlewaretoken")
                                    fields[i].value = "";
                            }
                            // Delete errors
                            var error;
                            while (error = document.querySelector(".error"))
                                error.parentNode.removeChild(error);
                        } else {
                            // If there is not errors
                            var field = document.getElementById(item)
                            if (field !== null && (field.nextSibling === null || !field.nextSibling.classList.contains("error"))) {
                                // Create element with text error and place it near appropriate input
                                var error = document.createElement("p");
                                error.classList.add("error");
                                error.innerText = json[item]
                                field.parentNode.insertBefore(error, field.nextSibling);
                            }
                        }

                    }
                },

                // handle a non-successful response
                error: function (xhr, errmsg, err) {
                    console.log(xhr.responseText)
                    console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
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

            if (duration !== undefined && duration !== null)
                element.onclick = function () {

                    if (element.dataset.anchor === undefined)
                        var end_position = 0;
                    else {
                        var anchor_obj = document.getElementById(element.dataset.anchor);
                        var end_position = anchor_obj.offsetTop;
                    }

                    var start_position = window.pageYOffset;
                    var distance = end_position - start_position;
                    var startTime = null

                    function animate(currentTime) {
                        if (startTime === null) {
                            startTime = currentTime;
                        }

                        var timeElapsed = currentTime - startTime;

                        var go_to = ease(timeElapsed, start_position, distance, duration);
                        window.scrollTo(0, go_to);

                        if (timeElapsed < duration)
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
}