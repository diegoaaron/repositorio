const app = Vue.createApp({
    data() {
        return {
            showBooks: true,
            title: 'The final empirez',
            author: 'Brandon Sanderson',
            age: 45
        }
    },
    methods: {
        changeTitle(abc) {
            this.title = abc;
        },
        toggleShowBooks() {
            this.showBooks = !this.showBooks;
        }
    }
})

app.mount('#app')