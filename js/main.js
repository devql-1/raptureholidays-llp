(function ($) {
    "use strict";

    // Spinner
    var spinner = function () {
        setTimeout(function () {
            if ($('#spinner').length > 0) {
                $('#spinner').removeClass('show');
            }
        }, 1);
    };
    spinner(0);

    $('.carousel').carousel({
        interval: 4000,
        pause: 'hover'
    });

    function initOwlCarousel($carousel, options) {
        if ($carousel.data('owl.carousel')) {
            $carousel.trigger('refresh.owl.carousel');
        } else {
            $carousel.owlCarousel(options);
        }
    }

    // Scroll indicator
    $(window).scroll(function() {
        if ($(this).scrollTop() > 100) {
            $('.scroll-indicator').fadeOut('slow');
        } else {
            $('.scroll-indicator').fadeIn('slow');
        }
    });

    // Fade in elements on scroll
    function fadeInOnScroll() {
        var selectors = '.fade-in, ._aos-animate, .service-card-modern, .package-card-modern, .tour-modern-card, .packages-item, .testimonial-card';
        $(selectors).each(function () {
            var el = $(this);
            if (el.data('aos-animated') === true) {
                return;
            }
            var top = el.offset().top;
            var scroll = $(window).scrollTop();
            var height = el.outerHeight();
            var windowHeight = $(window).height();
            if (scroll + windowHeight > top + height / 4) {
                el.addClass('animate-fade-up').data('aos-animated', true);
            }
        });
    }

    $(window).scroll(fadeInOnScroll);
    fadeInOnScroll();

    // services carousel
    initOwlCarousel($(".services-carousel"), {
        autoplay: true,
        smartSpeed: 1000,
        center: false,
        dots: true,
        loop: true,
        margin: 25,
        nav: false,
        responsiveClass: true,
        responsive: {
            0:{
                items:1
            },
            576:{
                items:1
            },
            768:{
                items:2
            },
            992:{
                items:3
            },
            1200:{
                items:3
            }
        }
    });

    initOwlCarousel($(".InternationalTour-carousel"), {
        autoplay: true,
        smartSpeed: 1000,
        center: false,
        dots: true,
        loop: true,
        margin: 25,
        nav: false,
        responsiveClass: true,
        responsive: {
            0:{
                items:1
            },
            576:{
                items:1
            },
            768:{
                items:2
            },
            992:{
                items:3
            },
            1200:{
                items:3
            }
        }
    });

    // packages carousel
    initOwlCarousel($(".packages-carousel"), {
        autoplay: true,
        smartSpeed: 1000,
        center: false,
        dots: false,
        loop: true,
        margin: 25,
        nav : true,
        navText : [
            '<i class="bi bi-arrow-left"></i>',
            '<i class="bi bi-arrow-right"></i>'
        ],
        responsiveClass: true,
        responsive: {
            0:{
                items:1
            },
            768:{
                items:2
            },
            992:{
                items:2
            },
            1200:{
                items:3
            }
        }
    });

    // testimonial carousel
    initOwlCarousel($(".testimonial-carousel"), {
        autoplay: true,
        smartSpeed: 1000,
        center: true,
        dots: true,
        loop: true,
        margin: 25,
        nav : true,
        navText : [
            '<i class="bi bi-arrow-left"></i>',
            '<i class="bi bi-arrow-right"></i>'
        ],
        responsiveClass: true,
        responsive: {
            0:{
                items:1
            },
            768:{
                items:2
            },
            992:{
                items:2
            },
            1200:{
                items:3
            }
        }
    });

    $(window).on('load', function () {
        $('.owl-carousel').trigger('refresh.owl.carousel');
    });

    // Back to top button
    $(window).scroll(function () {
        if ($(this).scrollTop() > 300) {
            $('.back-to-top').fadeIn('slow');
        } else {
            $('.back-to-top').fadeOut('slow');
        }
    });
$('.back-to-top').click(function () {
        $('html, body').animate({scrollTop: 0}, 1500, 'easeInOutExpo');
        return false;
    });

    function getHashTarget(href) {
        try {
            return $(href);
        } catch (e) {
            return $();
        }
    }

    $('a[href^="#"]').filter(function () {
        var href = $(this).attr('href');
        return href && href !== '#' && !$(this).is('[data-bs-toggle]') && getHashTarget(href).length > 0;
    }).on('click', function(e) {
        var href = $(this).attr('href');
        var target = getHashTarget(href);
        if (target.length > 0) {
            e.preventDefault();
            $('html, body').animate({
                scrollTop: target.offset().top
            }, 800, 'easeInOutExpo');
        }
    });

    // Animated statistics counter
    $('.stats-number').each(function () {
        $(this).prop('Counter', 0).animate({
            Counter: $(this).text()
        }, {
            duration: 3000,
            easing: 'swing',
            step: function (now) {
                $(this).text(Math.ceil(now));
            }
        });
    });

    // Search bar animation
    $('.search-bar input').on('focus', function() {
        $(this).parent().addClass('shadow-lg');
    }).on('blur', function() {
        $(this).parent().removeClass('shadow-lg');
    });

    // Card hover tilt effect
    $('.service-card, .destination-card, .package-card').on('mousemove', function(e) {
        var x = e.pageX - $(this).offset().left;
        var y = e.pageY - $(this).offset().top;
        var rotateY = (x / $(this).width() * 20) - 10;
        var rotateX = (y / $(this).height() * 20) - 10;
        $(this).css('transform', 'perspective(1000px) rotateX(' + -rotateX + 'deg) rotateY(' + rotateY + 'deg) scale(1.02)');
    }).on('mouseleave', function() {
        $(this).css('transform', 'perspective(1000px) rotateX(0) rotateY(0) scale(1)');
    });

})(jQuery);

