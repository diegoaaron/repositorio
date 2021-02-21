const getNombre = (idPost) => {
    console.log(idPost);
    fetch(`https://jsonplaceholder.typicode.com/posts/${idPost}`)
        .then(res => {
            return res.json();
        })
        .then(post => {
            fetch(`https://jsonplaceholder.typicode.com/users/${post.userId}`)
                .then(res => {
                    return res.json()
                })
                .then(user => {
                    console.log(user.name);
                })
        })
}

getNombre(80);

const getNombreAsync = async (idPost) => {

    try {
        const resPost = await fetch(`https://jsonplaceholder.typicode.com/posts/${idPost}`);
        const post = await resPost.json();

        const resAutor = await fetch(`https://jsonplaceholder.typicode.com/users/${post.userId}`);
        const user = await resAutor.json();

        console.log(user.name);

    } catch (error) {
        console.log(error);        
    }
}

getNombreAsync(80);