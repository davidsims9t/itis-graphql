import React from 'react'
import { Route, IndexRoute } from 'react-router'

import KingdomQuery from './KingdomQuery'
import HierarchyQuery from './HierarchyQuery'
import Wrapper from '../components/Wrapper'
import KingdomsContainer from '../components/KingdomsContainer'
import HierarchyContainer from '../components/HierarchyContainer'

export default (
  <Route path='/' component={Wrapper}>
    <IndexRoute component={KingdomsContainer} queries={KingdomQuery} />
    <Route path=':hierarchy' component={HierarchyContainer} queries={HierarchyQuery} />
  </Route>
)
