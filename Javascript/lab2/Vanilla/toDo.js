window.addEventListener("load", function(){ 
    function deactivateTasks(curTask, curButtons){
        let openTasks = document.getElementsByName('open-task');
        let buttons = document.querySelectorAll('.task-buttons');

        for(let i=0; i<openTasks.length; i++){
            if(openTasks[i] != curTask){
                if(buttons[i]){
                    buttons[i].classList.remove('show-buttons');
                }
                openTasks[i].classList.remove('selected-task');
            }
        }
    }

    function deleteTask(event){
        let taskId = event.target.parentElement.id
        taskId = taskId.replace("-btns", "");
        let task = document.getElementById(taskId);        

        let openTasks = document.getElementById('open-tasks');

        openTasks.removeChild(task);
        openTasks.removeChild(event.target.parentElement);
    }
    
    function moveTask(task){
        let openTasks = document.getElementById('open-tasks');
        let completedTasks = document.getElementById('completed-tasks');

        let taskNumber = task.id.replace("task","");

        let btns = document.getElementById(`task${taskNumber}-btns`);
        
        task.classList.remove('selected-task');
        task.classList.add('completed-task');

        task.removeEventListener('click', function(){});
        task.addEventListener('click', function(event){
            let completedTasks = document.getElementById('completed-tasks');
            
            completedTasks.removeChild(event.target);
        });

        openTasks.removeChild(btns);
        completedTasks.appendChild(task);
    }

    function toggleActiveTask(task, buttons){
        task.classList.toggle('selected-task');
        buttons.classList.toggle('show-buttons');
    }

    function createTask(task, buttons){
        let openTasks = document.getElementsByName('open-task');
        let tasks = document.getElementById('open-tasks');

        let newTask = document.createElement('div');
        let taskTitle = document.getElementById('task-title');
        newTask.classList.add('open-task');
        newTask.id = "task"+(openTasks.length+1);
        newTask.setAttribute('name', 'open-task');
        newTask.innerHTML = taskTitle.value;
        taskTitle.value = ""

        let newButtons = document.createElement('div');
        newButtons.classList.add('task-buttons');
        newButtons.setAttribute('name', 'task-buttons');
        newButtons.id = "task"+(openTasks.length+1)+"-btns";

        let deleteBtn = document.createElement('div');
        deleteBtn.classList.add('task-btn');
        deleteBtn.innerHTML = "Delete";
        deleteBtn.addEventListener('click', function(event){
            deleteTask(event);
        });

        let completedBtn = document.createElement('div');
        completedBtn.classList.add('task-btn');
        completedBtn.innerHTML = "Completed";
        completedBtn.addEventListener('click', function(){
            moveTask(newTask);            
        });

        newButtons.appendChild(deleteBtn);
        newButtons.appendChild(completedBtn);

        tasks.appendChild(newTask);
        tasks.appendChild(newButtons);

        newTask.addEventListener('click', function(){
            deactivateTasks(newTask, newButtons);
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