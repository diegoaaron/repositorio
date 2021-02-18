<template>
    <div class="flex flex-wrap w-full">
        <div v-if="currentSlide == 0" class="absolute w-full bg-blue-600" style="height: 350px"></div>
        <div v-if="currentSlide == 1" class="absolute w-full bg-yellow-600" style="height: 350px"></div>
        <div v-if="currentSlide == 2" class="absolute w-full bg-green-600" style="height: 350px"></div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            currentSlide: 0,
            interval: "",
        };
    },
    mounted() {
        this.interval =  setInterval(() => {
            if(this.currentSlide === 2) {
                this.currentSlide = 0;
            } else {
                this.currentSlide++;
            }
        }, 2000);
    },
    beforeUnmount() {
        clearInterval(this.interval);
    },
    
};
</script>

<style>

</style>