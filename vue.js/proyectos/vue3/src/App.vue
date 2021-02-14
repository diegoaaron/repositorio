<template>
  <h1>Dc Heros</h1>
  <ul>
    <li v-for="num in 10" :key="num">{{ num }}</li>
  </ul>
</template>

<script>
export default {
  data() {
    return {
      dcHeros: ["Supergirl", "Flash", "Batman"],
    }
  }
}
</script>

<style>

</style>