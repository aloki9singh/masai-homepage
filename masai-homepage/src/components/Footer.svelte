<script>
    import { Footer, FooterCopyright, FooterLinkGroup, FooterLink, FooterBrand, FooterIcon, Button } from 'flowbite-svelte';
  import { LinkedinSolid } from 'flowbite-svelte-icons';
  import { YoutubeSolid } from 'flowbite-svelte-icons';
    import { FacebookSolid, GithubSolid, DiscordSolid, TwitterSolid } from 'flowbite-svelte-icons';
    // import Dribble from 'flowbite-svelte-icons/Dribble.svelte'
  </script>
     <hr class="my-6 border-gray-200 sm:mx-auto dark:border-gray-700 lg:my-8" />
     
  <Footer footerType="socialmedia" class=" bg-black text-white">
    <hr class="my-2 border-gray-200 sm:mx-auto dark:border-gray-700 lg:my-4" />
  <div class="flex justify-between">
    <div>
        <img src="https://masaischool.com/images/footer/masai-logo-dark.svg" alt="">
    </div>
    <div class="flex mt-4 space-x-6 sm:justify-center items-center sm:mt-0">
        <div>
            Follow us :-
        </div>
        <FooterIcon href="/">
            <TwitterSolid class="w-8 h-5 text-gray-500 dark:text-gray-500 hover:text-gray-900 dark:hover:text-white" />
          </FooterIcon>
        <FooterIcon href="/">
          <FacebookSolid class="w-8 h-5 text-gray-500 dark:text-gray-500 hover:text-gray-900 dark:hover:text-white" />
        </FooterIcon>
        <FooterIcon href="/">
            <LinkedinSolid class="w-8 h-5 text-gray-500 dark:text-gray-500 hover:text-gray-900 dark:hover:text-white" />
          </FooterIcon>
        <FooterIcon href="/">
          <DiscordSolid class="w-8 h-5 text-gray-500 dark:text-gray-500 hover:text-gray-900 dark:hover:text-white" />
        </FooterIcon>
        
      
       
        <FooterIcon href="/">
          <GithubSolid class="w-8 h-5 text-gray-500 dark:text-gray-500 hover:text-gray-900 dark:hover:text-white" />
        </FooterIcon>
        <FooterIcon href="/">
            <YoutubeSolid class="w-8 h-5 text-gray-500 dark:text-gray-500 hover:text-gray-900 dark:hover:text-white" />
          </FooterIcon>
        <FooterIcon href="/">
          <!-- <Dribble /> -->
        </FooterIcon>
      </div>
  </div>
     <hr class="my-2 border-gray-200 sm:mx-auto dark:border-gray-700 lg:my-4" />
     <div>
       
     </div>
     <div class="flex flex-wrap">
        <div class="flex flex-wrap gap-3 mb-4">
            <Button color="dark" class="text-black bg-white" pill>Full Stack Web Development - Full Time</Button>
            <Button color="dark" class="text-black bg-white" pill>Data Analytics - Full Time</Button>
            <Button color="dark" class="text-black bg-white" pill>Mobile Development - Full Time</Button>
            <Button color="dark" class="text-black bg-white" pill>Software Testing & Automation - Full Time</Button>
            <Button color="dark" class="text-black bg-white" pill>Backend Development - Full Time</Button>
    
         </div>
         <div class="md:flex md:justify-between">
     
            <div class="grid grid-cols-2 gap-5 sm:gap-6 sm:grid-cols-3 text-[18px] text-white ">
              <div>
                <!-- <h2 class="mb-6 text-sm font-semibold text-gray-900 uppercase dark:text-white">Resources</h2> -->
                <FooterLinkGroup >
                  <FooterLink liClass=" hover:text-red-500 mb-4" >Success Stories</FooterLink>
                  <FooterLink liClass=" hover:text-red-500 mb-4" >Our Team</FooterLink>
                  <FooterLink liClass=" hover:text-red-500 mb-4" >Careers</FooterLink>
                  <FooterLink liClass=" hover:text-red-500 mb-4" >Masai Blog</FooterLink>
                  <FooterLink liClass=" hover:text-red-500 mb-4" >Talent Circle</FooterLink>
                  <FooterLink liClass=" hover:text-red-500 mb-4" >Masai School Admissions Test <br/>(MSAT)</FooterLink>
                </FooterLinkGroup>
              </div>
              <div>
                <!-- <h2 class="mb-6 text-sm font-semibold uppercase text-gray-900 dark:text-white">Follow us</h2> -->
                <FooterLinkGroup>
                  <FooterLink liClass=" hover:text-red-500 mb-4" >Hire From Us</FooterLink>
                  <FooterLink liClass=" hover:text-red-500 mb-4" >Our Investors</FooterLink>
                  <FooterLink liClass=" hover:text-red-500 mb-4" >Newsroom</FooterLink>
                  <FooterLink liClass=" hover:text-red-500 mb-4" >Contact Us</FooterLink>
                <FooterLink liClass=" hover:text-red-500 mb-4" >Become Coach</FooterLink>
                </FooterLinkGroup>
              </div>
              <div >
                <!-- <h2 class="mb-6 text-sm font-semibold uppercase text-gray-900 dark:text-white">Legal</h2> -->
                <FooterLinkGroup>
                  <FooterLink liClass=" hover:text-red-500 mb-4" >About Us</FooterLink>
                  <FooterLink liClass=" hover:text-red-500 mb-4" >FAQ</FooterLink>
                  <FooterLink liClass=" hover:text-red-500 mb-4" >Referral Program</FooterLink>
                  <FooterLink liClass=" hover:text-red-500 mb-4" >Masai Learn</FooterLink>
               
                  <FooterLink liClass=" hover:text-red-500 mb-4" >Industry Mentors</FooterLink>
                 
                </FooterLinkGroup>
              </div>
            </div>
          
          </div>
        <!-- ---------------- -->
        <div class="mb-6 md:mb-0 flex justify-center flex-row items-center ">
            <div class="">
                <div class="mb-5 text-center text-lg">
    
                    Connect with a growing <br/>
                                community of learners
                </div>
                
                <div class="rounded bg-white text-blue-500 px-4 py-2">
        
                    <FooterBrand href="https://www.flaticon.com/free-icons/telegram" class="text-sm" src="/telegram.png" alt="Flowbite Logo"  >
                        <span class="text-[16px]">JOIN OUR TELEGRAM</span>
                    </FooterBrand>
                </div>
            </div>
          
          </div>
     </div>

  
  

    <hr class="my-6 border-gray-200 sm:mx-auto dark:border-gray-700 lg:my-8" />
     
    <div class="sm:flex sm:items-center sm:justify-between">
        <!-- © 2023 by Masai School | A Nolan Edutech Pvt Ltd Venture -->
      <FooterCopyright href="/" by="Masai School | A Nolan Edutech Pvt Ltd Venture" />

    </div>
  </Footer>