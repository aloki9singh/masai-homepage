<script>
    import { Carousel } from 'flowbite-svelte';
  import CardDetail from './CardDetail.svelte';
  let name;
  let img1;
  let img2;
  let statement;
  let designation
    let details=[
        {
        statement:"Masai does a great job of attracting ambitious folk and it shows in the hunger with which the grads chase their own improvement and career advancement. The curriculum is shaped such that its graduates come into the job with with an understanding of workplace and technology practices that is simply missing from freshers hired from colleges. They continuously look for feedback for their curriculum and ensure that it is up to date with the pulse of the ecosystem. All of these have translated into a very smooth hiring experience for us with Masai. Our experience with Masai so far has led me to believe that its graduates would be good fits in startup culture.",
        img1:"https://masai-website-images.s3.ap-south-1.amazonaws.com/Arya_Adarsha_Gautam_a72b51d7b3.jpeg",
        name:"Arya Adarsha Gautam",
        designation:"CTO and Co-Founder -Pagarbook",
        img2:"https://masai-website-images.s3.ap-south-1.amazonaws.com/pagarbook_rect_adcdc345e4.svg"
    },
        {
        statement:"There are many platforms that bolster an individual's knowledge to show up to work and just do their tasks. But with Masai, it is quite evident that the individuals are given a well-rounded education into the different aspects besides programming that go into software engineering. The college curriculum while focusing on the theoretical aspects of programming hasn't really evolved to keep pace with the practical aspects of software engineering. Companies too can benefit significantly by sourcing developers from Masai as they have good familiarity with the tools and processes that go into building software solutions. The dominant trait amongst Masai graduates has mostly been to focus on gaining more knowledge",
        img1:"https://masai-website-images.s3.ap-south-1.amazonaws.com/Anirban_Majumdar_e001629fcc.jpeg",
        name:"Anirban Majumdar",
        designation:"CTO and Co-Founder -Urban Piper",
        img2:"https://masai-website-images.s3.ap-south-1.amazonaws.com/urbanpiper_rect_37c839e35e.svg"
    },
        {
        statement:"We were looking to hire entry-level developers and Masai more than delivered. Our selection rate from Masai's candidates is higher than other avenues of hiring and the process was completed in two days flat. The offer to joining ratio with Masai candidates was 100% which is awesome! The developers had a good foundation of the technologies they need to work with and could hit the ground running. We wholeheartedly recommend Masai to companies looking to hire entry-level developers quickly.",
        img1:"https://masai-website-images.s3.ap-south-1.amazonaws.com/Arya_Adarsha_Gautam_a72b51d7b3.jpeg",
        name:"Vamsee Mohan Kamabathula",
        designation:"CTO and Co-Founder -Qapita Fintech",
        img2:"https://masai-website-images.s3.ap-south-1.amazonaws.com/Qapita_13fe2db4fb.png"
    },
        {
        statement:"Hiring experience with Masai is a wow. All the candidates we interviewed were equally talented, selection wasn't easy. Masai training has made college and background irrelevant because once any student goes through the training the outcome is always good. We have also found that the students are trained even on soft skills, this covers the 360 degree needs of today's corporates or startups. In addition, Masai's one offer per candidate policy ensures students join once the offer is rolled out. Overall, we are confident that Masai is the new destination for quality and timely hiring.",
        img1:"https://masai-website-images.s3.ap-south-1.amazonaws.com/Pradeep_Sreeram_494522711e.jpeg",
        name:"Pradeep Sreeram",
        designation:"Engineering Lead -Eat.Fit",
        img2:"https://masai-website-images.s3.ap-south-1.amazonaws.com/eatfit_rect_02ec413e66.svg"
    },
       
]
    // Define an array of video URLs
    let videos = [
      'https://www.youtube.com/embed/tSlit0vgB20?si=Td9bmZJonS8XHUza',
      'https://www.youtube.com/embed/n0xIOjbNN0A?si=zXxLjSzsUNQ4BL4E',
      'https://www.youtube.com/embed/M18ivLdjZI0?si=kZzMHB2Jcq1Utbfh',
    ];
    function yourTransitionFunction(node, params) {
    // Define your custom transition logic here
    // For example, you can use the provided params to create transitions
    return{}
  }   


  let currentVideo = 0;

// Function to change the currently displayed video
function changeVideo(direction) {
  if (direction === 'next') {
    currentVideo = (currentVideo + 1) % videos.length;
  } else {
    currentVideo = (currentVideo - 1 + videos.length) % videos.length;
  }
}


  </script>

