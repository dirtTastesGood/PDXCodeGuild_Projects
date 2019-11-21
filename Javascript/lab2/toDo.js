window.addEventListener("load", function(){ 
    function deactivateTasks(curTask, curButtons){
        let openTasks = document.getElementsByName('open-task');
        let buttons = document.getElementsByName('task-buttons');

        for(let i=0; i<openTasks.length; i++){
            if(openTasks[i] != curTask){
                
                openTasks[i].classList.remove('selected-task');
                buttons[i].classList.remove('show-buttons');
            }
        }
    }
    
    function toggleActiveTask(task, buttons){
        deactivateTasks(task, buttons);

        task.classList.toggle('selected-task');
        buttons.classList.toggle('show-buttons');
    }

    function createTask(task, buttons){
        let openTasks = document.getElementsByName('open-task');
        let tasks = document.getElementById('open-tasks');

        let newTask = document.createElement('div');
        let taskTitle = document.getElementById('task-title').value;

        newTask.classList.add('open-task');
        newTask.id = "task"+(openTasks.length+1);
        newTask.setAttribute('name', 'open-task');
        newTask.innerHTML = taskTitle;

        let newButtons = document.createElement('div');
        newButtons.classList.add('task-buttons');
        newButtons.setAttribute('name', 'task-buttons');
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
            toggleActiveTask(newTask, newButtons);
        });
    }
    
    function main(){
        let openTasks = document.getElementsByClassName('open-task');
        
        let submitBtn = document.getElementById('submit-task');
    
        submitBtn.addEventListener("click", function(){
            createTask();
        });
    }

    main();
});

