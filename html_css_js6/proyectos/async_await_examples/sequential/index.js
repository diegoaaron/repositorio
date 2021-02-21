const {taskOne, taskTwo} = require('./tasks');

async function main() {
    console.time('measuring time');
    const valueOne = await taskOne();
    const valueTwo = await taskTwo();
    console.timeEnd('measuring time');

    console.log('Task One returned', valueOne);
    console.log('Task Two returned', valueTwo);
}

main();

