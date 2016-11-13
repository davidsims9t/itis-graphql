import Relay from 'react-relay'
import Hierarchy from './Hierarchy'

const nodeFragment = Relay.QL`
  fragment on HierarchyEdge {
    node {
      tsn
      id
      
      children(first:1) {
        edges {
          node {
            tsn
            taxonomicUnit(first:1) {
              edges {
                node {
                  id
                  completeName
                  credibilityRtng
                  taxonUnitType(first:1) {
                    edges {
                      node {
                        id
                        rankName
                      }
                    }
                  }
                }
              }
            }
          }
        }
      }

      taxonomicUnit(first:1) {
        edges {
          node {
            id
            completeName
            credibilityRtng
            taxonUnitType(first:1) {
              edges {
                node {
                  id
                  rankName
                }
              }
            }
          }
        }
      }
    }
  }`

export default Relay.createContainer(Hierarchy, {
  initialVariables: {
    tsn: null
  },

  fragments: {
    viewer: ($tsn) => Relay.QL`
      fragment on Query {
        hierarchies: allHierarchy(first:100, tsn:$tsn) {
          edges {
            ${nodeFragment}
          }
        }
      }`
  }
})
