import React, { Component } from 'react';
import {BrowserRouter, Route} from 'react-router-dom';
import {Header} from './components';
import {RegisterContainer, DetectContainer} from './containers';

class App extends Component {
    render() {
        return (
          <BrowserRouter>
            <div>
              <Header/>
              <Route exact path="/register" component={RegisterContainer}/>
              <Route exact path="/maskdetecting" component={DetectContainer}/>
            </div>
          </BrowserRouter>
        );
    }
}

export default App;