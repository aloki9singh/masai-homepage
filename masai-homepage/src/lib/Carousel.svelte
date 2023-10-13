<script>
    import { onMount, onDestroy } from "svelte";

    let images = [
        "https://www.masaischool.com/images/new-homepage/banner-student-image1.webp",
        "https://www.masaischool.com/images/new-homepage/banner-student-image2.webp",
        "https://www.masaischool.com/images/new-homepage/banner-student-image3.webp",
        "https://www.masaischool.com/images/new-homepage/banner-student-image4.webp",
    ];

    let currentIndex = 0;
    let interval;

    function nextSlide() {
        currentIndex = (currentIndex + 1) % images.length;
    }

    onMount(() => {
        interval = setInterval(nextSlide, 3000);
    });

    onDestroy(() => {
        clearInterval(interval);
    });
</script>

<div
    class="m-auto w-full  h-[500px] flex justify-center items-center relative z-[-1]"
>
    <img
        src={images[currentIndex]}
        alt={`Slide ${1}`}
       class="w-full h-full object-fit bg-[#d6e2fa] rounded-2xl"
    />
    <span class="m-auto border-[4px] border-solid border-[#9ec4d0] rounded-2xl h-full w-full absolute rotate-[-12deg] z-[-2]"></span>
</div>
