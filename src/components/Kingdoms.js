import React, { Component } from 'react'
import { Card, CardTitle, CardText, RadioGroup, Radio } from 'react-mdl'

export default class Kingdoms extends Component {
  constructor(props) {
    super(props)

    this.state = {
      kingdom: null
    }
  }

  onChange = event => {
    this.setState({
      kingdom: event.target.value
    })
  }

  render() {
    return (
      <Card>
        <CardTitle>Select a Kingdom</CardTitle>

        <CardText>
          <RadioGroup name="kingdoms" value={this.state.kingdom} onChange={this.onChange}>
            {this.props.kingdoms.edges.map(edge => {
              return (
                <Radio
                  ripple
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
