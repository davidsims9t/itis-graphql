import Relay from 'react-relay'
import Hierarchy from './Hierarchy'
import { repeat } from 'lodash'

const taxonUnitTypeFragment = Relay.QL`
  fragment on TaxonUnitTypesEdge {
    node {
      id
      rankName
    }
  }
`

const taxonomicUnitFragment = Relay.QL`
  fragment on TaxonomicUnitsEdge {
    node {
      id
      completeName
      credibilityRtng

      taxonUnitType(first:1) {
        edges {
          ${taxonUnitTypeFragment}
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

const childrenFragment = (level, iteration) => {
  if (level === 22 && iteration < 5) {
    const children = childrenFragment(level, iteration + 1)

    return Relay.QL`
      fragment on HierarchyEdge {
        node {
          tsn
          id

          children(first:1000, level:22) {
            edges {
              ${children}
            }
          }

          taxonomicUnit(first:1) {
            edges {
              ${taxonomicUnitFragment}
            }
          }
        }
      }
    `
  } else {
    return Relay.QL`
      fragment on HierarchyEdge {
        node {
          tsn
          id

          taxonomicUnit(first:1) {
            edges {
              ${taxonomicUnitFragment}
            }
          }
        }
      }
    `
  }
}

export default Relay.createContainer(Hierarchy, {
  initialVariables: {
    tsn: null,
    level: 6
  },

  fragments: {
    viewer: () => Relay.QL`
      fragment on Query {
        hierarchies: allHierarchy(first:100, tsn:$tsn) {
          edges {
            ${childrenFragment(22, 0)}
          }
        }
      }`
  }
})
