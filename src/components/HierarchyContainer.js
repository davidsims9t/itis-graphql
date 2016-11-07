import Relay from 'react-relay'
import Hierarchy from './Hierarchy'

export default Relay.createContainer(Hierarchy, {
  fragments: {
    viewer: () => Relay.QL`
      fragment on Viewer {
        hierarchies: allHierarchy(first:10, tsn:202423) {
          edges {
            node {
              tsn
              longname(first:1) {
                edges {
                  node {
                    completename
                  }
                }
              }
              children(first:10) {
                edges {
                  node {
                    longname(first:1) {
                      edges {
                        node {
                          completename
                        }
                      }
                    }
                  }
                }
              }
            }
          }
        }
      }`
  }
})
