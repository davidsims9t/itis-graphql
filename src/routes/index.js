import React from 'react'
import { Route } from 'react-router'

import ViewerQuery from './ViewerQuery'
import KingdomsContainer from '../components/KingdomsContainer'

export default (
  <Route path='/' component={KingdomsContainer} queries={ViewerQuery} />
)
