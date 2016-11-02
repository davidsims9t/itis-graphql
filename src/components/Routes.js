import React from 'react'
import { Route, IndexRoute } from 'react-router'
import App from './AppContainer'
import Kingdom from './Kingdom'
import ViewerQuery from './ViewerQuery'
import Home from './Home'

export default (
  <Route path="/" component={App} queries={ViewerQuery}>
    <IndexRoute component={Home} />
  </Route>
)
