
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
    <div class="slide-track " style="transform: translate3d(-3346.36px, 0px, 0px); transition-duration: 0ms;">
        {#each images as image (image)}
        <div class=" slide w-full !h-auto  " style="width:361.818px; margin-right:10px;">
          
       <img alt="community" class="object-cover pointer-events-none " style="opacity: 1; transition: opacity 1200ms ease-out 0s;" src={image}>
           
        </div>
        {/each}
       
    </div>
     <div class="m-auto w-7/12 flex justify-center items-center p-5">
    <!-- <Button class="bg-[#ed0331] uppercase tracking-wide p-3"
      >View All Courses</Button> -->
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