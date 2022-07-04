# authentication ==ok

# login ==ok

# view for listing all todos  ==ok

# view for fetching a specifics todo ==ok

# list all todos created by authenticated user ==ok

# view for updating a specific todo ==ok

# view for deleting a specific todo ==ok

# logout ==ok

from djngo.todosapp.models import users,todos
session={}
def authenticate(**kwargs):
    username=kwargs.get("username")
    password=kwargs.get("password")
    user=[user for user in users if user["username"]==username and user["password"]==password]
    return user

class SignInView:
    def post(self,*args,**kwargs):
        username=kwargs.get("username")
        password=kwargs.get("password")
        user=authenticate(username=username,password=password)
        if user:
            session["user"]=user[0]
            print("success")

        else:
            print("invalid")

class AllTodosView:
    def get(self,*args,**kwargs):
        return todos
    def get_id(self,id):
        todo=[todo for todo in todos if todo["todoId"]==id]
        return todo

    #for specific todo

    def get(self,*args,**kwargs):
        todo_Id=kwargs.get("todo_Id")
        # todo=[todo for todo in todos if todo["todoId"]==todo_Id]
        todo=self.get_id(todo_Id)
        print(todo)
    #for updating the todo
    def put(self, *args, **kwargs):
        todoId=kwargs.get("todoId")
        todo=self.get_id(todoId)[0]
        post=kwargs.get("post")
        todo.update(post)
        print(todo)

    #for deleting the todo
    def delete(self,*args,**kwargs):
        todo_Id=kwargs.get("todo_id")
        delete=self.get_id(todo_Id)
        if delete:
            todo=delete[0]
            todos.remove(todo)
            print("todo delete successfully")
            print(todos)




class SpecificTodoView:
    def get(self,*args,**kwargs):

        user_id=session["user"]["id"]
        tod=[tod for tod in todos if tod["userId"]==user_id]
        return tod

#for logout

def delete(**kwargs):
    session.pop("user")
    print("logout successfully")




signin=SignInView()
signin.post(username="nikil",password="Password@123")
# todo=AllTodosView()
# todo.get(todo_Id=2)
# specifictodo=SpecificTodoView()
# print(specifictodo.get())

# update=AllTodosView()
# post={"task_name": "new task"}
# update.put(todoId=2,post=post)
# delete=AllTodosView()
# delete.delete(todo_id=2)
delete()



