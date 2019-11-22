$(document).ready(function(){
    $.fn.createTask = function(){
        let $openTasks = $("#open-tasks");
        let $tasks = $(".open-task");

        let $newTask = $('<div>');
        $newTask.attr('id', "task"+($tasks.length +  1));
        $newTask.addClass('open-task');
        
        $taskTitle = $('#task-title');
        $newTask.html($taskTitle.val());
        $taskTitle.val('');

        let $newButtons = $('<div>');
        $newButtons.addClass('task-buttons');
        $newButtons.attr('id', 'task'+($tasks.length + 1)+'-btns');    

        let $deleteBtn = $('<div>');
        $deleteBtn.addClass('task-btn');
        $deleteBtn.html('Delete');
        $deleteBtn.click(function(event){
            $.fn.deleteTask(event);
        });

        let $completeBtn = $('<div>');
        $completeBtn.addClass('task-btn');
        $completeBtn.html('Completed');
        $completeBtn.click(function(event){
            // $.fn.moveTask(event);
        });

        $newButtons.append($deleteBtn);
        $newButtons.append($completeBtn);

        $newTask.click(function(event){
            $.fn.toggleActiveTask(event);
        });

        $openTasks.append($newTask);
        $openTasks.append($newButtons);
    }

    $.fn.toggleActiveTask = function(event){
        let $curTask = $('.selected-task');
        let $curButtons = $('.show-buttons');
        let $task = $(`#${event.target.id}`);
        let $taskId = $task.attr('id');
        
        if($curTask.attr('id') != $task.attr('id')){
            $curTask.toggleClass('selected-task');
            $curButtons.toggleClass('show-buttons');
        }

        $btnsId = `#task${$taskId.replace("task","")}-btns`;
        let $btns = $($btnsId);
        
        $task.toggleClass('selected-task');
        $btns.toggleClass('show-buttons');
    }

    $.fn.deleteTask = function(event){       
        let $openTasks = $('#open-tasks');

        let $taskId = event.target.parentElement.id;
        $taskId = $taskId.replace("-btns", "");
        let $task = $(`#${$taskId}`);

        $task.remove();
        event.target.parentElement.remove();
        
    }

    $.fn.main = function(){
        $('#submit-task').click(function(){
            $.fn.createTask();
        });

    }

    $.fn.main();
});