<script>
    import { Pagination, PaginationItem } from 'flowbite-svelte';
    import { ArrowLeftSolid, ArrowRightSolid } from 'flowbite-svelte-icons';
    const previous = () => {
      alert('Previous btn clicked. Make a call to your server to fetch data.');
    };
    const next = () => {
      alert('Next btn clicked. Make a call to your server to fetch data.');
    };
  </script>
  
  <div class="flex space-x-3">
    <PaginationItem class="flex items-center" on:click={previous}>
      <ArrowLeftSolid class="mr-2 w-3.5 h-3.5" />
      Previous
    </PaginationItem>
    <PaginationItem class="flex items-center" on:click={next}>
      Next
      <ArrowRightSolid class="ml-2 w-3.5 h-3.5" />
    </PaginationItem>
  </div>
  <div class="flex space-x-3">
    <PaginationItem large class="flex items-center" on:click={previous}>
      <ArrowLeftSolid class="mr-2 w-5 h-5" />
      Previous
    </PaginationItem>
    <PaginationItem large class="flex items-center" on:click={next}>
      Next
      <ArrowRightSolid class="ml-2 w-5 h-5" />
    </PaginationItem>
  </div>