import React, { Component } from 'react'

export default class extends Component {
  render() {
    return (
      <div>
        <h1>Kingdoms</h1>
        <ul>
          {this.props.viewer.kingdoms.edges.map(edge => {
            <li key={edge.node.kingdomId}>{edge.node.kingdomId}</li>
          })}
        </ul>
      </div>
    )
  }
}
