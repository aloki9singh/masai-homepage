
<script>

    const images=[
        "https://masai-website-images.s3.ap-south-1.amazonaws.com/paytm_a5c1ce2bc6.svg",
        "https://masai-website-images.s3.ap-south-1.amazonaws.com/whitehat_5a86f1e308.svg",
        "https://masai-website-images.s3.ap-south-1.amazonaws.com/bharatpe_a3a5a3f552.svg",
        "https://masai-website-images.s3.ap-south-1.amazonaws.com/swiggy_bc1b88842e.svg",
        "https://masai-website-images.s3.ap-south-1.amazonaws.com/salesken_baefe048ac.svg",
        "https://masai-website-images.s3.ap-south-1.amazonaws.com/vyapar_3f3770ebb5.svg",
        "https://masai-website-images.s3.ap-south-1.amazonaws.com/capgemini_31a863e94f.svg",
        "https://masai-website-images.s3.ap-south-1.amazonaws.com/simplilearn_f8af8de923.svg",
        "https://masai-website-images.s3.ap-south-1.amazonaws.com/pagarbook_2746958f65.svg",
        "https://masai-website-images.s3.ap-south-1.amazonaws.com/smallcase_1740bcc33f.svg",
        "https://masai-website-images.s3.ap-south-1.amazonaws.com/bharatagri_d4794042fe.svg",
        "https://masai-website-images.s3.ap-south-1.amazonaws.com/sharechat_23a9923a34.svg",
        "https://masai-website-images.s3.ap-south-1.amazonaws.com/leapfinance_0d785d05eb.svg",
        "https://masai-website-images.s3.ap-south-1.amazonaws.com/ola_15b5ee2b82.svg",
        "https://masai-website-images.s3.ap-south-1.amazonaws.com/ibm_795b5429ee.svg",
        "https://masai-website-images.s3.ap-south-1.amazonaws.com/byjus_e7b97a9c80.svg",
        "https://masai-website-images.s3.ap-south-1.amazonaws.com/ajio_a16cd7a85b.svg",
        "https://masai-website-images.s3.ap-south-1.amazonaws.com/svgviewer_png_output_38_4421638b42.png",
        "https://masai-website-images.s3.ap-south-1.amazonaws.com/globallogic_c30eb641f7.svg",
        "https://masai-website-images.s3.ap-south-1.amazonaws.com/eatfit_9dc276a187.svg",
        "https://masai-website-images.s3.ap-south-1.amazonaws.com/dream11_d6c8d97a52.svg",
        "https://masai-website-images.s3.ap-south-1.amazonaws.com/homelane_e9cadd0c3c.svg",
        "https://masai-website-images.s3.ap-south-1.amazonaws.com/moneytap_d5a6c9d532.svg",
        "https://masai-website-images.s3.ap-south-1.amazonaws.com/urbanpiper_2884348a0b.svg",
        "https://masai-website-images.s3.ap-south-1.amazonaws.com/airmeet_93e45faced.svg",
     
    ]
</script>



<div class="max-w-[1440px] mx-auto text-center">
    <p class="font-[700] text-[34px] leading-[40px] font-poppins transition-[background-color,border-color,color,fill,stroke,opacity,box-shadow,transform] duration-200 text-center mx-auto mb-[16px] capitalize">
        Meet our
        <span class="!text-[#ED0331] relative whitespace-nowrap isolate">
            4000+
            <img loading="lazy" alt="yellow-vector" class="mx-auto absolute w-full md:w-[264px] bottom-[-5px] md:bottom-[-8px] z-[10] h-[14px] md:h-[21px] left-0 right-0" style="opacity: 1; transition: opacity 1200ms ease-out 0s;" src="https://masaischool.com/images/new-homepage/yellow-vector.svg">
        </span>
        <span class="font-[700] text-[34px] leading-[40px] font-poppins transition-[background-color,border-color,color,fill,stroke,opacity,box-shadow,transform] duration-200 inline text-center mx-auto mb-[16px] capitalize">
            hiring partners
        </span>
    </p>
</div>

<div class="slider">
    <div class=" slide-track flex gap-[8px] md:gap-[16px] justify-around jusify-center p-[40px] overflow-auto">
   
        {#each images as image (image)}
        <div class="slide bg-white px-[4px] overflow-hidden mx-[8px] md:mx-[16px] w-[200px]  rounded-[24px] flex items-center justify-center" style="box-shadow: 0px 0px 13px #B6BEFC"> 
            <img src={image} alt="ajio.svg" style="">
        </div>
        {/each}
        <!-- {#each images as image (image)}
        <div class="slide bg-white px-[4px] overflow-hidden mx-[8px] md:mx-[16px] w-[200px]  rounded-[24px] flex items-center justify-center" style="box-shadow: 0px 0px 13px #B6BEFC"> 
            <img src={image} alt="ajio.svg"   style="">
        </div>
        {/each} -->
    </div>
</div>

 
<style>
    .slider {
        overflow: hidden;
        width: calc(100% * 30 );
        margin:auto;
        position: relative;
        width:90%;
        height: auto;
        display: grid;
        place-items: center;
    }
    .slide-track {
        display: flex;
        width: calc(250px*18);
        animation: scroll calc( 40s) linear infinite; /* Adjust animation duration based on the number of images */
    }
    .slide-track:hover {
        animation-play-state: paused;
    }
    /* .slide{
       height: 100px;
       width: 350px;
    } */
    img{
        width: 100%;
    }

    @keyframes scroll {
        0% {
            transform: translateX(0);
        }
        100% {
            transform: translateX(calc(-250px * 9));
        }
    }
    /* @media (min-width:768px) and (max-width:1024px){
        .slider {
        overflow: hidden;
        width: calc(100% *10 );
    }
    } */
</style>