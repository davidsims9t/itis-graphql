import React, { Component } from 'react'
import { Card } from 'react-mdl'

export default class Kingdoms extends Component {
  render() {
    return (
      <Card>
        <h1>Kingdoms</h1>
        <ul>
          {this.props.kingdoms.edges.map(edge => {
            return <li key={edge.node.kingdomId}>{edge.node.kingdomName}</li>
          })}
        </ul>
      </Card>
    )
  }
}
