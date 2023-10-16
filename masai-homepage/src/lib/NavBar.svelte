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

<div class="fixed w-full bg-white z-50">
  <div class="w-full p-2 bg-[#fedfe5] flex justify-center items-center gap-3">
    <p>Applications for our 6th November Batches are now open!</p>
    <Button class="bg-[#ed0331] uppercase tracking-wider">Apply Now</Button>
  </div>
  <Navbar class="w-full">
    <NavBrand href="/">
      <img
        src="https://masai-website-images.s3.ap-south-1.amazonaws.com/logo.png"
        class="mr-3 h-6 sm:h-9"
        alt="Masai Logo"
      />
    </NavBrand>
    <div class="flex gap-3 md:order-2">
      <Button
        size="lg"
        class="uppercase pl-1 pr-1 bg-[#e5feff] text-blue-500 hover:bg-[#8bd3d5]"
        >Refer & Earn</Button
      >
      {#if !user}
        <Button
          size="xl"
          outline
          color="red"
          class="hover:bg-red-100 hover:text-red-500 pl-2 pr-2"
          on:click={() => {
            dispatch("openSignUp");
          }}>Sign Up</Button
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
      <NavHamburger />
    </div>
    <NavUl ulClass="text-sm font-medium flex uppercase gap-9">
      <NavLi href="/" active={true}>Courses</NavLi>
      <NavLi href="/">Fees</NavLi>
      <NavLi href="/">Events</NavLi>
      <NavLi href="/">Learn</NavLi>
      <NavLi href="/">Success Stories</NavLi>
      <NavLi href="/">Hire from us</NavLi>
    </NavUl>
  </Navbar>
</div>
