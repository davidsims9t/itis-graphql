import Relay from 'react-relay'
import Hierarchy from './Hierarchy'

export default Relay.createContainer(Hierarchy, {
  initialVariables: {
    tsn: null
  },

  fragments: {
    viewer: ($tsn) => Relay.QL`
      fragment on Viewer {
        hierarchies: allHierarchy(first:100, tsn:$tsn) {
          edges {
            node {
              tsn
              taxonomicUnit(first:1) {
                edges {
                  node {
                    completeName
                    credibilityRtng
                    taxonUnitType(first:1) {
                      edges {
                        node {
                          rankName
                        }
                      }
                    }
                  }
                }
              }
              children(first:100) {
                edges {
                  node {
                    tsn
                    taxonomicUnit(first:1) {
                      edges {
                        node {
                          completeName
                          credibilityRtng
                          taxonUnitType(first:1) {
                            edges {
                              node {
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
            }
          }
        }
      }`
  }
})
