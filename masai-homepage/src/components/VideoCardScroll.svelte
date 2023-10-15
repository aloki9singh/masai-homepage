<script>
    import { Carousel } from 'flowbite-svelte';
  import CardDetail from './CardDetail.svelte';
  
    // Define an array of video URLs
    let videos = [
      'https://www.youtube.com/embed/tSlit0vgB20?si=Td9bmZJonS8XHUza',
      'https://www.youtube.com/embed/n0xIOjbNN0A?si=zXxLjSzsUNQ4BL4E',
      'https://www.youtube.com/embed/M18ivLdjZI0?si=kZzMHB2Jcq1Utbfh',
    ];
    function yourTransitionFunction(node, params) {
    // Define your custom transition logic here
    // For example, you can use the provided params to create transitions
    return{}
  }
  let currentVideo = 0;

// Function to change the currently displayed video
function changeVideo(direction) {
  if (direction === 'next') {
    currentVideo = (currentVideo + 1) % videos.length;
  } else {
    currentVideo = (currentVideo - 1 + videos.length) % videos.length;
  }
}


  </script>
  <div class="flex">
    
  <div class="max-w-4xl">
    <Carousel {videos} let:Controls
    images={[]}
    transition={yourTransitionFunction}
    duration={1000}
    ariaLabel="Your Aria Label"
    imgClass="your-img-class"
    >
      <!-- {#each videos as video (video)} -->
        <div class="my-2">
          <iframe
            width="560"
            height="315"
            src={videos[currentVideo]}
            title="YouTube video player"
            frameborder="0"
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
            allowfullscreen
          ></iframe>
        </div>
      <!-- {/each} -->
      <!-- <Controls >
           <button on:click={() => changeVideo('prev')}>Previous</button>
      <button on:click={() => changeVideo('next')}>Next</button>
    
      </Controls> -->
    </Carousel>
  </div>
  <div>
    <CardDetail/>
  </div>
  </div>

  