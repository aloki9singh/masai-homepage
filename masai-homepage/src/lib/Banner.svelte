<script>
  import { Button } from "flowbite-svelte";
  import Carousel from "./Carousel.svelte";
</script>

<div>
  <div class="w-full h-36">
    <div
  class="flex-row flex min-h-[196px] md:min-h-[198px] text-left p-[16px] rounded-[24px] absolute xl:max-w-[455px] left-[0px] xl:left-[-70%] z-1 bottom-[-40%] lg:bottom-[0px] xl:bottom-[40px]"
  style="box-shadow:0px 4px 7px 0px #BDBDBD40;background:linear-gradient(89.52deg, rgba(245, 245, 245, 0.322) 2.5%, rgba(255, 255, 255, 0.7) 99.54%)"
>
  <div>
    <img
      src="/images/new-homepage/quote-start.svg"
      alt="quote"
      class="mr-[4px] mt-[-18px] inline min-w-[19px]"
      style=""
    />
  </div>
  <div class="flex flex-col gap-[4px]">
    <div>
      <p
        class="!font-[600] text-[14px] leading-[24px] font-sans transition-[background-color,border-color,color,fill,stroke,opacity,box-shadow,transform] duration-200 !inline !text-[#21191B]"
      >
        I learnt a lot from Masai i.e discipline, time management and
        professionalism.
      </p>
      <img
        src="/images/new-homepage/quote-end.svg"
        alt="quote"
        class="mt-[-12px] inline min-w-[19px]"
        style=""
      />
    </div>
    <div class="flex-1 flex flex-col justify-end items-start gap-[5px]">
      <p
        class="!font-[400] text-[16px] leading-[24px] font-sans transition-[background-color,border-color,color,fill,stroke,opacity,box-shadow,transform] duration-200 undefined"
      >
        Salman Lukhman Shaikh
      </p>
      <img
        src="/images/new-homepage/company-logo4.svg"
        alt="company logo"
        class="mt-[4px] h-[32px]"
        style=""
      />
    </div>
  </div>
</div>
  </div>

  <div class="w-full">
    <img
      src="https://masai-website-images.s3.ap-south-1.amazonaws.com/banner_h_1_3d43d26bd0.webp"
      alt="masai-banner"
    />
  </div>
  <div class="flex p-5 justify-between items-center">
    <div class="flex flex-col gap-5 w-2/3">
      <div class="text-5xl font-extrabold">
        <p class="py-2">Realise Your Potential</p>
        <p>
          With
          <span class="text-[#ed0331] relative z-[-1]">
            Assured Outcomes
            <img
              alt="yellow-vector"
              src="https://www.masaischool.com/images/new-homepage/yellow-vector.svg"
              class="absolute z-[-1] bottom-[-3] left-0 w-full"
            />
          </span>
        </p>
        <p class="py-3">Delivered.</p>
      </div>
      <div>
        <p class="text-2xl p-0">India’s only outcome-based career institute.</p>
        <p class="text-2xl">Enter the tech workforce industry-ready.</p>
      </div>
      <div>
        <Button class="bg-[#ed0331] p-3 uppercase tracking-widest text-lg"
          >Get Your Dream Job</Button
        >
      </div>
    </div>
    <div class="w-full md:w-1/2 mx-auto p-4">
      <Carousel />
    </div>
  </div>
</div>

