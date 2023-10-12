<script>
  // Component Import
  import SignUp from "./lib/SignUp.svelte"
  import SignIn from "./lib/SignIn.svelte";
  import NavBar from "./lib/NavBar.svelte";
  import { Button,Drawer, CloseButton, Input, Label,Textarea } from "flowbite-svelte";
  
</script>

<main>
  <div
    class="w-full p-2 bg-[#fedfe5] flex justify-center items-center gap-3 sticky"
  >
    <p>Applications for our 6th November Batches are now open!</p>
    <Button class="bg-[#ed0331] uppercase tracking-wider">Apply Now</Button>
  </div>
  <NavBar/>
  <SignUp/>
  <SignIn/>
  <div class="w-full">
    <img
      src="https://masai-website-images.s3.ap-south-1.amazonaws.com/banner_h_1_3d43d26bd0.webp"
      alt="masai-banner"
    />
  </div>
  <div class='w-full'>
    <h1 class='text-center text-4xl font-extrabold'>Masai In <span class='text-[]'>News</span></h1>
    <div>
      <div>
        <img src="" alt="">
        <p></p>
      </div>
      <div>
        <img src="" alt="">
        <p></p>
      </div>
      <div>
      <img src="" alt="">
      <p></p>
      </div>
    </div>
  </div>
</main>

<style>

</style>
