<script>
  // CSS Import
  // Component Import
  import SignUp from "./lib/SignUp.svelte";
  import SignIn from "./lib/SignIn.svelte";
  import NavBar from "./lib/NavBar.svelte";
  import Banner from "./lib/Banner.svelte";
  import Courses from "./lib/Courses.svelte";
  import CareerTech from "./lib/CareerTech.svelte";
  import Verify from "./lib/Verify.svelte";
  // Library Import
  import { Toast } from 'flowbite-svelte';
  import { CheckCircleSolid,CloseCircleSolid } from 'flowbite-svelte-icons';
  // State Management
  let drawerId = {
    hiddenSignUp: true,
    hiddenVerify: true,
    hiddenSignIn: true,
  };
  const handleOpenSignUp = () => {
    drawerId = { ...drawerId, hiddenSignUp: false, hiddenSignIn: true };
  };
  const handleOpenSignIn = () => {
    drawerId = { ...drawerId, hiddenSignIn: false, hiddenSignUp: true };
  };
  const handleOpenVerify = () => {
    drawerId = { ...drawerId, hiddenSignIn: true, hiddenVerify: false };
  };
  const handleCloseVerify = () => {
    drawerId = {
      ...drawerId,
      hiddenSignIn: true,
      hiddenSignUp: true,
      hiddenVerify: true,
    };
  };
</script>
<!-- <Toast color="green" open={true} position='bottom-right' >
  <svelte:fragment slot="icon">
    <CheckCircleSolid class="w-5 h-5" />
    <span class="sr-only">Check icon</span>
  </svelte:fragment>
  Item moved successfully.
</Toast>
<Toast color="red" open={false} position='bottom-right'>
  <svelte:fragment slot="icon" >
    <CloseCircleSolid class="w-5 h-5" />
    <span class="sr-only">Error icon</span>
  </svelte:fragment>
  Item has been deleted.
</Toast> -->

<main>
  <NavBar on:openSignUp={handleOpenSignUp} />
  <SignUp
    hidden6={drawerId.hiddenSignUp}
    on:openSignIn={handleOpenSignIn}
    on:closeSignUp={handleCloseVerify}
  />
  <SignIn
    hidden6={drawerId.hiddenSignIn}
    on:openSignUp={handleOpenSignUp}
    on:openVerify={handleOpenVerify}
    on:closeSignIn={handleCloseVerify}
  />
  <Verify hidden6={drawerId.hiddenVerify} on:closeVerify={handleCloseVerify} />
  <Banner />
  <CareerTech />
  <Courses />
</main>

<style>
</style>
