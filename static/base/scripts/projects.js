window.addEventListener("DOMContentLoaded", function () {

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
                        <div class="button"><a href="' + element.absolute_url + '">Read more</a></div>\
                    </div>\
                    <img class="lazyload"\
                        src="data:image/gif;base64,R0lGODlhCgAIAIABAN3d3f///yH5BAEAAAEALAAAAAAKAAgAAAINjAOnyJv2oJOrVXrzKQA7"\
                        data-src="' + element.img + '" alt="project_image">\
                    <div class="project_item_content">\
                        <div class="title">' + element.title + '</div>\
                        <div class="summary">' + element.about + '</div>\
                        <div class="bottom_line">\
                            <div class="left">\
                                <div class="project_tags">' + tags_list + '</div>\
                            </div>\
                            <div class="right">\
                                <a href="' + element.code_source + '" class="hoverable"><i class="fab fa-github-square fa-lg"></i></a>\
                            </div>\
                        </div>\
                    </div>'


            container.innerHTML = project_item;
            $(".projects").append(container);
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

    function sendFilterRequest() {
        var section_nav = document.querySelector(".section_nav")
        var active_tags = section_nav.querySelectorAll(".tag.active");
        var category = section_nav.querySelector(".category.active").innerText;

        var tags = new Array()
        Array.prototype.forEach.call(active_tags, element => {
            tags.push((element.getElementsByTagName("a"))[0].innerText);
        });

        $.ajax({
            url: "/portfolio/", // the endpoint
            type: "GET", // http method
            dataType: "json",
            data: {
                tags: JSON.stringify(tags),
                category: JSON.stringify(category)
            },

            // handle a successful response
            success: function (json) {
                // Delete all project items
                console.log(json)
                var projects_container = (document.getElementsByClassName("projects"))[0];
                // Create new project items from filtered info
                projects_container.innerHTML = "";
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
        // Trigger click to smooth scroll to the top
        (document.getElementsByClassName("projects")[0]).click();

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
});