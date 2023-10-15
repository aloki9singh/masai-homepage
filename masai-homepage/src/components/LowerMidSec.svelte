


<script>
  import Card from "./Card.svelte";
  import Certificate from "./Certificate.svelte";
  import ElevateSection from "./ElevateSection.svelte";
  import Footer from "./Footer.svelte";
  import StudentsImpact from "./StudentsImpact.svelte";
  import VideoCardScroll from "./VideoCardScroll.svelte";
  let  arr={img1:"https://masai-website-images.s3.ap-south-1.amazonaws.com/PR_Article_Prateek_Shukla_Gen_AI_92324e2d6b.jpeg",
  img2:"https://masai-website-images.s3.ap-south-1.amazonaws.com/PR_Thungy_1_420b226e5b.webp",
  img3:"https://masai-website-images.s3.ap-south-1.amazonaws.com/PR_Thingy_2_f2c52e6fcf.webp",heading1:"Empowering Education Through GenAI",heading2:"Masai School targets fivefold revenue growth in three years",heading3:"Beyond Degrees: Embracing Alternative Credentialing and Micro-learning in Tech Recruitment"}

</script>
<div>
    <!-- <VideoCardScroll/> -->
    <!-- <div class="grid grid-cols-3  ">
      <Card img={arr.img1}  heading={arr.heading1}/>
      <Card img={arr.img2} heading={arr.heading2}/>
      <Card img={arr.img3} heading={arr.heading3}/>
    </div> -->
    <!-- <HiringPartners/> -->
    <StudentsImpact/>
    <!-- --------Elevate section----------------------- -->
     <ElevateSection/>
    <!-- certificate -->
    <Certificate/>
  <!-- -------MAsai in news section---------------------------------- -->
    <h2 class="font-[700] text-[34px] leading-[40px] font-poppins transition-[background-color,border-color,color,fill,stroke,opacity,box-shadow,transform] duration-200 text-center py-5">Masai In <span class="!text-[#ED0331] relative whitespace-nowrap isolate">News
      <img src="https://masaischool.com/images/new-homepage/yellow-vector.svg" alt="yellow-vector" class="mx-auto absolute w-full md:w-[264px] bottom-[-5px] md:bottom-[-5px] z-[10] h-[14px] md:h-[21px] left-0 right-0" style=""></span></h2>
   <div class="mb-[32px] mt-[20px] w-[100%] false  ">
    <div class="news-section swiper !p-[16px]  swiper-initialized swiper-horizontal swiper-backface-hidden">
      <div class="swiper-wrapper false  flex " style="transform: translate3d(0px, 0px, 0px); transition-duration: 0ms;">
        <div class="swiper-slide w-full !h-auto overflow-hidden  swiper-slide-active" style="width: 448px; margin-right: 10px;">
          <div class="h-full">
         
              <div>
                <div class="min-h-[250px] flex items-center">
                 <img src="https://masai-website-images.s3.ap-south-1.amazonaws.com/PR_Article_Prateek_Shukla_Gen_AI_92324e2d6b.jpeg" alt="news" class="m-auto w-full max-h-[250px] object-cover object-center my-auto" style="">
                </div>
                  <h4 class="max-h-[84px] !text-[16.54px] mt-[33px] text-[#293241] md:!text-[20px] !font-poppins !font-[700] !leading-[23.15px] md:!leading-[28px] textOverflow">Empowering Education Through GenAI</h4>
                </div>
              </div> 
            </div>
                <div class="swiper-slide w-full !h-auto overflow-hidden  swiper-slide-next" style="width: 448px; margin-right: 10px;">
                  <div class="h-full" >
                   
                      <div><div class="min-h-[250px] flex items-center"> <img src="https://masai-website-images.s3.ap-south-1.amazonaws.com/PR_Thungy_1_420b226e5b.webp" alt="news" class="m-auto w-full max-h-[250px] object-cover object-center my-auto" style=""></div>
                       <h4 class="max-h-[84px] !text-[16.54px] mt-[33px] text-[#293241] md:!text-[20px] !font-poppins !font-[700] !leading-[23.15px] md:!leading-[28px] textOverflow">Masai School targets fivefold revenue growth in three years</h4>
                      </div>
                    
                  </div> 
                </div>
                <div class="swiper-slide w-full !h-auto overflow-hidden " style="width: 448px; margin-right: 10px;"><div class="h-full" >
                
                    <div>
                      <div class="min-h-[250px] flex items-center">
                         <img src="https://masai-website-images.s3.ap-south-1.amazonaws.com/PR_Thingy_2_f2c52e6fcf.webp" alt="news" class="m-auto w-full max-h-[250px] object-cover object-center my-auto" style="">
                        </div>
                         <h4 class="max-h-[84px] !text-[16.54px] mt-[33px] text-[#293241] md:!text-[20px] !font-poppins !font-[700] !leading-[23.15px] md:!leading-[28px] textOverflow">Beyond Degrees: Embracing Alternative Credentialing and Micro-learning in Tech Recruitment</h4>
                      </div>
                 
                  </div> 
                  </div>
                </div>  
              </div>
            </div>
      <!-- ---------------------------------------------------------- -->
</div>