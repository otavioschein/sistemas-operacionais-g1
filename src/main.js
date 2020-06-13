import React from 'react'
import './App.css'
import data from './data.json'

export default function Main() { 

  /*let bubbleSort = (inputArr) => {
    console.log(`inputArr: ${inputArr}`)
    let len = inputArr.length;
    for (let i = 0; i < len; i++) {
        for (let j = 0; j < len; j++) {
            if (inputArr[j] > inputArr[j + 1]) {
                let tmp = inputArr[j];
                inputArr[j] = inputArr[j + 1];
                inputArr[j + 1] = tmp;
            }
        }
    }
    return inputArr;
  }*/

  function fifo(event) {
    event.preventDefault()

    let dataArray = []

    for (let i = 0; i < data.processes.length; i++) {
      dataArray.push(data.processes[i])
    }
    
    console.log(dataArray[1].name, dataArray[1].start)
  }



  return (
    <div>
      <section className="cards">
            <div className="run-process">
              <form>
                <select name="algorithms" id="algorithms">
                  <option value="fifo">FIFO</option>
                  <option value="sjf">SJF</option>
                  <option value="round-robin">Round Robin</option>
                  <option value="priority">Priority</option>
                </select>
                <input type="submit"  value="Run" onClick={event => fifo(event)} />
              </form>
            </div>

            <div className="card-processo_criado">
              <label>
                {data.processes[0].name}<br></br>
              </label>
              <label>
                {data.processes[0].start}<br></br>
              </label>
              <label>
                {data.processes[0].id}
              </label>
            </div>
          </section>
    </div>
)}