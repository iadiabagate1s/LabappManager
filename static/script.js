
// let login = document.querySelector("#log2")
// login.onload( alert('log in as an admin using last-name: admin   lab-id: 123456 '))



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

// ----------------------------------------------------
function openPage(pageName, elmnt, color) {
    // Hide all elements with class="tabcontent" by default */
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
      tabcontent[i].style.display = "none";
    }
  
    // Remove the background color of all tablinks/buttons
    tablinks = document.getElementsByClassName("tablink");
    for (i = 0; i < tablinks.length; i++) {
      tablinks[i].style.backgroundColor = "";
    }
  
    // Show the specific tab content
    document.getElementById(pageName).style.display = "block";
  
    // Add the specific color to the button used to open the tab content
    elmnt.style.backgroundColor = color;
  }
  
  // Get the element with id="defaultOpen" and click on it
  document.getElementById("defaultOpen").click();
