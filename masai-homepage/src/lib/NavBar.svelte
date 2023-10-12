<script>
  import { Button, Navbar,NavBrand,NavHamburger,NavLi,NavUl } from "flowbite-svelte";
</script>

<Navbar class="sticky">
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
      <Button
        size="xl"
        outline
        color="red"
        class="hover:bg-red-100 hover:text-red-500 pl-2 pr-2">Sign Up</Button
      >
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