<script>
  import { Card, Button, Toggle, Img } from 'flowbite-svelte';
  let hCard = false;
  export let img;
  export let heading;
 
</script>

<div class="flex flex-col justify-between">

 <div> <Img src={img} alt="image"/></div>
     <h5 class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">{heading}</h5>
  
</div>
