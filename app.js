import React from 'react'
import ReactDOM from 'react-dom'
import Router from 'react-router'
import Relay from 'react-relay'
import { createHistory } from 'history'

let history = createHistory()

ReactDOM.render(<Router history={history}>{routes}</Router>, document.getElementById('app'))
