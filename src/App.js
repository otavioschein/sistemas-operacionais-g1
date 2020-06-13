import React, { useState } from 'react';
import './App.css';

function App() {
  const [ id, setId ] = useState(0)
  const [ name, setName ] = useState('')
  const [ time, setTime ] = useState('')
  const [ start, setStart ] = useState('')
  const [ priority, setPriority ] = useState('')

  /*useEffect(() => { // usar o effect apenas quando a variavel mudar, podendo ter mais de uma

  }, [])*/

  function handleAddProcess(e) {
    e.preventDefault()

    setId(id + 1)
    setName(e.name)
    setTime(e.time)
    setStart(e.start)
    setPriority(e.priority)
    
  }
  

  return (
    <section className="cards">
      <div className="card-processo_criacao">
        <form onSubmit={() => handleAddProcess()}>
            <div>
              <input placeholder="Process Name" value={name} onChange={e => setTime(e.target.value)}/>
              <input placeholder="Process Time" value={time} onChange={e => setTime(e.target.value)}/>
              <input placeholder="Process Start" value={start} onChange={e => setStart(e.target.value)}/>
              <input placeholder="Process Priority" value={priority} onChange={e => setPriority(e.target.value)}/>
            </div>
            <button type="submit">Create Process</button>
        </form>
      </div>

      <div className="card-processo_criado">
          <label>
            {id}
          </label>
          <label>
            {name}
          </label>
          <label>
            {time}
          </label>
          <label>
            {start}
          </label>
          <label>
            {priority}
          </label>
      </div>
    </section>
   
  )
  }

export default App;
