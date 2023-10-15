<script>
    import { Footer, FooterCopyright, FooterLinkGroup, FooterLink, FooterBrand, FooterIcon, Button } from 'flowbite-svelte';
    import { FacebookSolid, GithubSolid, DiscordSolid, TwitterSolid ,YoutubeSolid,LinkedinSolid} from 'flowbite-svelte-icons';
   
  </script>

  <Footer footerType="socialmedia" class=" bg-black text-white">
    <div class="mx-auto py-5 px-4 sm:px-6 lg:px-8 flex md:flex-row flex-col items-center justify-center border-b border-opacity-20 border-[rgba(209,213,219,0.2)]"> 
        <img src="https://masaischool.com/images/footer/arrow-gif.gif" alt="arrow" class="w-[96px] h-[96px] mr-[16px] hidden lg:block" style=""> <h2 class="font-extrabold tracking-tight text-gray-900">
            <span class="block text-white text-[24px] font-semibold">Get Started</span> 
            <span class="block text-[#FFDB66] text-ms-16 font-semibold">Join the Program</span>
        </h2> <button class="inline-flex items-center mt-4 md:mt-0 md:ml-4 justify-center px-5 py-2.5 text-base font-medium rounded-md text-white bg-red-500">Get your dream job</button>
    </div>
    <!-- <hr class="my-6 border-gray-200 sm:mx-auto dark:border-gray-700 lg:my-8" /> -->
    
    <!-- <hr class="my-2 border-gray-200 sm:mx-auto dark:border-gray-700 lg:my-4" /> -->
  <div class="flex justify-between border-b border-opacity-20 border-[rgba(209,213,219,0.2)] py-4  mb-5">
    <div>
        <img src="https://masaischool.com/images/footer/masai-logo-dark.svg" alt="">
    </div>
    <div class="flex mt-4 space-x-6 sm:justify-center items-center sm:mt-0">
        <div class="text-gray-500">
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
     <!-- <hr class="my-2 border-gray-200 sm:mx-auto dark:border-gray-700 lg:my-4" /> -->
     <div class="flex flex-wrap">
        <div class="flex flex-wrap gap-3 mb-4">
            <Button  class="text-black bg-white" pill>Full Stack Web Development - Full Time</Button>
            <Button  class="text-black bg-white" pill>Data Analytics - Full Time</Button>
            <Button  class="text-black bg-white" pill>Mobile Development - Full Time</Button> 
           <div> <Button  class="text-black bg-white mb-4" pill>Software Testing & Automation - Full Time</Button>
            <Button  class="text-black bg-white" pill>Backend Development - Full Time</Button>
    </div>
         </div>
         <div class="md:flex md:justify-between">
     
            <div class="grid grid-cols-2 gap-5 sm:gap-6 sm:grid-cols-3 text-[18px] text-white ">
              <div>
                <!-- <h2 class="mb-6 text-sm font-semibold text-gray-900 uppercase dark:text-white">Resources</h2> -->
                <FooterLinkGroup ulClass="text-gray-300">
                  <FooterLink liClass=" hover:text-red-700   mb-4" style="text-decoration: none;" >Success Stories</FooterLink>
                  <FooterLink liClass=" hover:text-red-700   mb-4" style="text-decoration: none;" >Our Team</FooterLink>
                  <FooterLink liClass=" hover:text-red-700   mb-4" style="text-decoration: none;" >Careers</FooterLink>
                  <FooterLink liClass=" hover:text-red-700   mb-4" style="text-decoration: none;" >Masai Blog</FooterLink>
                  <FooterLink liClass=" hover:text-red-700   mb-4" style="text-decoration: none;" >Talent Circle</FooterLink>
                  <FooterLink liClass=" hover:text-red-700   mb-4" style="text-decoration: none;" >Masai School Admissions Test <br/>(MSAT)</FooterLink>
                </FooterLinkGroup>
              </div>
              <div>
                <!-- <h2 class="mb-6 text-sm font-semibold uppercase text-gray-900 dark:text-white">Follow us</h2> -->
                <FooterLinkGroup ulClass="text-gray-300">
                  <FooterLink liClass=" hover:text-red-700   mb-4" style="text-decoration: none;" >Hire From Us</FooterLink>
                  <FooterLink liClass=" hover:text-red-700   mb-4" style="text-decoration: none;" >Our Investors</FooterLink>
                  <FooterLink liClass=" hover:text-red-700   mb-4" style="text-decoration: none;" >Newsroom</FooterLink>
                  <FooterLink liClass=" hover:text-red-700   mb-4" style="text-decoration: none;" >Contact Us</FooterLink>
                <FooterLink liClass=" hover:text-red-700   mb-4" style="text-decoration: none;" >Become Coach</FooterLink>
                </FooterLinkGroup>
              </div>
              <div >
                <!-- <h2 class="mb-6 text-sm font-semibold uppercase text-gray-900 dark:text-white">Legal</h2> -->
                <FooterLinkGroup ulClass="text-gray-300">
                  <FooterLink liClass=" hover:text-red-700   mb-4" style="text-decoration: none;" >About Us</FooterLink>
                  <FooterLink liClass=" hover:text-red-700   mb-4" style="text-decoration: none;" >FAQ</FooterLink>
                  <FooterLink liClass=" hover:text-red-700   mb-4" style="text-decoration: none;" >Referral Program</FooterLink>
                  <FooterLink liClass=" hover:text-red-700   mb-4" style="text-decoration: none;" >Masai Learn</FooterLink>
               
                  <FooterLink liClass=" hover:text-red-700   mb-4" style="text-decoration: none;" >Industry Mentors</FooterLink>
                 
                </FooterLinkGroup>
              </div>
            </div>
          
          </div>
        <!-- ---------------- -->
        <div class="mb-6 md:mb-0 md:p-10 p-5 flex justify-center flex-row items-center ">
            <div class="">
                <div class="mb-5 text-center text-lg text-gray-300">
    
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

  
  

    <hr class="my-6 border-gray-500 sm:mx-auto dark:border-gray-700 lg:my-8" />
     
    <div class="sm:flex sm:items-center sm:justify-between ">
    
      <FooterCopyright href="/" by="Masai School | A Nolan Edutech Pvt Ltd Venture" />

    </div>

    <!-- <div class="py-5 lg:px-3 px-4 md:px-0 flex justify-between items-center" style="box-shadow: rgba(243, 242, 242, 0.2) 0px -1px 0px 0px;">
     <p class="xs:hidden lg:block text-neutral-ms-grey-500 leading-[22px] font-normal text-base">© 2023 by Masai School | A Nolan Edutech Pvt Ltd
        Venture
     </p>
         <p class="xs:block lg:hidden text-neutral-ms-grey-500 leading-4 font-normal text-[10px]">
            © 2023 by Masai School
        </p>
         <div class="text-right"><a href="/privacy" rel="noreferrer" class="underline cursor-pointer text-neutral-ms-grey-500 xs:leading-4 lg:leading-[18px] xs:text-[10px] lg:text-xs inline font-normal">
            Privacy Policy
        </a> 
            <span class="text-neutral-ms-grey-500 xs:leading-4 lg:leading-[18px] xs:text-[10px] lg:text-xs font-normal inline mx-0">&amp;</span> 
            <a href="/terms" rel="noreferrer" class="underline cursor-pointer text-neutral-ms-grey-500 xs:leading-4 lg:leading-[18px] xs:text-[10px] lg:text-xs inline font-normal">Terms and Conditions</a></div></div>
  -->
  </Footer>