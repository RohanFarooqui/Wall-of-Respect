$(document).ready(function () {

    //-> Set Values
    function set_values(id) {

        //->  Remove & Set Smoke 
        let smoke_path ="../static/Visitor Page/Img/smoke.png";
        $('#smoke').fadeOut(250, function(){
            $('#smoke').attr("src",smoke_path);
            $('#smoke').fadeIn(250);
        });

        //->  Get & Set Image 
        let img_path = document.getElementById(id).src;
        $('#featured').fadeOut(500, function() {
            $('#featured').attr("src",img_path);
            $('#featured').fadeIn(500);
        });

        //-> Get & Set Name + Signature
        let Name = document.getElementsByClassName(id + " Name")[0].innerText;
        $('#Associate_Name').fadeOut(500, function() {
            $('#Associate_Name').text(Name);
            $('#Associate_Name').fadeIn(500);
        });
        $('#Associate_Signature').fadeOut(500, function() {
            $('#Associate_Signature').text(Name);
            $('#Associate_Signature').fadeIn(500);
        });
        


        //->  Get & Set Campaign
        let Campaign = document.getElementsByClassName(id + " Campaign")[0].innerText;
        $('#Associate_Campaign').fadeOut(500, function() {
            $('#Associate_Campaign').text(Campaign);
            $('#Associate_Campaign').fadeIn(500);
        });





        //-> Get & Set Description
        let Description = document.getElementsByClassName(id + " Descripton")[0].innerText;
        $('#Associate_Description').fadeOut(500, function() {
            $('#Associate_Description').text(Description);
            $('#Associate_Description').fadeIn(500);
        });

        //-> Get & Set Quote
        let Quote = document.getElementsByClassName(id + " Quote")[0].innerText;
        $('#Associate_Quote').fadeOut(500, function() {
            $('#Associate_Quote').text(Quote);
            $('#Associate_Quote').fadeIn(500);
        });

    }

    //-> Variables Define 
    var $st = $('.pagination'); /* Slick Variable */
    var $slickEl = $('.center'); /* Slick Variable */


    $slickEl.on('init reInit afterChange', function (event, slick, currentSlide, nextSlide) {
        var i = (currentSlide ? currentSlide :0) + 1;
        $st.text(i + ' of ' + slick.slideCount);
        
        if(currentSlide == null){
            set_values(1);
        }

        id_of_Center_img(currentSlide);


    });

    $slickEl.slick({
        centerMode: true,
        centerPadding: '100px',
        slidesToShow: 9,
        focusOnSelect: true,
        autoplay:false, /*true*/
        autoplaySpeed:6000,
        pauseOnHover: true,
        dots: false,
        infinite: true,
        prevArrow: false,
        nextArrow: false,
        mobileFirst: false,
        responsive: [
            {
                breakpoint: 1100,
                settings: "unslick"
            },
            {
                breakpoint: 1101,
                settings: {
                    arrows: false,
                    centerMode: true,
                    //centerPadding: '40px',
                    slidesToShow: 1,
                }
            },
            /*{
                breakpoint: 480,
                settings: {
                    arrows: false,
                    centerMode: true,
                    centerPadding: '40px',
                    slidesToShow: 1
                }
            }*/
        ]
    });

    //--> Controls
    //-> Next slide button
    $('.next-image').click(function () {
        $slickEl.slick('slickNext');
    });

    //-> Prev slide button
    $('.prev-image').click(function () {
        $slickEl.slick('slickPrev');
    });

    //-> Featured Image 
    function id_of_Center_img(id) {
        if (id == null) {
            let id =1;
            set_values(id);
        }
        else { 
            id = id+1;
            set_values(id); 
        }
    }

    //=> Event Listener Check Browser Size Continously
    /*window.addEventListener("resize", function () {
        if ($(document).width() < 1100) {
            $slickEl.slick("unslick");
            console.log("FF");
        }
        else {
            $slickEl.slick("slick");
            console.log("ON");
        }
    });

    //-> Check Size of Screen on Load
    window.addEventListener('load', function() {
        if ($(document).width() < 1101) {
            $slickEl.slick("unslick");
            console.log("FF "+$(document).width());
        }
        else {
            $slickEl.slick("slick");
            console.log("ON");
        }        
        
    });*/
    
    


});










