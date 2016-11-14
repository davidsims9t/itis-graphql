import Relay from 'react-relay'
import Hierarchy from './Hierarchy'

const taxonUnitType = Relay.QL`
  fragment on TaxonUnitTypesEdge {
    node {
      id
      rankName
    }
  }
`

const taxonomicUnit = Relay.QL`
  fragment on TaxonomicUnitsEdge {
    node {
      id
      completeName
      credibilityRtng

      taxonUnitType(first:1) {
        edges {
          ${taxonUnitType}
        }
      }
    }
  }
`

// const synonymLinks = Relay.QL`
//   synonymLinks(first:10) {
//     edges {
//       node {
//         tsnAccepted
//       }
//     }
//   }
// `

const childrenWithoutChildren = Relay.QL`
  fragment on HierarchyEdge {
    node {
      tsn
      id

      taxonomicUnit(first:1) {
        edges {
          ${taxonomicUnit}
        }
      }
    }
  }
`

const childrenWithChildren = Relay.QL`
  fragment on HierarchyEdge {
    node {
      tsn
      id

      children(first:1) {
        edges {
          ${childrenWithoutChildren}
        }
      }

      taxonomicUnit(first:1) {
        edges {
          ${taxonomicUnit}
        }
      }
    }
  }
`

const nodeFragment = hasChildren => {
  if (hasChildren) {
    return childrenWithChildren
  } else {
    return childrenWithoutChildren
  }
}

export default Relay.createContainer(Hierarchy, {
  initialVariables: {
    tsn: null,
    level: 6
  },

  fragments: {
    viewer: () => {
      return Relay.QL`
        fragment on Query {
          hierarchies: allHierarchy(first:100, tsn:$tsn, level:$level) {
            edges {
              ${nodeFragment(true)}
            }
          }
        }`
      }
  }
})
