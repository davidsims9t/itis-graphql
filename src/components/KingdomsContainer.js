import Relay from 'react-relay'
import Kingdoms from './Kingdoms'

export default Relay.createContainer(Kingdoms, {
  fragments: {
    viewer: () => Relay.QL`
      fragment on Kingdom {
        edges {
          node {
            kingdomId
          }
        }
      }`
  }
})
