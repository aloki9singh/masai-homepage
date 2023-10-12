<script>
    import { Button, CloseButton, Drawer, Input, Label } from "flowbite-svelte";
    import { sineIn } from "svelte/easing";

    let hidden6 = true;
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
                class="mb-4 dark:text-white"
            />
        </div>
        <div class='h-96 flex flex-col justify-center'>
            <h2 class="text-2xl text-center font-bold mt-10">SignIn</h2>
            <p class="text-center text-lg mb-6">
                New User
                <span class="text-[#3470e4] ml-1"> SignUp </span>
            </p>
            <form action="#" class="mt-6">
                <div class="mb-6">
                    <Label for="fullname" class="block mb-2 text-md"
                        >Phone number or email address<span class="text-red-600"
                            >*</span
                        ></Label
                    >
                    <Input
                        id="fullname"
                        name="fullname"
                        required
                        placeholder="Enter phone number or email address"
                        class="focus:border-[#3470e4] placeholder:text-lg placeholder:text-gray-300 text-md"
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
