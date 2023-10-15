<script>
    import { onMount, onDestroy } from "svelte";
    let currentIndex = 0;
    let interval;
    const messages=[
        {
            message:'Going through the 11-11-6 curriculum was a breathtaking experience. Every new unit came with great enthusiasm and a new challenge',
            name:'Salman Lukhman Shaikh',
            image:'https://www.masaischool.com/images/new-homepage/company-logo1.svg'

        },
        {
            message:"I developed Communication Skills, People Skills, Mindset, active patience, JAVA, DSA, JavaScript, CSS, and HTML.",
            name:'Puja Kumari',
            image:'https://www.masaischool.com/images/new-homepage/company-logo2.svg'

        }
        ,
        {
            message:"I liked that every thing is taught in a structured manner, and there is no spoon feeding. That helps us learn by ourself when we do.",
            name:'Ramendra Vikram Singh Parihar',
            image:'https://www.masaischool.com/images/new-homepage/company-logo3.svg',

        },
        {
            message:'I learnt a lot from Masai i.e discipline, time management and professionalism.',
            name:'Harshit Tripathi',
            image:'https://www.masaischool.com/images/new-homepage/company-logo4.svg',
        }
    ]

    function nextSlide() {
        currentIndex = (currentIndex + 1) % messages.length;
    }

    onMount(() => {
        interval = setInterval(nextSlide, 3000);
    });

    onDestroy(() => {
        clearInterval(interval);
    });
</script>

<div
    class="m-auto top-0 left-0  h-[170px] p-2 flex justify-between flex-col rounded-xl box-shadow"
>
<div><img src="https://www.masaischool.com/images/new-homepage/quote-start.svg" alt="left-quote" class="inline"/> <span>{messages[currentIndex].message}</span><img src="https://www.masaischool.com/images/new-homepage/quote-end.svg" alt="right-quote" class="inline"> </div>
<p>{messages[currentIndex].name}</p>
<div><img src={messages[currentIndex].image} alt="message-logo"></div>
</div>

<style>
    .box-shadow{
        box-shadow: rgba(100, 100, 111, 0.2) 0px 7px 29px 0px;
    }
</style>
