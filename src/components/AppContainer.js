import Relay from 'react-relay'
import App from './App'

export default Relay.createContainer(App, {
  fragments: {
    viewer: () => Relay.QL`
      fragment on User {
        ${App.getFragment('viewer')}
      }`
  }
})
