import Relay from 'react-relay'
import Hierarchy from './Hierarchy'

export default Relay.createContainer(Hierarchy, {
  fragments: {
    viewer: () => Relay.QL`
      fragment on Viewer {
        hierarchy: allHierarchy(first:10, level: 10) {
          edges {
            node {
              hierarchyString
            }
          }
        }
      }`
  }
})
