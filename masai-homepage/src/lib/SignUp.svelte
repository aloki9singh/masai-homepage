<script>
  import { Button, CloseButton, Drawer, Input, Label } from "flowbite-svelte";
  import { sineIn } from "svelte/easing";
  import { createEventDispatcher } from "svelte";
  export let hidden6;
  let transitionParamsRight = {
    x: 320,
    duration: 200,
    easing: sineIn,
  };
  const dispatch = createEventDispatcher();
  let formData = {
    username: "",
    email: "",
    phone: "",
    referalCode: "",
  };
  const handleSubmit = (event) => {
    event.preventDefault();
    fetch("http://kapil7982.pythonanywhere.com/signup", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        full_name: formData.username,
        email: formData.email,
        phone: formData.phone,
      }),
    })
      .then((response) => response.json())
      .then((data) => {
        if (data.error) {
          alert(`Error ${data.status_code}: ${data.error}`);
        } else {
          alert(data.message);
        }
      })
      .catch((error) => alert(`Erro:${error}`));
  };
</script>

<div>
  <Drawer
    placement="right"
    transitionType="fly"
    transitionParams={transitionParamsRight}
    bind:hidden={hidden6}
    id="sidebar6"
    class="md:w-1/3 w-full "
  >
    <div class="flex items-center">
      <CloseButton
        on:click={() => dispatch("closeSignUp")}
        class="dark:text-white"
      />
    </div>
    <h2 class="text-2xl text-center font-bold mt-[-2]">Create Account</h2>
    <p class="text-center text-lg mb-6">
      Already have an account? <span
        class="text-[#3470e4] ml-1"
        tabindex="0"
        on:keydown={() => {}}
        role="button"
        on:click={() => {
          dispatch("openSignIn");
        }}>SignIn</span
      >
    </p>
    <form action="#" class="mb-6" on:submit={handleSubmit}>
      <div class="mb-6">
        <Label for="username" class="block mb-2 text-md"
          >Full Name <span class="text-red-600">*</span></Label
        >
        <Input
          id="username"
          name="username"
          type="text"
          required
          placeholder="Enter full name"
          bind:value={formData.username}
          class="focus:border-[#3470e4] placeholder:text-lg placeholder:text-gray-300 text-md"
        />
      </div>
      <div class="mb-6">
        <Label for="email" class="mb-2 text-md"
          >Email Adress <span class="text-red-600">*</span></Label
        >
        <Input
          id="email"
          name="email"
          type="email"
          required
          placeholder="Enter email address"
          bind:value={formData.email}
          class="focus:border-[#3470e4] placeholder:text-lg placeholder:text-gray-300"
        />
      </div>
      <div class="mb-6">
        <Label for="phone" class="mb-2 text-md"
          >Phone Number <span class="text-red-600">*</span></Label
        >
        <Input
          id="phone"
          name="phone"
          required
          placeholder="Enter your whatsapp number"
          bind:value={formData.phone}
          class="focus:border-[#3470e4] placeholder:text-lg placeholder:text-gray-300"
          type="number"
        />
      </div>
      <!-- <div class="mb-6">
        <Label for="referal_code" class="mb-2 text-md"
          >Referal Code (Optional)</Label
        >
        <Input
          id="title"
          name="title"
          required
          placeholder="Enter referal code"
          bind:value={formData.referalCode}
          class="focus:border-[#3470e4] placeholder:text-lg placeholder:text-gray-300"
          type="text"
        />
      </div> -->
      <Button
        type="submit"
        class="w-full bg-[#3470e4] uppercase text-sm tracking-widest font-medium"
        >Submit</Button
      >
    </form>
    <p class="text-sm text-center">
      By signing up, I accept the Masai <span class="text-[#3470e4] underline"
        >Terms of Service
      </span>and acknowledge the
      <span class="text-[#3470e4] underline">Privacy Policy.</span>
    </p>
  </Drawer>
</div>

<style>
</style>
