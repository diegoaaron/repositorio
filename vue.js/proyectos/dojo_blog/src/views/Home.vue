<template>
  <div class="home">
    <h1>Home</h1>
    <PostList v-if="showPosts" :posts="posts" />
    <button @click="showPosts = !showPosts">toggle posts</button>
    <button @click="posts.pop()">delete a post</button>
  </div>
</template>

<!-- https://youtu.be/0FwBjPeLqQ8?list=PL4cUxeGkcC9hYYGbV60Vq3IXYNfDk8At1&t=1135 -->

<script>
import PostList from '../components/PostList.vue'
import { ref } from 'vue'

export default {
  name: 'Home',
  components: { PostList },
  setup() {

    const posts = ref([]);
    const error = ref(null)

    const load = async () => {
      try {
        let data = await fetch('http://localhost:3000/posts')
      }
      catch (err) {

      }
    }

    const showPosts = ref(true)

    return { posts, showPosts }
  }
}
</script>
