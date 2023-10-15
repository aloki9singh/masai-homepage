<script>
  // Component Import
  import SignUp from "./lib/SignUp.svelte"
  import SignIn from "./lib/SignIn.svelte";
  import NavBar from "./lib/NavBar.svelte";
  import { Button,Drawer, CloseButton, Input, Label,Textarea, Heading } from "flowbite-svelte";
  import Footer from "./components/Footer.svelte";
  import Card from "./components/Card.svelte";
  import VideoCardScroll from "./components/VideoCardScroll.svelte";
  import LoweMidSec from "./components/LoweMidSec.svelte";
  
  let  arr={img1:"https://masai-website-images.s3.ap-south-1.amazonaws.com/PR_Article_Prateek_Shukla_Gen_AI_92324e2d6b.jpeg",
  img2:"https://masai-website-images.s3.ap-south-1.amazonaws.com/PR_Thungy_1_420b226e5b.webp",
  img3:"https://masai-website-images.s3.ap-south-1.amazonaws.com/PR_Thingy_2_f2c52e6fcf.webp",heading1:"Empowering Education Through GenAI",heading2:"Masai School targets fivefold revenue growth in three years",heading3:"Beyond Degrees: Embracing Alternative Credentialing and Micro-learning in Tech Recruitment"}
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
    <LoweMidSec/>
</main>

<style>

</style>
