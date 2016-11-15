import React, { Component } from 'react'
import { Card, CardTitle, CardText, RadioGroup, Radio, Button } from 'react-mdl'
import { browserHistory } from 'react-router'

const levels = [
  {
    key: 6,
    value: 'Class'
  },
  {
    key: 10,
    value: 'Order'
  },
  {
    key: 14,
    value: 'Family'
  },
  {
    key: 22,
    value: 'Genus'
  }
]

export default class Kingdoms extends Component {
  constructor(props) {
    super(props)

    this.state = {
      tsn: 202423,
      level: 6
    }
  }

  onChangeKingdom = event => {
    this.setState({
      tsn: parseInt(event.target.value)
    })
  }

  onChangeLevel = event => {
    this.setState({
      level: parseInt(event.target.value)
    })
  }

  onClick = () => {
    const { tsn, level } = this.state
    browserHistory.push(`/hierarchy/${tsn}/${level}`)
  }

  render() {
    return (
      <Card style={{width:'100%'}}>
        <CardTitle>Hierarchical Report</CardTitle>

        <CardText>
          <h3 className="mdl-card__title-text">Select a Kingdom:</h3>

          <RadioGroup name="kingdoms" value={this.state.tsn} onChange={this.onChangeKingdom}>
            {this.props.viewer.kingdoms.edges.map(edge => {
              return (
                <Radio
                  ripple
                  key={edge.node.kingdomId}
                  name={edge.node.tsn}
                  value={edge.node.tsn}>
                  {edge.node.kingdomName}
                </Radio>
              )
            })}
          </RadioGroup>

          <h3
            style={{marginTop: '20px'}}
            className="mdl-card__title-text">Run report from kingdom through:</h3>

          <RadioGroup name="level" value={this.state.level} onChange={this.onChangeLevel}>
            {levels.map(level => {
              return (
                <Radio
                  ripple
                  key={level.key}
                  name={level.key}
                  value={level.key}>
                  {level.value}
                </Radio>
              )
            })}
          </RadioGroup>

          <Button
            style={{marginTop: '20px'}}
            ripple
            raised
            primary
            onClick={this.onClick}>
            Submit
          </Button>
        </CardText>
      </Card>
    )
  }
}
