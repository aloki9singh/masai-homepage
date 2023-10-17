<script>
    import { Avatar, Card } from 'flowbite-svelte';
    import { GiftBoxSolid, ArrowUpRightFromSquareOutline, LinkedinSolid } from 'flowbite-svelte-icons';
    export let detail;
  </script>
  
  <Card class="md:w-[350px]  rounded-[30px] flex justify-center w-full  " >
    <div class="w-full flex justify-end ">
      <LinkedinSolid class="w-7 h-7 mb-3 text-white text-right bg-blue-700 rounded p-1 pb-0"/>
      
    </div>
    <div class="flex">
     
         <img
        src="https://icon2.cleanpng.com/20180525/hbt/kisspng-quotation-mark-apostrophe-computer-icons-5b0878a73ff363.686669161527281831262.jpg"
        alt="left-quote"
        class="inline  text-black w-3 h-3  mr-2"
    />
    <p class="mb-3 leading-6 font-normal text-sm text-gray-500 dark:text-gray-400 line-clamp-3 ">
    {detail.statement}</p>
    </div>
   
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