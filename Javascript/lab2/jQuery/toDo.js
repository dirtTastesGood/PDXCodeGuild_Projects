$(document).ready(function(){
    $.fn.createTask = function(){
        let $openTasks = $("#open-tasks");
        let $tasks = $("#open-task");
        
        let $newTask = $('<div>');
        $newTask.attr('id', "task"+$tasks.length);
        $newTask.addClass('open-task');
        
        $taskTitle = $('#task-title');
        $newTask.html($taskTitle.val());
        $taskTitle.val('');

        $newTask.click(function(event){
            // $fn.deactivateTasks(event);
            $.fn.toggleActiveTask(event);
        });

        let $newButtons = $('<div>');
        $newButtons.addClass('task-buttons');
        $newButtons.attr('id', 'task'+$tasks.length+"-btns");
        
        let $deleteBtn = $('<div>');
        $deleteBtn.addClass('task-btn');
        $deleteBtn.html('Delete');
        $deleteBtn.click(function(event){
            // $.fn.deleteTask(event);
        });

        let $completeBtn = $('<div>');
        $completeBtn.addClass('task-btn');
        $completeBtn.html('Completed');
        $completeBtn.click(function(event){
            // $.fn.moveTask(event);
        });

        $newButtons.append($deleteBtn);
        $newButtons.append($completeBtn);

        $openTasks.append($newTask);
        $openTasks.append($newButtons);
    }

    $.fn.toggleActiveTask = function(event){
        console.log(event);
        
    }

    $.fn.main = function(){
        $('#submit-task').click(function(){
            $.fn.createTask();
        });

    }

    $.fn.main();
});