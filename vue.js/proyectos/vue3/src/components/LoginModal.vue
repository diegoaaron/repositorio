<template>
        <section 
        @click="$emit('close-login')" 
        class="z-20 h-screen w-screen bg-gray-500 fixed top-0 opacity-50"></section>
        <div class="absolute inset-0">
            <div class="flex h-full">
                <div class="z-30 m-auto bg-white p-2 rounded shadow w-1/3">
                    <div class="p-2 border" >
                        <h1 class="text-xl">Login</h1>
                        <form class="p-2 my-2">
                            <div class="my-4">
                                <label>Email or Username</label>
                                <input class="rounded shadow p-2 w-full" />
                            </div>
                            <div class="my-4">
                                <label>Password</label>
                                <input class="rounded shadow p-2 w-full" type="password" />
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </div>
</template>

<script>
export default {

};
</script>

<style>

</style>