<div class="md:grid grid-cols-2">
    <div class="max-w-4xl flex p-5">
      <iframe
        class="rounded-[15px] my-2"
        width="560"
        height="315"
        src={videos[currentVideo]}
        title="YouTube video player"
        frameborder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
        allowfullscreen
      ></iframe>
    </div>
    <div>
        <div class="md:flex md:overflow-x-auto pt-5 gap-5 justify-center w-full">
            {#each details as detail (detail.name) }
              <div class="card-detail p-2 w-full justify-center  flex ">
                <CardDetail detail={detail} />
              </div>
            {/each}
          </div>
          <div>
            <div class="flex items-center pb-[10px] flex-wrap justify-between px-[16px] svelte-jnbt72">
              <a href="https://www.masaischool.com/blog/category/impact-stories/?_gl=1*ripovy*_ga*MTA2NjI4OTA3Mi4xNjc3MDQyMzQ2*_ga_GPPD2PTVSL*MTY5NzM0OTIxMi4yMS4xLjE2OTczNTEzMjYuNjAuMC4w" class="undefined !font-[600] text-[16px] leading-[24px] font-sans inline-block focus:!ring-0 outline-offset-[5px] outline-[1px] outline-[transparent] focus-visible:!shadow-[0_0_0_3px_rgba(66,_153,_225,_0.6)] disabled:opacity-[0.6] disabled:cursor-not-allowed transition-[background-color,border-color,color,fill,stroke,opacity,box-shadow,transform] duration-200 !p-0 text-[#ED0331] hover:underline"  target="_blank">Read More</a>
              <div class="flex justify-center gap-[8px] w-[fit-content]">
                <button type="button" class=" rounded-[0.375rem]   border-[1px] border-[currentColor]  justify-center items-center !font-[600] text-[14px] leading-[24px] font-sans tracking-[1.25px] uppercase inline-block focus:!ring-0 outline-offset-[5px] outline-[1px] outline-[transparent] focus-visible:!shadow-[0_0_0_3px_rgba(66,_153,_225,_0.6)] disabled:opacity-[0.6] disabled:cursor-not-allowed transition-[background-color,border-color,color,fill,stroke,opacity,box-shadow,transform] duration-200 company-review-card-prev text-[#ED0331] hover:text-white cursor-pointer !p-[4px] min-w-[auto] w-[32px] h-[32px] !bg-white active:!bg-[#CC032A] hover:!bg-[#ED0331] swiper-button-disabled" >
                  <div>
                    <svg width="24" height="24" fill="currentColor" viewBox="0 0 24 24" class="" xmlns="http://www.w3.org/2000/svg">
                      <path d="M15.41 16.58L10.83 12L15.41 7.41L14 6L7.99997 12L14 18L15.41 16.58Z" fill="currentColor"></path>
                    </svg>
                  </div>
                </button>
                <button type="button" class=" rounded-[0.375rem]   border-[1px] border-[currentColor]  justify-center items-center !font-[600] text-[14px] leading-[24px] font-sans tracking-[1.25px] uppercase inline-block focus:!ring-0 outline-offset-[5px] outline-[1px] outline-[transparent] focus-visible:!shadow-[0_0_0_3px_rgba(66,_153,_225,_0.6)] disabled:opacity-[0.6] disabled:cursor-not-allowed transition-[background-color,border-color,color,fill,stroke,opacity,box-shadow,transform] duration-200 company-review-card-next text-[#ED0331] hover:text-white cursor-pointer !p-[4px] min-w-[auto] w-[32px] h-[32px] !bg-white active:!bg-[#CC032A] hover:!bg-[#ED0331]">
                  <div>
                    <svg width="24" height="24" fill="currentColor" viewBox="0 0 24 24" class="" xmlns="http://www.w3.org/2000/svg">
                      <path d="M8.59003 16.58L13.17 12L8.59003 7.41L10 6L16 12L10 18L8.59003 16.58Z" fill="currentColor"></path>
                    </svg>
                  </div>
                </button>
              </div>
            </div>
          </div>
    </div>
  </div>
  

  
  <style>
    /* Add this in your component's style section or a global stylesheet */
    .card-detail {
      /* width: 375px; Set the desired width for each CardDetail */
      white-space: nowrap; /* Prevent content from wrapping */
      margin-right: 20px; /* Add space between CardDetails */
    }
  </style>