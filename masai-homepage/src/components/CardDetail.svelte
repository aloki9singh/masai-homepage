<script>
    import { Avatar, Card } from 'flowbite-svelte';
    import { GiftBoxSolid, ArrowUpRightFromSquareOutline, LinkedinSolid } from 'flowbite-svelte-icons';
    export let detail;
  </script>
  
  <Card class="md:w-[400px]  rounded-[30px]" >
    <div class="w-full flex justify-end ">
      <LinkedinSolid class="w-7 h-7 mb-3 text-white text-right bg-blue-700 rounded p-1"/>
    </div>
    <p class="mb-3 font-normal text-gray-500 dark:text-gray-400 line-clamp-2 pt-5">"{detail.statement}</p>
    <div class="flex gap-5 py-5">
        <Avatar src={detail.img1} rounded />
        <div>
            <h2 class="text-black text-sm">{detail.name}</h2>
            <p class="text-[12px]">{detail.designation}</p>
        </div>
    </div>
   <div class="">
    <img src={detail.img2} class="h-7" alt="">
   </div>
  </Card>