const {taskOne, taskTwo} = require('./tasks');

// Ejecución secuencial
async function main() {
    try {
        console.time('measuring time');
        const valueOne = await taskOne();
        const valueTwo = await taskTwo();
        console.timeEnd('measuring time');
    
        console.log('Task One returned 1', valueOne);
        console.log('Task Two returned 1', valueTwo);    
    } catch (error) {
        console.log(error);
    }
}

main();


// Ejecución paralela
async function main2() {
    try {
        console.time('measuring time 2');
        const results = await Promise.all([taskOne(), taskTwo()]);
        console.timeEnd('measuring time 2');
    
        console.log('Task One returned 2', results[0]);
        console.log('Task Two returned 2', results[1]);    
    } catch (error) {
        console.log(error);
    }
}

main2();