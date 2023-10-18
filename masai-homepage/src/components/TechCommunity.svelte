
<script>
  import { Button } from "flowbite-svelte";

    let images=[
        "https://masaischool.com/images/new-homepage/community/community1.webp",
        "https://masaischool.com/images/new-homepage/community/community2.webp",
        "https://masaischool.com/images/new-homepage/community/community3.webp",
        "https://masaischool.com/images/new-homepage/community/community4.webp",
        "https://masaischool.com/images/new-homepage/community/community5.webp",
        "https://masaischool.com/images/new-homepage/community/community6.webp",
        "https://masaischool.com/images/new-homepage/community/community7.webp",
        "https://masaischool.com/images/new-homepage/community/community8.webp",
        "https://masaischool.com/images/new-homepage/community/community9.webp",
        "https://masaischool.com/images/new-homepage/community/community10.webp",
        "https://masaischool.com/images/new-homepage/community/community11.webp",
        "https://masaischool.com/images/new-homepage/community/community12.webp",

    ]
</script>
<div class="max-w-full mx-auto mt-[20px]">
    <p class="font-[700] text-[34px] leading-[40px] font-poppins transition-[background-color,border-color,color,fill,stroke,opacity,box-shadow,transform] duration-200 text-center mx-auto mb-[16px] capitalize">
        Be a part of our thriving
        <br>
        <span class="text-[#ED0331] relative whitespace-nowrap isolate">
            tech community
            <img src="https://masaischool.com/images/new-homepage/yellow-vector.svg" alt="yellow-vector" class="absolute w-full md:w-[264px] bottom-[-8px] z-[10] h-[14px] md:h-[21px] left-0 right-0" style="">
        </span>
    </p>

</div>


<div class="slider">
   
    <div class="slide-track mt-10 " style="transform: translate3d(-3346.36px, 0px, 0px); transition-duration: 0ms;">
        {#each images as image (image)}
        <div class=" slide w-full h-[300px]  " style="width:361.818px; margin-right:10px;">
          
       <img alt="community" class="object-cover pointer-events-none " style="opacity: 1; transition: opacity 1200ms ease-out 0s;" src={image}>
           
        </div>
        {/each}
       
    </div>
</div>
<div class="md:flex items-center justify-center relative pt-[20px] max-w-[1440px] mx-auto mb-20">
    
    <div class="flex mb-[20px] md:mb-0 px-[16px] md:px-0 justify-end items-center gap-[8px] md:absolute right-[80px] z-[3]">
      <button type="button" w="32px" h="32px" as="button" colorscheme="red" minw="32px !important" class="rounded-[0.375rem]  hover:bg-[#FEDFE5] border-[1px] border-[currentColor]  justify-center items-center !font-[600] text-[14px] leading-[24px] font-sans tracking-[1.25px] uppercase p-[12px_16px] inline-block focus:!ring-0 outline-offset-[5px] outline-[1px] outline-[transparent] focus-visible:!shadow-[0_0_0_3px_rgba(66,_153,_225,_0.6)] disabled:opacity-[0.6] disabled:cursor-not-allowed transition-[background-color,border-color,color,fill,stroke,opacity,box-shadow,transform] duration-200 w-[32px] text-[#ED0331] h-[32px] min-w-[32px] !p-0 curved-swiper-button-prev1">
        <div>
          <svg width="24" height="24" fill="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
            <path d="M15.41 16.58L10.83 12L15.41 7.41L14 6L7.99997 12L14 18L15.41 16.58Z" fill="currentColor"></path>
          </svg>
        </div>
      </button>
      <button type="button" class=" rounded-[0.375rem]  hover:bg-[#FEDFE5] border-[1px] border-[currentColor] justify-center items-center !font-[600] text-[14px] leading-[24px] font-sans tracking-[1.25px] uppercaseinline-block focus:!ring-0 outline-offset-[5px] outline-[1px] outline-[transparent] focus-visible:!shadow-[0_0_0_3px_rgba(66,_153,_225,_0.6)] disabled:opacity-[0.6] disabled:cursor-not-allowed transition-[background-color,border-color,color,fill,stroke,opacity,box-shadow,transform] duration-200 w-[32px] text-[#ED0331] h-[32px] min-w-[32px] !p-0 curved-swiper-button-next1">
        <div>
          <svg width="24" height="24" fill="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
            <path d="M8.59003 16.58L13.17 12L8.59003 7.41L10 6L16 12L10 18L8.59003 16.58Z" fill="currentColor"></path>
          </svg>
        </div>
      </button>
    </div>
    <div class="text-center relative z-[2] flex-1">
      <a href="/" disabled="false" target="_blank" class="active:!ring-0 p-3 bg-[#ED0331] hover:bg-red-600 rounded-[8px] text-white !font-[600] text-[14px] leading-[24px] font-sans tracking-[1.25px] uppercase  inline-block focus:!ring-0 outline-offset-[5px] outline-[1px] outline-[transparent] focus-visible:!shadow-[0_0_0_3px_rgba(66,_153,_225,_0.6)] disabled:opacity-[0.6] disabled:cursor-not-allowed transition-[background-color,border-color,color,fill,stroke,opacity,box-shadow,transform] duration-200">
        Join our community
      </a>
    </div>
  </div>
  

<style>
    .slider {
        overflow: hidden;
        
        margin:auto;
        position: relative;
        min-height: auto;
        display: grid;
        place-items: center;
    }
    .slide-track {
        display: flex;
        width: calc(250px*18);
        animation: scroll calc( 60s) linear infinite; /* Adjust animation duration based on the number of images */
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
        height:auto
    }

    @keyframes scroll {
        0% {
            transform: translateX(0);
        }
        100% {
            transform: translateX(calc(-250px * 5));
        }
    }
   
</style>