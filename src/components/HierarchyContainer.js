import Relay from 'react-relay'
import Hierarchy from './Hierarchy'

export default Relay.createContainer(Hierarchy, {
  fragments: {
    hierarchy: () => Relay.QL`
      fragment hierarchy on HierarchyDefaultConnection {
        edges {
          node {
            hierarchyString
          }
        }
      }`
  }
})
