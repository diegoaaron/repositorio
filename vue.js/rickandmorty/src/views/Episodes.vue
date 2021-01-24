<template>
  <h1>Episodes</h1>
  <ul>
      <li v-for="episode in episodes" :key="episode.id">
          {{ episode.name }}
      </li>
  </ul>
</template>

<script>
import { request as fetchGQL } from 'graphql-request';
import { inject, ref } from 'vue';
export default {
    setup() {
        let episodes = ref([]);
        const info = inject('info');

        fetchGQL('https://rickandmortyapi.com/graphql',
        /* GraphQL */`query {
            episodes {
                info {
                    count
                    pages
                    next
                    prev
                }
                results {
                    id
                    name
                    air_date
                    episode
                    created
                }
            }
        }`).then((data) => {
            episodes.value = data.episodes.results;
            info.value = data.episodes.info;
        });

        return {
            episodes,
        };
    },
};
</script>

<style>

</style>