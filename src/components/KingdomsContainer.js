import Relay from 'react-relay'
import Kingdoms from './Kingdoms'

export default Relay.createContainer(Kingdoms, {
  fragments: {
    viewer: () => Relay.QL`
      fragment on Query {
        kingdoms: allKingdoms(first:10) {
          edges {
            node {
              kingdomId
              kingdomName
              tsn
            }
          }
        }
      }`
  }
})
