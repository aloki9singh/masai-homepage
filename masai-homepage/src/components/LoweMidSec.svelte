


<script>
  import Card from "./Card.svelte";
  import Footer from "./Footer.svelte";
  import VideoCardScroll from "./VideoCardScroll.svelte";
  let  arr={img1:"https://masai-website-images.s3.ap-south-1.amazonaws.com/PR_Article_Prateek_Shukla_Gen_AI_92324e2d6b.jpeg",
  img2:"https://masai-website-images.s3.ap-south-1.amazonaws.com/PR_Thungy_1_420b226e5b.webp",
  img3:"https://masai-website-images.s3.ap-south-1.amazonaws.com/PR_Thingy_2_f2c52e6fcf.webp",heading1:"Empowering Education Through GenAI",heading2:"Masai School targets fivefold revenue growth in three years",heading3:"Beyond Degrees: Embracing Alternative Credentialing and Micro-learning in Tech Recruitment"}

</script>
<div>
    <VideoCardScroll/>
    <div class="grid grid-cols-3  ">
      <Card img={arr.img1}  heading={arr.heading1}/>
      <Card img={arr.img2} heading={arr.heading2}/>
      <Card img={arr.img3} heading={arr.heading3}/>
    </div>
  
    <Footer/>
</div>