import Relay from 'react-relay'
import Kingdoms from './Kingdoms'

export default Relay.createContainer(Kingdoms, {
  fragments: {
    kingdoms: () => Relay.QL`
      fragment kingdoms on KingdomDefaultConnection {
        edges {
          node {
            kingdomId
            kingdomName
          }
        }
      }`
  }
})
