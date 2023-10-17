<script>
  import {
    Avatar,
    Button,
    Navbar,
    NavBrand,
    NavHamburger,
    NavLi,
    NavUl,
    ArrowKeyDown,
    Dropdown,
    DropdownItem,
  } from "flowbite-svelte";
  import { createEventDispatcher } from "svelte";
  export let user;
  function removeAfterAtSymbol(inputString) {
    const atIndex = inputString.indexOf("@");
    if (atIndex !== -1) {
      return inputString.substring(0, atIndex);
    }
    return inputString;
  }

  const dispatch = createEventDispatcher();
</script>

<div class="fixed w-full bg-white z-50 ">
  <div class="w-full p-2 bg-[#fedfe5] flex justify-center items-center gap-3 font-medium text-[15.8px]">
    <p>Applications for our 6th November Batches are now open!</p>
    <Button class="bg-[#ed0331] uppercase tracking-wider px-3 text-[15px] py-2">Apply Now</Button>
  </div>
  <Navbar class="w-full md:w-[80%] m-auto py-5">
    <div class="flex justify-between items-center md:gap-2">
      <NavHamburger class='p-0'/>
      <NavBrand href="/">
        <img
          src="https://masai-website-images.s3.ap-south-1.amazonaws.com/logo.png"
          class="mr-3 h-10"
          alt="Masai Logo"
        />
      </NavBrand>
    </div>
    
    <div class="flex gap-3 md:order-2">
      <Button
        size="lg"
        class="uppercase pl-1 pr-1 px-2 bg-[#e5feff] text-[#6E71CC] hover:bg-[#8bd3d5]"
        >Refer & Earn</Button
      >
      {#if !user}
        <Button
          size="xl"
          outline
          color="red"
          class="hover:bg-red-100 text-sm hover:text-red-200  px-3 border-none lg:border lg:border-solid lg:border-red-600"
          on:click={() => {
            dispatch("openSignUp");
          }}>SIGN UP</Button
        >
      {:else}
        <div class="flex justify-center items-center rounded-lg pr-2">
          <Avatar>{removeAfterAtSymbol(user.email)[0]}</Avatar>
          <span class="ml-2">{removeAfterAtSymbol(user.email)}</span>
          <ArrowKeyDown class="border-none" />
          <Dropdown>
            <DropdownItem>Dashboard</DropdownItem>
            <DropdownItem
              on:click={() => {
                dispatch("LogOutUser");
              }}>Sign out</DropdownItem
            >
          </Dropdown>
        </div>
      {/if}
    </div>
    <NavUl ulClass="text-sm font-medium flex uppercase h-screen md:h-full  flex flex-col md:flex-row md:gap-2 lg:gap-9 md:hidden xl:flex">
      <NavLi href="/" active={true}>Courses</NavLi>
      <NavLi href="/">Fees</NavLi>
      <NavLi href="/">Events</NavLi>
      <NavLi href="/">Learn</NavLi>
      <NavLi href="/">Success Stories</NavLi>
      <NavLi href="/">Hire from us</NavLi>
    </NavUl>
  </Navbar>
</div>
