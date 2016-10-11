import React from 'react'
import {Route} from 'react-router'
import App from './components/App'
import Kingdom from './components/Kingdom'

export default (
  <Route path="/" component={App}>
    <Route path="/kingdoms" component={Kingdom} />
  </Route>
)
