import React from 'react'
import { Route, IndexRoute } from 'react-router'

import ViewerQuery from './ViewerQuery'
import Wrapper from '../components/Wrapper'
import KingdomsContainer from '../components/KingdomsContainer'
import HierarchyContainer from '../components/HierarchyContainer'

export default (
  <Route path='/' component={Wrapper}>
    <IndexRoute
      component={KingdomsContainer}
      queries={ViewerQuery} />
    <Route
      path='/hierarchy/:tsn/:level'
      component={HierarchyContainer}
      queries={ViewerQuery} />
  </Route>
)
