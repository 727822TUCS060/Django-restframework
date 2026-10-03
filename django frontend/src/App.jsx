import React, { useEffect } from 'react'
import axios from 'axios'

const App = () => {
    const createnewtask=()=>{
        const new_task={
            student_reference:1,
            task_name:"create frontend",
            description:"using react js"
        }
        axios.post('http://127.0.01:8000/student/task_list/',new_task)
        .then(response => console.log(response.data))
        .catch(error => console.log(error))
    }
    const UpdateTask=()=>{
        const new_task={
            student_reference:1,
            task_name:"create frontend applications",
            description:"using react js"
        }
        axios.put('http://127.0.01:8000/student/task_id/3/',new_task)
        .then(response => console.log(response.data))
        .catch(error => console.log(error))
    }
    const deletetask=()=>{
        axios.delete('http://127.0.01:8000/student/task_id/3/')
        .then(response => console.log(response.data))
        .catch(error => console.log(error))
    }
    const gettask=()=>{
        axios.get('http://127.0.01:8000/student/task_list/')
        .then(response => console.log(response.data))
        .catch(error => console.log(error))
    }

  return (
    <div>
      <button onClick={createnewtask}>create task</button>
      <button onClick={UpdateTask}>Update task</button>
      <button onClick={deletetask}>Delete task</button>
      <button onClick={gettask}>Get task</button>
    </div>
  )
}

export default App

