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
    credential: "",
  };
  // phone check
  const checkPhone=(num)=>{
    if(num.length!==10||isNaN(num)){
      return false;
    }
    return true;
  }
  const handleSubmit = (event) => {
    event.preventDefault();
    let loginData;
    const isEmail = /^[^@]+@[^@]+\.[^@]+$/.test(formData.credential);
    if(isEmail){
      loginData={email:formData.credential}
    }
    const isPhone=checkPhone(formData.credential);
    if(isPhone){
      loginData={phone:formData.credential}
    }
    console.log(isEmail,isPhone)
    if(!isPhone&&!isEmail){
     return alert("Enter valid email or phone")
    }

    fetch("https://kapil7982.pythonanywhere.com/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(loginData),
    })
      .then((response) => response.json())
      .then((data) => {
        if (data.error) {
          alert(`Error ${data.status_code}: ${data.error}`);
        } else {
          if (data.otp) {
            localStorage.setItem('otp',JSON.stringify(data.otp));
            alert(
              `OTP: ${data.otp},Expire In 5 Min`
            );
            dispatch('openVerify')
          } else {
            alert(data.message); 
          }
        }
      })
      .catch((error) =>alert(error));
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
        on:click={() => dispatch("closeSignIn")}
        class="mb-4 dark:text-white"
      />
    </div>
    <div class="h-96 flex flex-col justify-center">
      <h2 class="text-2xl text-center font-bold mt-10">SignIn</h2>
      <p class="text-center text-lg mb-6">
        New User?
        <span
          role="button"
          tabindex="0"
          on:keydown={() => {}}
          on:click={() => {
            dispatch("openSignUp");
          }}
          class="text-[#3470e4] ml-1"
        >
          SignUp
        </span>
      </p>
      <form action="#" class="mt-6" on:submit={handleSubmit}>
        <div class="mb-6">
          <Label for="fullname" class="block mb-2 text-md"
            >Phone number or email address<span class="text-red-600">*</span
            ></Label
          >
          <Input
            id="fullname"
            name="fullname"
            required
            placeholder="Enter phone number or email address"
            class="focus:border-[#3470e4] placeholder:text-lg placeholder:text-gray-300 text-md"
            bind:value={formData.credential}
          />
        </div>
        <Button
          type="submit"
          class="w-full bg-[#3470e4] uppercase text-sm tracking-widest font-medium"
          >Continue</Button
        >
      </form>
    </div>
  </Drawer>
</div>
