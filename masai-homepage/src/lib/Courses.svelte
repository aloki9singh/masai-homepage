<script>
  import { Button } from "flowbite-svelte";
  import { CheckCircleSolid } from "flowbite-svelte-icons";
</script>

<div class='md:mt-20 mt-5'>
  <h1 class="md:text-5xl font-[700] text-2xl text-center pb-5">Our Courses</h1>
  <p class="md:text-3xl font-[700] text-xl text-center">
    Practice-Based Learning Tracks,
    <span class="text-[#ed0331] relative z-[-1]">
      Supercharged By A.I.
      <img
        alt="yellow-vector"
        src="https://www.masaischool.com/images/new-homepage/yellow-vector.svg"
        class="absolute z-[-1] bottom-[-3] left-0"
      />
    </span>
  </p>
  <div class="flex m-auto gap-5 md:w-9/12 w-full md:flex-row flex-col md:mt-10 mt-3">
    <div class="flex flex-col md:w-1/2 w-2/2 m-5 rounded-[15px] shadow-lg rounded-e">
      <div class="flex justify-center items-center bg-[#b7b8e5] py-8">
        <img
          src="https://masai-website-images.s3.ap-south-1.amazonaws.com/full_stack1_329d6b5595.png"
          alt="img-frontend"
          width="150px"
          height="150px"
        />
      </div>
      <div class="w-full p-4">
        <h5
          class="mb-2 text-xl font-semibold tracking-tight text-gray-900 dark:text-white"
        >
          Full Stack Web Development
        </h5>
        <p
          class="mb-2 font-normal text-gray-700 dark:text-gray-400 leading-tight"
        >
          Become job-ready in 30 weeks
        </p>
        <hr />
        <ul class="my-5 space-y-4 text-sm">
          <li class="flex space-x-2">
            <CheckCircleSolid
              class="w-4 h-4 rounded text-[#6fcd9e]  dark:text-primary-500"
            />
            <span
              class=" font-normal leading-tight text-gray-500 dark:text-gray-400"
            >
              Opportunities: Full Stack Developer, Software Engineer & much
              more.
            </span>
          </li>
          <li class="flex space-x-2">
            <CheckCircleSolid
              class="w-4 h-4 rounded text-[#6fcd9e]  dark:text-primary-500"
            />
            <span
              class=" font-normal leading-tight text-gray-500 dark:text-gray-400"
            >
              100% live learning with expert instructors.
            </span>
          </li>
          <li class="flex space-x-2">
            <CheckCircleSolid
              class="w-4 h-4 rounded text-[#6fcd9e]  dark:text-primary-500"
            />
            <span
              class=" font-normal leading-tight text-gray-500 dark:text-gray-400"
              >Pay After Placement
            </span>
          </li>
        </ul>
        <Button class="w-full bg-[#ed0331] uppercase tracking-wide p-3"
          >View Details</Button
        >
      </div>
    </div>
    <!-- Second Card -->
    <div class="flex flex-col md:w-1/2 m-5 rounded-[15px] shadow-lg rounded-e">
      <div class="flex justify-center items-center bg-[#e5c9b7] py-8">
        <img
          src="https://masai-website-images.s3.ap-south-1.amazonaws.com/backend_ea129d404e.png"
          alt="img-backend"
          width="150px"
          height="150px"
        />
      </div>
      <div class="w-full p-4">
        <h5
          class="mb-2 text-xl font-semibold tracking-tight text-gray-900 dark:text-white"
        >
          Backend Development
        </h5>
        <p
          class="mb-2 font-normal text-gray-700 dark:text-gray-400 leading-tight"
        >
          Become job-ready in 35 weeks
        </p>
        <hr />
        <ul class="my-5 space-y-4 text-sm">
          <li class="flex space-x-2">
            <CheckCircleSolid
              class="w-4 h-4 rounded text-[#6fcd9e]  dark:text-primary-500"
            />
            <span
              class=" font-normal leading-tight text-gray-500 dark:text-gray-400"
            >
              Opportunities: Backend Web Developer, API developer & much more.</span
            >
          </li>
          <li class="flex space-x-2">
            <CheckCircleSolid
              class="w-4 h-4 rounded text-[#6fcd9e]  dark:text-primary-500"
            />
            <span
              class=" font-normal leading-tight text-gray-500 dark:text-gray-400"
            >
              100% live learning with expert instructors.
            </span>
          </li>
          <li class="flex space-x-2">
            <CheckCircleSolid
              class="w-4 h-4 rounded text-[#6fcd9e]  dark:text-primary-500"
            />
            <span
              class=" font-normal leading-tight text-gray-500 dark:text-gray-400"
            >
              Pay After Placement
            </span>
          </li>
        </ul>
        <Button class="w-full bg-[#ed0331] uppercase tracking-wide p-3"
          >View Details</Button
        >
      </div>
    </div>
  </div>
  <div class="m-auto w-7/12 flex justify-center items-center p-5">
    <Button class="bg-[#ed0331] uppercase tracking-wide p-3"
      >View All Courses</Button
    >
  </div>
</div>

<style>
</style>
