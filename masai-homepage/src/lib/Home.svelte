<script>
  import { Button } from "flowbite-svelte";
  import Carousel from "./Carousel.svelte";
  import TextCarousel from "./TextCarousel.svelte";
</script>

<div>
  <div
    class="flex md:text-left text-center justify-between items-center relative md:flex-row flex-col md:text-auto"
  >
    <div class="flex flex-col gap-5 w-full py-5">
      <div class="md:text-5xl lg:text-4xl text-2xl font-extrabold w-full text-center lg:flex lg:flex-col lg:text-left">
        <span class="py-2 sm:inline">Realise Your Potential</span>
        <span>
          With
          <span class="text-[#ed0331] relative z-[-1]">
            Assured Outcomes
            <img
              alt="yellow-vector"
              src="https://www.masaischool.com/images/new-homepage/yellow-vector.svg"
              class="absolute z-[-1] bottom-[-3] left-0 w-full"
            />
          </span>
        </span>
        <span class="py-3 inline">Delivered.</span>
      </div>
      <div class="mt-3">
        <span class="md:text-2xl text-sm">
          India’s only outcome-based career institute. <span
            class="block md:hidden"
            >Enter the tech workforce industry-ready.</span
          >
        </span>
        <span class=" md:block hidden md:text-2xl">
          Enter the tech workforce industry-ready.
        </span>
      </div>
      <div>
        <Button class="bg-[#ed0331] p-3 uppercase tracking-widest lg:text-lg text-md"
          >Get Your Dream Job</Button
        >
      </div>
    </div>
    <div class="md:w-5/12 w-full mx-auto md:p-4">
      <Carousel />
    </div>
    <div class="md:w-4/12 w-11/12 md:top-60  md:right-72 top-3/4 right-5 absolute h-[200px] ">
      <TextCarousel />
    </div>
  </div>
</div>
 