import add
import show
import update 
import delete


add_task_response= add.add_task("Study") 
print(add_task_response) 

show_task_response= show.show_tasks()
print(show_task_response)

update_task_response= update.update_tasks("Study", "Code") 
print(update_task_response) 

delete_task_response= delete.delete_tasks("Study") 
print(delete_task_response)