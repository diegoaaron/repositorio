const { userInfo } = require("os");

async function requestHandler(req, res) {
    try {
        const user = await User.findById(req.userId);
        const tasks = await Task.findById(user.tasksId);
        tasks.completed = true;
    
        await tasks.save();
        res.send('Task completed');
    } catch (error) {
        res.send(error);
        
    }


}