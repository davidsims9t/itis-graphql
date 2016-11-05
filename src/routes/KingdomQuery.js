import Relay from 'react-relay'

export default {
  kingdoms: Component => Relay.QL`
    query {
      kingdoms: allKingdoms {
        ${Component.getFragment('kingdoms')}
      }
    }
  `
}
