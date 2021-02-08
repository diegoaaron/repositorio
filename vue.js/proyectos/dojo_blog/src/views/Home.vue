<template>
  <div class="home">
    <h1>Home</h1>
    <h2>Refs</h2>
    <p>{{ ninjaOne.name }} - {{ ninjaOne.age }}</p>
    <button @click="updateNinjaOne">Update ninja one</button>

    <h2>Reactive</h2>
    <p>{{ ninjaTwo.name }} - {{ ninjaTwo.age }}</p>
    <button @click="updateNinjaTwo">Update ninja two</button>
  </div>
</template>

<script>

// https://youtu.be/V-kxBWcPJfo?list=PL4cUxeGkcC9hYYGbV60Vq3IXYNfDk8At1&t=1920

import { ref, reactive } from 'vue'

export default {
  name: 'Home',
  setup() {

    const ninjaOne = ref({ name: 'mario', age: 30})
    const ninjaTwo = reactive({ name: 'luigi', age: 35})

    const updateNinjaOne = () => {
      ninjaOne.value.age = 40
    }

    const updateNinjaTwo = () => {
      ninjaTwo.age = 45
    }

    return { ninjaOne, updateNinjaOne, ninjaTwo, updateNinjaTwo }
  }
}
</script>
