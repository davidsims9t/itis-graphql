import React from 'react'
import { IndexRoute } from 'react-router'

import ViewerQuery from './ViewerQuery'
import KingdomsContainer from '../components/KingdomsContainer'

export default (
  <Route path='/'>
    <IndexRoute component={KingdomsContainer} queries={ViewerQuery} />
  </Route>
)
