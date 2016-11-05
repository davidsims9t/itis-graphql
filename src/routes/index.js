import React from 'react'
import { Route, IndexRoute } from 'react-router'

import ViewerQuery from './ViewerQuery'
import Wrapper from '../components/Wrapper'
import KingdomsContainer from '../components/KingdomsContainer'

export default (
  <Route path='/' component={Wrapper}>
    <IndexRoute component={KingdomsContainer} queries={ViewerQuery} />
  </Route>
)
