import Relay from 'react-relay'

export default {
  hierarchy: Component => Relay.QL`
    query {
      hierarchy: allHierarchy(first:10, level:10) {
        ${Component.getFragment('hierarchy')}
      }
    }
  `
}
