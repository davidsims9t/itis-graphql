import React, { Component } from 'react'

export default class Kingdoms extends Component {
  render() {
    return (
      <div>
        <h1>Kingdoms</h1>
        <ul>
          {this.props.kingdoms.edges.map(edge => {
            return <li key={edge.node.kingdomId}>{edge.node.kingdomName}</li>
          })}
        </ul>
      </div>
    )
  }
}
