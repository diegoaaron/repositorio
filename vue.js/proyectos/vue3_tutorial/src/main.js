const template = `<div>
<h1>{{ name }}</h1>
</div>`;

const data = function data() {
    return {
        title: "Vue3 Tutorial updated",
        name: "Sarthak",
    };
}

const app = { data, template};

Vue.createApp(app).mount('#vue-app');
