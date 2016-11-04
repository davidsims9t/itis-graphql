import React from 'react'
import ReactDOM from 'react-dom'
import { Router, applyRouterMiddleware, browserHistory } from 'react-router'
import Relay from 'react-relay'
import useRelay from 'react-router-relay'
import Routes from './src/routes'

ReactDOM.render(
  <Router
    render={applyRouterMiddleware(useRelay.default)}
    routes={Routes}
    history={browserHistory}
    environment={Relay.Store} />,
  document.getElementById('mount')
)
