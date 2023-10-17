<script>
  // CSS Import
  // Component Import
  import SignUp from "./lib/SignUp.svelte";
  import SignIn from "./lib/SignIn.svelte";
  import NavBar from "./lib/NavBar.svelte";
  import Courses from "./lib/Courses.svelte";
  import CareerTech from "./lib/CareerTech.svelte";
  import Verify from "./lib/Verify.svelte";
  import Pedagogy from "./lib/Pedagogy.svelte";
  import LowerMidSec from "./components/LowerMidSec.svelte";
  import Footer from "./components/Footer.svelte";
  import Home from './lib/Home.svelte'
  import Banner from './lib/Banner.svelte'
  // Library Import

  // State Management
  // Drawer Management
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
  // Auth Management

  let user = null;
  const handleLogin = (event) => {
    console.log(event.detail);
    user = event.detail;
  };
  const handleLogOut = () => {
    user = null;
    localStorage.removeItem("user");
  };
</script>

<main>
  
  <NavBar
    on:openSignUp={handleOpenSignUp}
    {user}
    on:LogOutUser={handleLogOut}
  />
  <Banner/>
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
  <Verify
    hidden6={drawerId.hiddenVerify}
    on:closeVerify={handleCloseVerify}
    on:LogInUser={handleLogin}
  />
  <Home/>
  <CareerTech />
  <Courses />
  <Pedagogy />
  <LowerMidSec />
  <Footer />
</main>

<style>
</style>
