import React from 'react'
import { render } from 'react-dom'
import { Router, browserHistory, applyRouterMiddleware } from 'react-router'
import Relay from 'react-relay'
import useRelay from 'react-router-relay'
import Routes from './components/Routes'

render(
  <Router
    history={browserHistory}
    render={applyRouterMiddleware(useRelay)}
    routes={Routes}
    environment={Relay.Store} />,
  document.getElementById('mount')
)
