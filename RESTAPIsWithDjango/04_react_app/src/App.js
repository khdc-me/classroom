import React, {Component} from 'react';


const list = [
  {
    "id":1,
    "title":"Personal Web Site",
    "description":"Finish it"
  },
  {
    "id":2,
    "title":"LPIC-1",
    "description":"Get the LPIC-1 certification"
  },
  {
    "id":3,
    "title":"New Car",
    "description":"Purchase a new car."
  }
]

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {list};
  }
  
  render() {
    return (
      <div>
        {this.state.list.map(item => (
          <div key={item.id}>
            <h1>{item.title}</h1>
            <p>{item.description}</p>
          </div>
        ))}
      </div>
    );
  }
}

export default App;
