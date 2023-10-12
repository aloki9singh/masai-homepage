<script>
  import { Button } from "flowbite-svelte";
</script>

<div>
  <div class="w-full">
    <img
      src="https://masai-website-images.s3.ap-south-1.amazonaws.com/banner_h_1_3d43d26bd0.webp"
      alt="masai-banner"
    />
  </div>
  <div class="flex p-5">
    <div class="flex flex-col gap-5 w-2/3">
      <div class="text-5xl font-extrabold">
        <p class="py-2">Realise Your Potential</p>
        <p>
          With
          <span class="text-[#ed0331] relative">
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
        <Button class="bg-[#ed0331] p-3 uppercase tracking-widest text-lg">Get Your Dream Job</Button>
      </div>
    </div>
    <div class="w-1/2" />
  </div>
</div>
