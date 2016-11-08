import React, { Component } from 'react'
import { Card, CardTitle, CardText, List, ListItem, Icon } from 'react-mdl'

export default class Hierarchy extends Component {
  componentWillMount() {
    this.props.relay.setVariables({tsn: parseInt(this.props.params.tsn)})
  }

  render() {
    if (!this.props.viewer.hierarchies) {
      return <div>Loading...</div>
    }

    return (
      <Card style={{width:'100%'}}>
        <CardTitle>List for Kingdom Animalia</CardTitle>

        <CardText style={{padding: 0}}>
          <List style={{padding: 0}}>
            {this.props.viewer.hierarchies.edges.map(edge => {
              return (
                <ListItem key={edge.node.id} style={{display: 'block'}}>
                  <span>
                    Kingdom: {edge.node.taxonomicUnit.edges[0].node.completeName}
                    - TSN: {edge.node.tsn}
                  </span>
                  <List>
                    {edge.node.children.edges.map(edge => {
                      return (
                        <ListItem style={{display: 'block'}}>
                          <span>
                            {edge.node.taxonomicUnit.edges[0].node.taxonUnitType.edges[0].node.rankName.trim()}: {edge.node.taxonomicUnit.edges[0].node.completeName}
                          </span>
                          <span>
                            - TSN: {edge.node.tsn}
                          </span>
                        </ListItem>
                      )
                    })}
                  </List>
                </ListItem>
              )
            })}
          </List>
        </CardText>
      </Card>
    )
  }
}
