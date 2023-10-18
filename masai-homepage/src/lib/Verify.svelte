<script>
  import { onMount } from "svelte";
  import { Button, CloseButton, Drawer, Input, Label } from "flowbite-svelte";
  import { createEventDispatcher } from "svelte";
  import { sineIn } from "svelte/easing";
  export let hidden6;
  let transitionParamsRight = {
    x: 320,
    duration: 200,
    easing: sineIn,
  };
  const dispatch = createEventDispatcher();
  const formData = {
    otp1: "",
    otp2: "",
    otp3: "",
    otp4: "",
    otp5: "",
    otp6: "",
  };
  let currentFocus = 1;

  onMount(() => {
    focusOnInput(currentFocus);
  });

  const handleInput = (event, inputIndex) => {
    formData[`otp${inputIndex}`] = event.target.value;

    if (event.target.value && inputIndex < 6) {
      focusOnInput(inputIndex + 1);
    }

    if (!event.target.value && inputIndex > 1) {
      focusOnInput(inputIndex - 1);
    }
  };

  const focusOnInput = (index) => {
    currentFocus = index;
    const input = document.getElementById(`otp-${index}`);
    input.focus();
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    const otp_code = Object.values(formData).join("");

    fetch("https://kapil7982.pythonanywhere.com/verify_otp", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        otp_code: otp_code,
      }),
    })
      .then((response) => response.json())
      .then((data) => {
        if (data.error) {
          alert(data.error);
        } else {
          dispatch("LogInUser", { email: data.email });
          dispatch("closeVerify");
          alert("Login Successfully!");
        }
      })
      .catch((error) => console.error("Error:", error));
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
        on:click={() => dispatch("closeVerify")}
        class="mb-4 dark:text-white"
      />
    </div>
    <div class="h-96 flex flex-col justify-center">
      <h2 class="text-2xl font-bold mt-10">Verify Email/Phone</h2>
      <p class="text-md mb-1">
        Enter the OTP!
        <span class="text-[#3470e4] ml-1"> Edit </span>
      </p>
      <form on:submit={handleSubmit}>
        <div class="mb-4 flex justify-between">
          {#each Array.from({ length: 6 }) as _, i}
            <Input
              type="text"
              name="otp-{i + 1}"
              bind:value={formData[`otp${i + 1}`]}
              class="border border-gray-300 rounded-lg text-md h-14 py-2 px-2 w-14 text-center mr-1 focus:outline-none focus:border-blue-500"
              maxlength="1"
              id={`otp-${i + 1}`}
              on:input={(event) => handleInput(event, i + 1)}
              required
            />
          {/each}
        </div>
        <Button
          type="submit"
          class="bg-blue-500 hover:bg-blue-600 text-white rounded-md py-2 px-4 w-full text-center font-semibold mt-4 uppercase"
        >
          Verify
        </Button>
      </form>
    </div>
  </Drawer>
</div>
