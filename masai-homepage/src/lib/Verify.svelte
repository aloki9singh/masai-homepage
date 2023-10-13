<script>
 import { Button, CloseButton, Drawer, Input, Label } from "flowbite-svelte";
    import { createEventDispatcher } from "svelte";
    import { sineIn } from "svelte/easing";
    export let hidden6;
    let transitionParamsRight = {
        x: 320,
        duration: 200,
        easing: sineIn,
    };
    const dispatch=createEventDispatcher();
    const formData={
        otp1:'',
        otp2:'',
        otp3:'',
        otp4:'',
        otp5:'',
        otp6:'',
    }
    const handleSubmit=(event)=>{
        event.preventDefault();
        dispatch('closeVerify')
    }
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
                on:click={() =>dispatch('closeVerify')}
                class="mb-4 dark:text-white"
            />
        </div>
        <div class='h-96 flex flex-col justify-center'>
            <h2 class="text-2xl font-bold mt-10">Verify Email/Phone</h2>
            <p class="text-md mb-1">
                Enter Otp sent to abak005350@gmail...
                <span class="text-[#3470e4] ml-1"> Edit </span>
            </p>
            <form on:submit={handleSubmit}>
                <div class="mb-4 flex justify-between">
                    <Input type="text" name="otp-1" bind:value={formData.otp1} class="border border-gray-300 rounded-lg text-md h-14 py-2 px-2 w-14 text-center mr-1 focus:outline-none focus:border-blue-500" maxlength="1" required/>
                    <Input type="text" name="otp-2" bind:value={formData.otp2} class="border border-gray-300 rounded-lg text-md h-14 py-2 px-2 w-14 text-center mr-1 focus:outline-none focus:border-blue-500" maxlength="1" required/>
                    <Input type="text" name="otp-3" bind:value={formData.otp3} class="border border-gray-300 rounded-lg text-md h-14 py-2 px-2 w-14 text-center mr-1 focus:outline-none focus-border-blue-500" maxlength="1" required/>
                    <Input type="text" name="otp-4" bind:value={formData.otp4} class="border border-gray-300 rounded-lg text-md h-14 py-2 px-2 w-14 text-center mr-1 focus:outline-none focus:border-blue-500" maxlength="1" required/>
                    <Input type="text" name="otp-5" bind:value={formData.otp5} class="border border-gray-300 rounded-lg text-md h-14 py-2 px-2 w-14 text-center mr-1 focus:outline-none focus-border-blue-500" maxlength="1" required/>
                    <Input type="text" name="otp-6" bind:value={formData.otp6} class="border border-gray-300 rounded-lg text-md h-14 py-2 px-2 w-14 text-center mr-1 focus:outline-none focus:border-blue-500" maxlength="1" required/>
                </div>
                <Button type="submit" class="bg-blue-500 hover:bg-blue-600 text-white rounded-md py-2 px-4 w-full text-center font-semibold mt-4 uppercase">Verify</Button>
            </form>
        </div>
    </Drawer>
</div>