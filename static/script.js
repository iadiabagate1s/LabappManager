window.addEventListener('DOMContentLoaded', (event) =>{
    alert('Log in as an Admin w/  name: admin  lab id: 123456')

})

//on click delete a user .. from DATABASE and remove element from the DOM
$('.deleteuser').on('click',async function(e){
    console.log(e.target)
    let lab_id = $(this).data()
    $(this).parent().parent().remove()
    console.log(lab_id.id)
    console.log(lab_id.last_name)
    
    results = await axios.post(`/user/delete/${lab_id.last_name}`,{
        lab_id
    })

    console.log (results)
})

//on click delete a Project .. from DATABASE and remove element from the DOM
$('.deleteproject').on('click',async function(e){
    console.log(e.target)
    let quote_id = $(this).data()
    $(this).parent().parent().remove()
    console.log(quote_id.id)
    
    await axios.post(`/projects/delete/${quote_id.id}`)

})
//on click delete a Task .. from DATABASE and remove element from the DOM
$('.deletetask').on('click',async function(e){
    console.log(e.target)
    let task_id = $(this).data()
    $(this).parent().parent().remove()

    await axios.post(`/tasks/delete/${task_id.id}`)

})
//handle completing task on user home. removes the complete button and appends the completed task to 
// differnt table 
$('.completetask').on('click',async function(e){
    console.log(e.target)
    let task_id = $(this).data()
    $(this).parent().parent().remove()
    res = await axios.post(`/task/complete/${task_id.id}`)
    task = res.data.task
    $("#compupdate").append(`<tr><td><strong>${task.task_id}</strong>  <strong>${task.company}</strong><p>${task.todo}</p></td></tr>`)

})

