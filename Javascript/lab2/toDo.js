
window.addEventListener("load", function(){ 
    function toggleActiveTask(task, buttons){

        
    }
    
    let openTasks = document.getElementsByClassName('open-task');

    for(let i=1; i<openTasks.length+1; i++){
        let task = openTasks[i-1];
        let buttons = document.getElementById('task'+i+'-btns');
        
        let curTask;
        let curButtons;
        
        task.addEventListener('click', function(){
    
            if(curTask && curTask != task && curTask.classList.contains('selected-task')){
                curTask.classList.toggle('selected-task');
            }
            if(curButtons && curButtons != buttons && curButtons.classList.contains('show-buttons')){
                curButtons.classList.toggle('show-buttons');
            }   
            
            task.classList.toggle('selected-task');
            buttons.classList.toggle('show-buttons');
        
            curTask = task;
            curButtons = buttons;
            });
        }

    let submitBtn = document.getElementById('submit-task');
    let tasks = document.getElementById('open-tasks');

    submitBtn.addEventListener("click", function(){
        let newTask = document.createElement('div');
        let taskTitle = document.getElementById('task-title').value;

        newTask.classList.add('open-task');
        newTask.id = "task"+(openTasks.length+1);
        newTask.innerHTML = taskTitle;

        let newButtons = document.createElement('div');
        newButtons.classList.add('task-buttons');
        newButtons.id = "task"+(openTasks.length+1)+"-btns";

        let deleteBtn = document.createElement('div');
        deleteBtn.classList.add('task-btn');
        deleteBtn.innerHTML = "Delete";

        let completedBtn = document.createElement('div');
        completedBtn.classList.add('task-btn');
        completedBtn.innerHTML = "Completed";

        newButtons.appendChild(deleteBtn);
        newButtons.appendChild(completedBtn);

        tasks.appendChild(newTask);
        tasks.appendChild(newButtons);

        newTask.addEventListener('click', function(){
            if(curTask && curTask != task && curTask.classList.contains('selected-task')){
                curTask.classList.toggle('selected-task');
            }
            if(curButtons && curButtons != buttons && curButtons.classList.contains('show-buttons')){
                curButtons.classList.toggle('show-buttons');
            }   
            
            task.classList.toggle('selected-task');
            buttons.classList.toggle('show-buttons');

            curTask = task;
            curButtons = buttons;
        });
    });
});