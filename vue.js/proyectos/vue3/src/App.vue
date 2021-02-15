<template>
  <h1>Dc Heros</h1>
  <ul>
    <li v-for="hero in dcHeros" :key="hero">{{ hero.name }}</li>
  </ul>

  <form @submit.prevent="dcHeros.push({ name: newHero });
  newHero = '';">
    <input v-model="newHero" placeholder="Type Hero Name here">
    <button type="submit">Add Hero</button>
  </form>
  

</template>

<script>
export default {
  data() {
    return {
      newHero: "",
      dcHeros: [{name: "Supergirl"}, {name: "Flash"}, {name: "Batman"}, {name: "Arrow"}, {name: "Superman"}],
    }
  }
}
</script>

<style>

</style>