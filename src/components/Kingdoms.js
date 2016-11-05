import React, { Component } from 'react'
import { Card, CardTitle, CardText, RadioGroup, Radio } from 'react-mdl'

export default class Kingdoms extends Component {
  onChange = () => {

  }

  render() {
    return (
      <Card>
        <CardTitle>Select a Kingdom</CardTitle>

        <CardText>
          <RadioGroup onChange={this.onChange}>
            {this.props.kingdoms.edges.map(edge => {
              return (
                <Radio
                  key={edge.node.kingdomId}
                  name={edge.node.kingdomId}
                  value={edge.node.kingdomId}>
                  {edge.node.kingdomName}
                </Radio>
              )
            })}
          </RadioGroup>
        </CardText>
      </Card>
    )
  }
}
