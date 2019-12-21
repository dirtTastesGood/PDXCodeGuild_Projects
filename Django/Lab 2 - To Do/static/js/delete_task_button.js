let deleteTaskButton = document.querySelector('#delete-task-button');

deleteTaskButton.addEventListener('mouseover', () =>{
    deleteTaskButton.innerHTML = "Delete task!";
});

deleteTaskButton.addEventListener('mouseout', () => {
    deleteTaskButton.innerText = 'Task complete!';
});