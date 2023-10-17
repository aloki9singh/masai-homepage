<script>
  import { Button } from "flowbite-svelte";
// https://www.masaischool.com/images/new-homepage/curriculum-style/star.svg
// https://www.masaischool.com/images/new-homepage/curriculum-style/bulb.svg
// https://www.masaischool.com/images/new-homepage/curriculum-style/check.svg
// https://www.masaischool.com/images/new-homepage/curriculum-style/certificate.svg
// https://www.masaischool.com/images/new-homepage/curriculum-style/graduate.svg

</script>
<p class="md:text-3xl text-2xl font-[700] text-center z-[-1] hidden md:block">
    <span class="z-[-10]">Best-In-Class</span>
    <span class="text-[#ed0331] relative z-[-1]">
        Curriculum
        <img
            alt="yellow-vector"
            src="https://www.masaischool.com/images/new-homepage/yellow-vector.svg"
            class="absolute bottom-[-3] left-0"
        />
    </span>
    <span class="z-[-10]">&</span>
    <span class="text-[#ed0331] relative z-[-1]">
        Pedagogy
        <img
            alt="yellow-vector"
            src="https://www.masaischool.com/images/new-homepage/yellow-vector.svg"
            class="absolute bottom-[-3] left-0"
        />
    </span>
</p>
<div class="w-11/12  md:hidden mx-auto p-3 bg-[#6e71cc] rounded-xl">
    <div class="flex justify-center items-center p-3 rounded-full mr-auto bg-white w-1/4 mx-auto mb-5">
        <img src="https://www.masaischool.com/images/new-homepage/curriculum-style/graduate.svg" alt="graduate-svg">
    </div>
    <p class="text-2xl font-extrabold text-white text-center" >Best In-Class Curriculum & Pedagogy</p>
</div>
<div class="w-full relative">
    <div class="w-full md:h-[450px] mt-8 md:px-20 px-5 md:overflow-scroll">
        <div class="md:w-5/12 w-full">
            <div class='w-full md:mb-52 mb-6 box-shadow p-3 rounded-md text-center md:text-left md:shadow-none'>
                <img src="https://www.masaischool.com/images/new-homepage/curriculum-style/laptop.svg" alt="laptop-svg" class='mx-auto md:hidden'>
                <h3 class="md:text-2xl  text-lg font-[700] md:mb-8 mb-4 z-[-10]">100% <span class="text-[#ed0331]">Live</span>  Distance Learning</h3>
                <p class='tmd:ext-md text-sm'>India’s Only Live Tech-Learning Course With Tier 1 Instructors. Get Real-Time Feedback, Interactive Sessions & A Personalised Learning Experience.</p>
            </div>
            <div class='w-full md:mb-52 mb-6 box-shadow p-3 rounded-md text-center md:text-left md:shadow-none'>
                <img src="https://www.masaischool.com/images/new-homepage/curriculum-style/star.svg" alt="laptop-svg" class='mx-auto md:hidden'>
                <h3 class="md:text-2xl text-lg font-[700] md:mb-8 mb-4 z-[-10]">Generative <span class="text-[#ed0331]">AI Integrated</span> Program</h3>
                <p class='md:text-md text-sm'>Harness & Implement The Power Of AI In Coding & Data Analytics. What’s More? Use Custom AI Tools To Enhance Placement Preparation.</p>
            </div>
            <div class='w-full md:mb-52 mb-6 box-shadow p-3 rounded-md text-center md:text-left md:shadow-none'>
                <img src="https://www.masaischool.com/images/new-homepage/curriculum-style/bulb.svg" alt="laptop-svg" class='mx-auto md:hidden'>
                <h3 class="md:text-2xl text-lg font-[700] md:mb-8 mb-4 z-[-10]"> <span class="text-[#ed0331]">Industry Ready</span> Curriculum</h3>
                <p class='md:text-md text-sm'> Our Curriculum Is Regularly Updated Through Industry Feedback. In-Demand Specialisations Are Added To Aid Our Students Launch Sustainable Careers.</p>
            </div>
            <div class='w-full md:mb-52 mb-6 box-shadow p-3 rounded-md text-center md:text-left md:shadow-none'>
                <img src="https://www.masaischool.com/images/new-homepage/curriculum-style/check.svg" alt="laptop-svg" class='mx-auto md:hidden'>
                <h3 class="md:text-2xl text-lg font-[700] md:mb-8 mb-4 z-[-10]">Focus On Learning <span class="text-[#ed0331]">Agility</span></h3>
                <p class='md:text-md text-sm'>We Prioritise Flexible Thinking & Continuous Skill Development. Stay Nimble In An Ever-Changing World By Embracing Adaptability, Curiosity & Rapid Learning.</p>
            </div>
            <div class='w-full md:mb-52 mb-6 box-shadow p-3 rounded-md text-center md:text-left md:shadow-none'>
                <img src="https://www.masaischool.com/images/new-homepage/curriculum-style/certificate.svg" alt="laptop-svg" class='mx-auto md:hidden'>
                <h3 class="md:text-2xl text-lg font-[700] md:mb-8 mb-4 z-[-10]">Industry Ready In Just <span class="text-[#ed0331]">25 - 35 Weeks</span></h3>
                <p class='md:text-md text-sm'>Curriculum At Masai Is Designed To Be Intensive & Extensive. With Our Unique Pedagogy Learn Right In Less Time. All We Ask Is Your Dedication!</p>
            </div>
        </div>
        <div class='hidden md:block'>
            <img src="https://www.masaischool.com/images/new-homepage/curriculum-style/course-image5.webp" class="h-[450px] w-5/12 absolute bottom-2 right-20 rounded-2xl z-[-2]" alt="pedagogy">
        </div>
    </div>
</div>

<div>
     <div class="m-auto w-7/12 flex justify-center items-center p-5">
    <Button class="bg-[#ed0331] uppercase tracking-wide p-3"
      >GET YOUR DREAM JOB</Button
    >
  </div>
</div>
<style>
    .box-shadow{
        box-shadow: rgba(0, 0, 0, 0.02) 0px 1px 3px 0px, rgba(27, 31, 35, 0.15) 0px 0px 0px 1px;
    }
    @media (min-width:728px){
        .box-shadow{
            box-shadow: none;
        }
    }
</style>

