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
              children(first:10) {
                edges {
                  node {
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
