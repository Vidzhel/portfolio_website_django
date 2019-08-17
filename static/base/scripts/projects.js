window.addEventListener("DOMContentLoaded", function () {


    // Get loaded projects and overall projects count
    var projects_container = document.getElementById("projects");
    var overall_projects_count = projects_container.dataset.projects_count;
    var loaded_projects = (projects_container.getElementsByClassName("project_item")).length;

    // Hide button if all projects are loaded
    if (overall_projects_count - loaded_projects <= 0) {
        var load_more_button = document.getElementById("load_more");
        load_more_button.style.cssText = "visibility: hidden;";
    }

    function create_projects(projects_info) {
        var projects_container = document.getElementsByClassName("projects");

        // Get all active tags
        var section_nav = document.querySelector(".section_nav")
        var active_tags = section_nav.querySelectorAll(".tag.active");

        var active_tags_list = new Array();
        Array.prototype.forEach.call(active_tags, element => {
            active_tags_list.push(element.innerText.toUpperCase());
        })

        Array.prototype.forEach.call(projects_info, element => {

            var container = document.createElement("div");
            container.classList.add("project_item");
            container.classList.add("hidden");

            // container.classList.add("fade_in");
            if (element.in_progress)
                container.classList.add("in_progress");

            var tags_list = new String()

            Array.prototype.forEach.call(element.tags, tag => {
                var tag = tag[0];
                if (active_tags_list.includes(tag.toUpperCase()))
                    tags_list += '<div class="tag active"><a href="#">' + tag + '</a></div> ';
                else
                    tags_list += '<div class="tag"><a href="#">' + tag + '</a></div> ';

            });

            project_item = '\
                    <div class="read_more">\
                        <div class="button"><a href="' + element.alias + '">Read more</a></div>\
                    </div>\
                    <img class="lazyload"\
                        src="{% static "base/images/placeholder.jpg" %}"\
                        data-src="' + element.img + '" alt="project_image">\
                    <div class="project_item_content">\
                        <div class="title">' + element.title + '</div>\
                        <div class="summary">' + element.description + '</div>\
                        <div class="bottom_line">\
                            <div class="left">\
                                <div class="project_tags">' + tags_list + '</div>\
                            </div>\
                            <div class="right">\
                                <a rel="nofollow" href="' + element.code_source + '" class="hoverable"><i class="fab fa-github-square fa-lg"></i></a>\
                            </div>\
                        </div>\
                    </div>'


            container.innerHTML = project_item;
            $(".projects").append(container);

            $(function () {
                $(".hidden").animate({
                    opacity: 1
                }, {
                    duration: 500,
                    queue: false
                });
                $(".hidden").animate({
                    "margin-top": "15px"
                }, {
                    duration: 500,
                    specialEasing: {
                        "margin-top": "easeOutCirc"
                    },
                    queue: false
                });
            });

            lazyload();


        });

        // Add event to new tags
        var tags = (document.getElementsByClassName("projects"))[0].getElementsByClassName("tag");

        for (var i = 0; i < tags.length; i++) {
            tags[i].addEventListener("click", function (event) {
                filterByTag(event);
            });
        }
    }

    // * Filter
    var token = document.querySelector("[name='csrfmiddlewaretoken']");

    function sendFilterRequest(page = 0) {
        var section_nav = document.querySelector(".section_nav")
        var active_tags = section_nav.querySelectorAll(".tag.active");
        var category = section_nav.querySelector(".category.active").innerText;

        var tags = new Array()
        Array.prototype.forEach.call(active_tags, element => {
            tags.push((element.getElementsByTagName("a"))[0].innerText);
        });

        $.ajax({
            url: "/portfolio/", // the endpoint
            type: "POST", // http method
            dataType: "json",
            data: {
                csrfmiddlewaretoken: token.getAttribute("value"),
                page: page,
                tags: JSON.stringify(tags),
                category: JSON.stringify(category)
            },

            // handle a successful response
            success: function (json) {
                // If it's first page Delete old project items

                if (page === 0) {
                    var projects_container = (document.getElementsByClassName("projects"))[0];
                    // Create new project items from filtered info
                    projects_container.innerHTML = "";

                    // Get loaded projects and overall projects count
                    var projects_container = document.getElementById("projects");
                    var overall_projects_count = (json[0])["projects_count"]
                    projects_container.dataset.projects_count = overall_projects_count
                    var loaded_projects = (projects_container.getElementsByClassName("project_item")).length + json.length;

                    if (overall_projects_count - loaded_projects > 0) {
                        var load_more_button = document.getElementById("load_more");
                        load_more_button.style.cssText = "";
                    } else {
                        var load_more_button = document.getElementById("load_more");
                        load_more_button.style.cssText = "visibility: hidden;";
                    }

                }
                create_projects(json);

            },

            // handle a non-successful response
            error: function (xhr, errmsg, err) {
                console.log(xhr.responseText)
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }
        });

    }

    // * Tags control

    var tags = document.getElementsByClassName("tag");

    function filterByTag(event) {

        target = event.path[1];
        if (target.classList.contains("active")) {
            target.classList.remove("active");

            for (var y = 0; y < tags.length; y++)
                if (target.innerText == tags[y].innerText)
                    tags[y].classList.remove("active");

        } else {

            target.classList.add("active");

            for (var z = 0; z < tags.length; z++)
                if (target.innerText == tags[z].innerText)
                    tags[z].classList.add("active");
        }

        sendFilterRequest()
    }
    // On click select or deselect all tags with the same inner text and send get request
    for (var i = 0; i < tags.length; i++) {
        tags[i].addEventListener("click", function (event) {
            filterByTag(event);
        });
    }
    // * Categories control

    var categories = document.getElementsByClassName("category");

    // On click select category and send get request
    for (var i = 0; i < categories.length; i++) {

        categories[i].addEventListener("click", function (event) {
            target = event.path[0];
            if (!target.classList.contains("active")) {
                for (var y = 0; y < categories.length; y++)
                    categories[y].classList.remove("active");

                target.classList.add("active");
                sendFilterRequest()
            }
        });

    }

    // *PAGINATION

    var load_more_button = document.getElementById("load_more");

    load_more_button.onclick = function () {
        load_more_projects()
    }

    var PAGINATION_PAGE_NUM = 9;

    function load_more_projects() {

        // Get loaded projects and overall projects count
        var projects_container = document.getElementById("projects");
        var overall_projects_count = projects_container.dataset.projects_count;
        var loaded_projects = (projects_container.getElementsByClassName("project_item")).length;

        // If there are projects that can be loaded than send request
        if (overall_projects_count - loaded_projects > 0) {
            page = Math.floor(loaded_projects / PAGINATION_PAGE_NUM);

            sendFilterRequest(page);

            if (overall_projects_count - loaded_projects - PAGINATION_PAGE_NUM <= 0)
                load_more_button.style.cssText = "visibility: hidden;";
        }
    }

});