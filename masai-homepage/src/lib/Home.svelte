<script>
  import { Button } from "flowbite-svelte";
  import Carousel from "./Carousel.svelte";
  import TextCarousel from "./TextCarousel.svelte";
</script>

<div>
  <div
    class="flex p-5 py-10 md:text-left text-center justify-between items-center relative md:flex-row flex-col md:text-auto"
  >
    <div class="flex flex-col gap-5 w-2/3">
      <div class="md:text-5xl lg:text-4xl text-2xl font-extrabold">
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
        <p class="  md:text-2xl p-0">
          India’s only outcome-based career institute. <span
            class="block md:hidden"
            >Enter the tech workforce industry-ready.</span
          >
        </p>
        <p class=" md:block hidden md:text-2xl">
          Enter the tech workforce industry-ready.
        </p>
      </div>
      <div>
        <Button class="bg-[#ed0331] p-3 uppercase tracking-widest text-lg"
          >Get Your Dream Job</Button
        >
      </div>
    </div>
    <div class="md:w-5/12 mx-auto p-4">
      <Carousel />
    </div>
    <div class="w-4/12 top-72 md:block hidden right-80 absolute h-[200px]">
      <TextCarousel />
    </div>
  </div>
</div>
