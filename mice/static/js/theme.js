$(function () {
    "use strict";

    function e() {
        $(window).scroll(function () {
            $(this).scrollTop() > 300 ? $(".scroll-top").fadeIn() : $(".scroll-top").fadeOut()
        }), $(".scroll-top").click(function () {
            return $("html, body").animate({
                scrollTop: 0
            }, 800), !1
        }), $('.scroll-down[href^="#"], .scroll-to-target[href^="#"]').on("click", function (e) {
            e.preventDefault();
            var a = this.hash,
                i = $(a);
            $("html, body").stop().animate({
                scrollTop: i.offset().top
            }, 900, "swing", function () {
                window.location.hash = a
            })
        })
    }

    function a() {
        var e = $(window).scrollTop();
        $(window).height();
        // e > 0 ? $(".header").addClass("header-prepare") : $(".header").removeClass("header-prepare"), e > 0 ? $(".header").addClass("header-fixed") : $(".header").removeClass("header-fixed")
    }

    function i() {
        var e = $(window).height();
        $(".js-fullscreen-height").css("height", e)
    }

    function t() {
        function e() {
            var e = $(".fullscreen-carousel").find("li.flex-active-slide").attr("data-slide");
            "dark-slide" == e && ($("#header").addClass("header").removeClass("header-light"), $("#header").removeClass("header-default")), "light-slide" == e && ($("#header").addClass("header-light").removeClass("header-dark"), $("#header").removeClass("header-default")), "default-slide" == e && ($("#header").removeClass("header-dark"), $("#header").removeClass("header-light"), $("#header").addClass("header"))
        }

        function a() {
            $(window).width();
            var e = $(window).height();
            $(window).width() > 767 ? $(".hero-slider-1 .slides .js-Slide-fullscreen-height").css("height", e) : $(".hero-slider-1 .slides .js-Slide-fullscreen-height").css("height", "400px")
        }
        $(".fullscreen-carousel").length > 0 && $(".fullscreen-carousel").flexslider({
            animation: "slide",
            animationSpeed: 700,
            animationLoop: !1,
            slideshow: !1,
            easing: "swing",
            controlNav: !1,
            before: function (e) {
                $(".fullscreen-carousel .intro-content-inner").fadeOut().animate({
                    top: "80px"
                }, {
                        queue: !1,
                        easing: "easeOutQuad",
                        duration: 700
                    }), e.slides.eq(e.currentSlide).delay(400), e.slides.eq(e.animatingTo).delay(400)
            },
            after: function (a) {
                $(".fullscreen-carousel .flex-active-slide").find(".intro-content-inner").fadeIn(2e3).animate({
                    top: "0"
                }, {
                        queue: !1,
                        easing: "easeOutQuad",
                        duration: 1200
                    }), e()
            },
            start: function (a) {
                $("body").removeClass("loading"), e()
            },
            useCSS: !0
        }), a(), $(window).resize(function () {
            a()
        })
    }

    function o() {
        $(".fullwidth-slider").owlCarousel({
            slideSpeed: 400,
            singleItem: !0,
            autoHeight: !1,
            navigation: !0,
            autoPlay: !0,
            animationLoop: !0,
            slideshow: !0,
            pagination: !0,
            navigationText: ["<i class='fa fa-angle-left'></i>", "<i class='fa fa-angle-right'></i>"]
        }), $(".image-slider").owlCarousel({
            navigation: !0,
            pagination: !0,
            slideSpeed: 350,
            paginationSpeed: 400,
            singleItem: !0,
            navigationText: ["<i class='fa fa-angle-left'></i>", "<i class='fa fa-angle-right'></i>"],
            autoPlay: !1,
            autoHeight: !0,
            responsive: !0
        }), $(".testimonial-carousel").owlCarousel({
            autoPlay: !0,
            autoHeight: !0,
            stopOnHover: !0,
            singleItem: !0,
            slideSpeed: 350,
            pagination: !0,
            navigation: !1,
            navigationText: ["<i class='fa fa-angle-left'></i>", "<i class='fa fa-angle-right'></i>"]
        }), $(".team-carousel").owlCarousel({
            autoPlay: !0,
            stopOnHover: !0,
            items: 3,
            itemsDesktop: [1170, 3],
            itemsDesktopSmall: [1024, 2],
            itemsTabletSmall: [768, 1],
            itemsMobile: [480, 1],
            pagination: !1,
            navigation: !0,
            navigationText: ["<i class='fa fa-angle-left'></i>", "<i class='fa fa-angle-right'></i>"]
        }), $(".client-carousel").owlCarousel({
            autoPlay: 2500,
            stopOnHover: !0,
            items: 5,
            itemsDesktop: [1170, 4],
            itemsDesktopSmall: [1024, 3],
            itemsTabletSmall: [768, 2],
            itemsMobile: [480, 1],
            pagination: !1,
            navigation: !1,
            navigationText: ["<i class='fa fa-angle-left'></i>", "<i class='fa fa-angle-right'></i>"]
        }), $(".content-carousel").owlCarousel({
            autoPlay: !0,
            autoHeight: !0,
            stopOnHover: !0,
            singleItem: !0,
            slideSpeed: 500,
            pagination: !1,
            navigation: !0,
            navigationText: ["<i class='fa fa-angle-left'></i>", "<i class='fa fa-angle-right'></i>"],
            responsive: !0
        }), $(".item5-carousel").owlCarousel({
            autoPlay: 2500,
            stopOnHover: !0,
            items: 5,
            itemsDesktop: [1170, 3],
            itemsDesktopSmall: [1024, 2],
            itemsTabletSmall: [768, 1],
            itemsMobile: [480, 1],
            pagination: !0,
            navigation: !0,
            navigationText: ["<i class='fa fa-angle-left'></i>", "<i class='fa fa-angle-right'></i>"]
        }), $(".item4-carousel").owlCarousel({
            autoPlay: 2500,
            stopOnHover: !0,
            items: 4,
            itemsDesktop: [1170, 3],
            itemsDesktopSmall: [1024, 2],
            itemsTabletSmall: [768, 1],
            itemsMobile: [480, 1],
            pagination: !1,
            navigation: !0,
            navigationText: ["<i class='fa fa-angle-left'></i>", "<i class='fa fa-angle-right'></i>"]
        }), $(".item3-carousel").owlCarousel({
            autoPlay: !1,
            stopOnHover: !0,
            items: 3,
            itemsDesktop: [1170, 3],
            itemsDesktopSmall: [1024, 2],
            itemsTabletSmall: [768, 1],
            itemsMobile: [480, 1],
            pagination: !0,
            navigation: !0,
            navigationText: ["<i class='fa fa-angle-left'></i>", "<i class='fa fa-angle-right'></i>"]
        }), $(".item1-carousel").owlCarousel({
            autoPlay: !1,
            autoHeight: !0,
            stopOnHover: !0,
            singleItem: !0,
            slideSpeed: 350,
            pagination: !0,
            navigation: !0,
            navigationText: ["<i class='fa fa-angle-left'></i>", "<i class='fa fa-angle-right'></i>"],
            responsive: !0
        })
    }

    function n() {
        $(".slider-hero").owlCarousel({
            navigation: !0,
            slideSpeed: 700,
            paginationSpeed: 400,
            pagination: !0,
            addClassActive: !0,
            touchDrag: !0,
            singleItem: !0,
            navigationText: !1,
            autoPlay: !1,
            autoHeight: !1,
            beforeMove: function () {
                $(".slider-hero .overlay-hero .caption-hero").fadeOut(1)
            },
            afterMove: function () {
                $(".slider-hero .owl-item.active ").find(".caption-hero").delay(500).fadeIn(1500), BackgroundCheck.refresh()
            },
            afterInit: function () {
                $(".slider-hero .owl-item.active ").find(".caption-hero").delay(500).fadeIn(1500), BackgroundCheck.init({
                    targets: ".full-intro",
                    images: ".owl-carousel .item img"
                })
            }
        }), $(window).height(function () {
            function e() {
                var e = $(window).innerHeight();
                $(".slider-hero, .full-screen-intro").css("height", e)
            }
            e(), $(window).resize(function () {
                e()
            })
        })
    }

    // function l() {
    //     $(".video").mediaelementplayer({
    //         loop: !0,
    //         enableKeyboard: !1,
    //         iPadUseNativeControls: !1,
    //         pauseOtherPlayers: !1,
    //         iPhoneUseNativeControls: !1,
    //         AndroidUseNativeControls: !1,
    //         enableAutosize: !0
    //     }), $(".bg-video").mediaelementplayer({
    //         loop: !0,
    //         enableKeyboard: !1,
    //         iPadUseNativeControls: !1,
    //         pauseOtherPlayers: !1,
    //         iPhoneUseNativeControls: !1,
    //         AndroidUseNativeControls: !1,
    //         enableAutosize: !0,
    //         alwaysShowControls: !1
    //     }), $(".audio").mediaelementplayer({
    //         audioWidth: "100%",
    //         pauseOtherPlayers: !1
    //     }), $(".video, .audio, .post-media, .post-media iframe").fitVids()
    // }

    function s() {
        var e = $(".container-masonry");
        e.imagesLoaded(function () {
            e.isotope({
                itemSelector: ".nf-item",
                layoutMode: "masonry",
                masonry: {
                    columnWidth: 0,
                    gutter: 0
                }
            })
        }), $(".container-filter").on("click", ".categories", function () {
            var a = $(this).attr("data-filter");
            e.isotope({
                filter: a
            })
        });
        var a = $(".container-grid");
        a.imagesLoaded(function () {
            a.isotope({
                itemSelector: ".nf-item",
                layoutMode: "fitRows"
            })
        }), $(".container-filter").on("click", ".categories", function () {
            var e = $(this).attr("data-filter");
            a.isotope({
                filter: e
            })
        }), $(".categories-filter").each(function (e, a) {
            var i = $(a);
            i.on("click", ".categories", function () {
                i.find(".active").removeClass("active"), $(this).addClass("active")
            })
        }), $(".masonry").masonry({
            itemSelector: ".nf-item"
        })
    }

    function r() {
        $(".load-ele-fade").viewportChecker({
            classToAdd: "visible animated fadeIn",
            offset: 100,
            callbackFunction: function (e, a) { }
        }), $(function () {
            new WOW({
                boxClass: "wow",
                animateClass: "animated",
                offset: 0,
                mobile: !1,
                live: !0
            }).init()
        })
    }

    function c(e) {
        var a = $(window).scrollTop(),
            i = .5 * a,
            t = -.5 * a,
            o = a / $(".parallax").height();
        $(".parallax").hasClass("parallax-section1") && e.css("top", i), $(".parallax").hasClass("parallax-section2") && e.css("top", t), $(".parallax").hasClass("parallax-static") && e.css("top", 1 * a), $(".parallax").hasClass("parallax-opacity") && e.css("opacity", 1 - 1 * o), $(".parallax").hasClass("parallax-background1") && e.css("background-position", "left " + i + "px"), $(".parallax").hasClass("parallax-background2") && e.css("background-position", "left " + -i + "px")
    }

    function d() {
        $(".search-overlay-menu-btn").on("click", function (e) {
            $(".search-overlay-menu").addClass("open"), $('.search-overlay-menu > form > input[type="search"]').focus()
        }), $(".search-overlay-close").on("click", function (e) {
            $(".search-overlay-menu").removeClass("open")
        }), $(".search-overlay-menu, .search-overlay-menu .search-overlay-close").on("click keyup", function (e) {
            e.target != this && "search-overlay-close" != e.target.className && 27 != e.keyCode || $(this).removeClass("open")
        }), $(".cbox-gallary1").colorbox({
            rel: "gallary",
            maxWidth: "95%",
            maxHeight: "95%"
        }), $(".cbox-iframe").colorbox({
            iframe: !0,
            maxWidth: "95%",
            maxHeight: "95%",
            innerWidth: 640,
            innerHeight: 390
        }), $(".skillbar").each(function () {
            $(this).find(".skillbar-bar").animate({
                width: $(this).attr("data-percent")
            }, 2e3)
        }), $(".tipped").tipper(), $(".counter").each(function () {
            var e = $(this),
                a = e.attr("data-count");
            $({
                countNum: e.text()
            }).animate({
                countNum: a
            }, {
                    duration: 8e3,
                    easing: "linear",
                    step: function () {
                        e.text(Math.floor(this.countNum))
                    },
                    complete: function () {
                        e.text(this.countNum)
                    }
                })
        })
    }
    $(window).load(function () {
        $("#loader").fadeOut(), $("#preloader").delay(350).fadeOut("slow"), $("body").delay(350).css({
            overflow: "visible"
        }), s()
    }), $(document).ready(function () {
        t(), a(), i(), e(), n(), o(), s(), r(), d()
    }), $(window).resize(function () {
        a(), i()
    }), $(window).scroll(function () {
        a()
    }), $(".slide-bg-image, .bg-image").each(function (e) {
        $(this).attr("data-background-img") && $(this).css("background-image", "url(" + $(this).data("background-img") + ")")
    }), $(".parallax").each(function () {
        var e = $(this);
        $(window).scroll(function () {
            c(e)
        }), c(e)
    });
    var u;
    u = $(window).width() >= 1024 ? "position" : "transform", $(window).stellar({
        responsive: !0,
        positionProperty: u,
        horizontalScrolling: !1
    }), d(), $(".accordion-title").click(function (e) {
        $(this).next().slideToggle("easeOut"), $(this).toggleClass("active"), $("accordion-title").toggleClass("active"), $(".accordion-content").not($(this).next()).slideUp("easeIn"), $(".accordion-title").not($(this)).removeClass("active")
    }), $(".accordion-content").addClass("defualt-hidden"), $(function () {
        $(".tabs").tabs()
    }), $(function () {
        $("#range-slider").slider({
            range: !0,
            min: 0,
            max: 500,
            values: [0, 300],
            slide: function (e, a) {
                $(".price-amount-from").text("$" + a.values[0]), $(".price-amount-to").text("$" + a.values[1])
            }
        }), $(".price-amount-from").text("$" + $("#range-slider").slider("values", 0)), $(".price-amount-to").text("$" + $("#range-slider").slider("values", 1))
    })
});
