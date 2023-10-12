<script>
  import { Button, CloseButton, Drawer, Input, Label } from "flowbite-svelte";
  import { sineIn } from "svelte/easing";

  let hidden6 =true;
  let transitionParamsRight = {
    x: 320,
    duration: 200,
    easing: sineIn,
  };
</script>

<div>
  <Drawer
    placement="right"
    transitionType="fly"
    transitionParams={transitionParamsRight}
    bind:hidden={hidden6}
    id="sidebar6"
    class="w-1/3"
  >
    <div class="flex items-center">
      <CloseButton
        on:click={() => (hidden6 = true)}
        class="dark:text-white"
      />
    </div>
    <h2 class='text-2xl text-center font-bold mt-[-2]'>Create Account</h2>
    <p class='text-center text-lg mb-6'>Already have an account? <span class='text-[#3470e4] ml-1'>SignIn</span></p>
    <form action="#" class="mb-6">
      <div class="mb-6">
        <Label for="fullname" class="block mb-2 text-md">Full Name <span class='text-red-600'>*</span></Label>
        <Input id="fullname" name="fullname" required placeholder="Enter full name" class='focus:border-[#3470e4] placeholder:text-lg placeholder:text-gray-300 text-md' />
      </div>
      <div class="mb-6">
        <Label for="email" class="mb-2 text-md">Email Adress <span class='text-red-600'>*</span></Label>
        <Input id="email" name="email" required placeholder="Enter email address" class='focus:border-[#3470e4] placeholder:text-lg placeholder:text-gray-300'/>
      </div>
      <div class="mb-6">
        <Label for="phone" class="mb-2 text-md">Phone Number <span class='text-red-600'>*</span></Label>
        <Input id="phone" name="phone" required placeholder="Enter your whatsapp number" class='focus:border-[#3470e4] placeholder:text-lg placeholder:text-gray-300' />
      </div>
      <div class="mb-6">
        <Label for="referal_code" class="mb-2 text-md">Referal Code (Optional)</Label>
        <Input id="title" name="title" required placeholder="Enter referal code" class='focus:border-[#3470e4] placeholder:text-lg placeholder:text-gray-300'/>
      </div>
      <Button type="submit" class="w-full bg-[#3470e4] uppercase text-sm tracking-widest font-medium">Submit</Button>
    </form>
    <p class='text-sm text-center'>By signing up, I accept the Masai <span class='text-[#3470e4] underline'>Terms of Service </span>and acknowledge the <span class='text-[#3470e4] underline'>Privacy Policy.</span></p>
  </Drawer>
</div>
